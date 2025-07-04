import re
import time

import cv2
import numpy as np
from pytesseract import pytesseract
from sqlalchemy.orm import joinedload

from db.db_setup import get_session
from db.models import MonsterLevel, BossMonster
from features.utils.use_selected_generals_utils import open_general_selection_list, select_general_from_list
from utils.generals_utils import extract_general_template_image
from utils.helper_utils import get_current_datetime_string
from utils.image_recognition_utils import template_match_coordinates, is_template_match, template_match_coordinates_all, \
    template_match_multiple_sizes


def crop_middle_portion(image, mode):
    """
    Crop the image into three parts (row-wise or column-wise) and store the middle portion.
    :return: The middle portion of the cropped image.
    """
    # Get image dimensions
    height, width, _ = image.shape

    if mode:  # Row-wise cropping
        third_height = height // 3
        middle_crop_top = third_height
        middle_crop_bottom = third_height * 2
        # Crop the middle portion (second third row-wise)
        return image[middle_crop_top:middle_crop_bottom, :]

    else:  # Column-wise cropping
        third_width = width // 3
        middle_crop_left = third_width
        middle_crop_right = third_width * 2
        # Crop the middle portion (second third column-wise)
        return image[:, middle_crop_left:middle_crop_right]


def crop_image_fixed_height(image, height):
    """
    Crop the image starting from the top-left corner (0, 0) with a fixed height (custom height).

    :param image: The image to crop.
    :param height: The height to crop.
    :return: The cropped image.
    """
    # Get image dimensions
    height_img, width_img, _ = image.shape

    # Starting point (0, 0) is fixed
    x1, y1 = 0, 0

    # Define x2 as the width of the image
    x2 = width_img

    # Define y2 as y1 + height (fixed vertical crop distance)
    y2 = min(y1 + height, height_img)  # Ensure y2 does not exceed the image height

    # Crop the image using the defined coordinates
    cropped_img = image[y1:y2, x1:x2]

    return cropped_img


def crop_boss_text_area(src_img):
    """Dynamically crop the marked green rectangle area based on proportional values."""

    # Get image dimensions
    height, width = src_img.shape[:2]

    # Define cropping ratios (based on analysis of the 540p image)
    left_ratio = 0.55  # Start column (percentage of width)
    right_ratio = 0.95  # End column (percentage of width)
    top_ratio = 0.22  # Start row (percentage of height)
    bottom_ratio = 0.37  # End row (percentage of height)

    # Convert ratios to pixel values
    left = int(width * left_ratio) + 25
    right = int(width * right_ratio) + 13
    top = int(height * top_ratio)
    bottom = int(height * bottom_ratio) - 75

    # Ensure cropping remains within valid bounds
    left = min(left, width - 1)
    right = min(right, width)
    top = min(top, height - 1)
    bottom = min(bottom, height)

    # Crop the region of interest (ROI)
    cropped_img = src_img[top:bottom, left:right]

    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\boss_text_img_{get_current_datetime_string()}.png", cropped_img)
    return cropped_img


def extract_monster_name_from_image(src_img):
    # Yellow text to black and rest to white
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for the yellow color
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create a mask for the yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Replace the yellow color with black
    result = cv2.bitwise_and(src_img, src_img, mask=mask)
    result[mask > 0] = (0, 0, 0)

    # Replace the remaining pixels with white
    result[mask == 0] = (255, 255, 255)

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # gray = cv2.medianBlur(gray, 3)
    # new code(uncomment medianBlur and comment the following if there is an issue)
    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adjust the contrast of the image
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(blurred, alpha=alpha, beta=beta)

    # Apply adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(adjusted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    # Apply dilation and erosion to enhance text
    kernel = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(adaptive_thresh, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)

    kernel_sharpen = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
    sharpened = cv2.filter2D(erosion, -1, kernel_sharpen)

    # Apply adaptive thresholding to make text stand out
    processed = cv2.adaptiveThreshold(sharpened, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)


    # cv2.imwrite(r"C:\Users\evsah\Jupyter\assets\output\boss_name.png",processed)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\boss_text_img_filter_{get_current_datetime_string()}.png",
    #             processed)

    # OCR Configuration (allow letters & numbers, but not special characters except .)
    custom_config = '--oem 3 --psm 6 -c tessedit_char_whitelist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789."'
    monster_info_text = pytesseract.image_to_string(processed,config=custom_config).replace(" ", "").replace("\n","").lower()
    return monster_info_text



def lookup_boss_by_name(extracted_monster_name):
    """
    Finds all MonsterLevel objects where the name column matches the extracted monster name.
    The extracted name is already normalized (lowercase, alphanumeric + periods).
    """
    # Use a context manager to handle session lifecycle
    with get_session() as session:
        # Fetch all boss IDs and names
        monster_levels = session.query(MonsterLevel.id, MonsterLevel.name, MonsterLevel.boss_monster_id).all()

        # Normalize database names and find matches locally
        matching_ids = [
            monster.id for monster in monster_levels
            if normalize_boss_text(monster.name) == extracted_monster_name
        ]

        # Fetch MonsterLevel with `monster_logic_id` attached directly in the query
        if matching_ids:
            bosses = (
                session.query(
                    MonsterLevel,  # Retrieve the full MonsterLevel object
                    BossMonster.monster_logic_id.label("logic_id")  # Attach logic_id dynamically
                )
                .join(BossMonster, BossMonster.id == MonsterLevel.boss_monster_id)
                .filter(MonsterLevel.id.in_(matching_ids))
                .options(joinedload(MonsterLevel.boss_monster))
                .all()
            )
            # The list contains tuples: (MonsterLevel object, logic_id)
            return bosses

        # Return None if no matches found
        return None

def normalize_boss_text(text):
    """
    Removes spaces, dashes, and parentheses, keeping only alphanumeric + periods.
    """
    return text.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").lower()


def click_join_alliance_war_btn(thread):
    join_alliance_war_btn_img = cv2.imread("assets/540p/join rally/join_alliance_war_btn.png")

    src_img = thread.capture_and_validate_screen()
    join_alliance_war_btn_match = template_match_coordinates(src_img, join_alliance_war_btn_img)
    if not join_alliance_war_btn_match:
        # print("Cannot find the alliance war join button")
        return False
    thread.adb_manager.tap(*join_alliance_war_btn_match)

def preset_option_use_selected_generals(thread):
    selected_preset = thread.cache['join_rally_controls']['settings']['selected_presets']
    # Empty the selected main general cache
    thread.cache['join_rally_controls']['cache']['selected_main_general_id'] = None
    selected_main_general_id = thread.cache['join_rally_controls']['cache']['selected_main_general_id']

    # Loop over main and assistant general in order
    for general_type in [True,False]:
        generals_list = selected_preset.get('main_generals' if general_type else 'assistant_generals', [])
        # print(f"{'Main Gen' if general_type else 'Assistant Gen'} :: {selected_main_general_id}")
        # Check if the list contains any main general in it
        if not generals_list and general_type:
            # print("At least one main general should be selected to continue using the selected general option")
            thread.log_message(f"No main general selected. At least one must be chosen to use the selected general option.", level="info")
            return False

        # Check if the list contains any assistant general in it
        if not generals_list and not general_type:
            # print("No assistant generals to select, skipping.")
            thread.log_message(f"No assistant generals selected. Proceeding without assistant generals.", level="info")
            continue  # Skip assistant selection if no assistants and not main

        # Remove selected main general from the assistant general list
        if selected_main_general_id and not general_type:
            generals_list[:] = [gen for gen in generals_list if gen['id'] != selected_main_general_id]
            selected_main_general_id = None

        # Load general template images
        for general in generals_list:
            # Details View
            details_image_path = f"assets\\540p\\generals\\{general.get('details_image_name')}"
            details_image = extract_general_template_image(cv2.imread(details_image_path))
            general['details_image'] = details_image

            # List View
            list_image_path = f"assets\\540p\\generals\\{general.get('list_image_name')}"
            list_image = extract_general_template_image(cv2.imread(list_image_path), view=False)
            general['list_image'] = list_image

        # Open general selection window
        open_general_selection_window = open_general_selection_list(thread,general_type)
        # When main general selection window is not opened (assistant is optional)
        if not open_general_selection_window and general_type:
            # print("Failed to open main general selection window")
            thread.log_message(f"Unable to open main general selection window.", level="info")
            return False
        elif not open_general_selection_window and not general_type:
            # print("Failed to open assistant general selection window(no assistant general enabled)")
            thread.log_message(f"No assistant generals available for the selected main general. Skipping assistant selection.", level="info")
            continue

        # Select the general
        if open_general_selection_window:
            general_selected, selected_main_general_id = select_general_from_list(thread, generals_list, selected_preset['general_preset_config'])

            # When main general is not selected, then skip the preset (assistant is not mandatory)
            if not general_selected and general_type:
                thread.adb_manager.press_back()
                time.sleep(1)
                return False
            # Just press back for assistant general
            if not general_selected and not general_type:
                thread.adb_manager.press_back()
                time.sleep(1)

    return True



def preset_option_skip_no_general(thread):
    no_main_general_img = cv2.imread("assets/540p/join rally/no_main_general.png")
    src_img = thread.capture_and_validate_screen()
    if is_template_match(src_img,no_main_general_img):
        return False
    return True


def preset_option_reset_to_one_troop(thread):
    src_img = thread.capture_and_validate_screen()

    # Check the troops count
    troops_count = check_selected_troops_count(src_img.copy())
    if troops_count == 1:
        # print("Troop count verified; only selected one troop")
        thread.log_message(f"Troop count verified. Only one troop is selected as required.", level="info")
        return True

    # If count is not 1, then set the count to 1
    # print("Troop count is not 1. Attempting to select one troop...")
    thread.log_message(f"Troop count is not 1. Attempting to select only one troop.", level="info")
    if select_one_troop(thread):
        # Optionally, recheck the troop count to confirm
        src_img = thread.capture_and_validate_screen(ads=False)
        troops_count = check_selected_troops_count(src_img.copy())
        if troops_count == 1:
            # print("New Troop count verified; only selected one troop")
            thread.log_message(f"Troop selection adjusted. Only one troop is now selected.", level="info")
            return True

    return False


def check_selected_troops_count(src_img):
    troops_count_img = cv2.imread("assets/540p/join rally/troops_count.png")
    # Crop the img area where the troop count is present
    troops_count_img_match = template_match_coordinates(src_img, troops_count_img, return_center=False)
    if troops_count_img_match:
        x1, y1 = troops_count_img_match  # Extract top-left corner of matched template
        w, h = troops_count_img.shape[:-1]  # Width & height of the template image

        # Crop the area *after* the matched template
        roi = src_img[y1:y1 + h, x1 + w:x1 + w + 160].copy()  # Start after the match

        # Check if the troop selected already is 1
        troops_count = pytesseract.image_to_string(roi, config='--psm 6')
        # print(troops_count)
        troops_count = troops_count.split('/')[0]
        try:
            troops_count = int(re.sub(r'\D', '', troops_count))
        except Exception as e:
            # change the count to a negative value
            troops_count = -1
        finally:
            return troops_count
    else:
        return -1


def select_one_troop(thread):
    """
    Selects exactly one troop by switching to the 'One Soldier' preset and applying it.
    The preset cycling order is: 1 Full Tiers -> Power First -> One Soldier.

    Args:
        thread: The thread object containing cache and adb_manager.

    Returns:
        bool: True if one troop was successfully selected, False otherwise.
    """
    # Template images for the three presets
    power_first_template = cv2.imread("assets/540p/join rally/preset_power_first_img.png")
    one_full_tiers_template = cv2.imread("assets/540p/join rally/preset_one_full_tiers_img.png")
    one_soldier_template = cv2.imread("assets/540p/join rally/preset_one_soldier_img.png")

    # Template images for the Reset and One Troop buttons
    reset_btn_template = cv2.imread("assets/540p/join rally/preset_reset_btn.png")
    one_troop_btn_template = cv2.imread("assets/540p/join rally/preset_one_soldier_btn.png")

    # Maximum attempts to cycle through presets
    # Since the order is 1 Full Tiers -> Power First -> One Soldier,
    # it takes at most 2 clicks to reach One Soldier from any preset:
    # - 1 Full Tiers -> Power First -> One Soldier (2 clicks)
    # - Power First -> One Soldier (1 click)
    # - One Soldier -> (0 clicks)
    max_attempts = 2
    attempts = 0

    while attempts < max_attempts:
        # Capture the current screen
        src_img = thread.capture_and_validate_screen(ads=False)

        # Check if the One Soldier preset is already selected
        one_soldier_match = template_match_coordinates(src_img, one_soldier_template, threshold=0.9)
        if one_soldier_match:
            # print("One Soldier preset is already selected.")
            # Check for the Reset button
            reset_btn_match = template_match_coordinates(src_img, reset_btn_template, threshold=0.9)
            if reset_btn_match:
                # print("Reset button found. Clicking to clear troop selection...")
                thread.adb_manager.tap(*reset_btn_match)
                time.sleep(1)

                # Capture the screen again to check for the One Troop button
                src_img = thread.capture_and_validate_screen(ads=False)
                one_troop_btn_match = template_match_coordinates(src_img, one_troop_btn_template, threshold=0.9)
                if one_troop_btn_match:
                    # print("One Troop button found. Clicking to select one troop...")
                    thread.adb_manager.tap(*one_troop_btn_match)
                    time.sleep(1)
                    return True
                else:
                    # print("One Troop button not found after resetting.")
                    return False
            else:
                # If no Reset button, check for the One Troop button directly
                one_troop_btn_match = template_match_coordinates(src_img, one_troop_btn_template, threshold=0.9)
                if one_troop_btn_match:
                    # print("One Troop button found. Clicking to select one troop...")
                    thread.adb_manager.tap(*one_troop_btn_match)
                    time.sleep(1)
                    return True
                else:
                    # print("Neither Reset nor One Troop button found.")
                    return False

        # If One Soldier preset is not selected, check for the other presets
        # Check 1 Full Tiers first (since it requires 2 clicks to reach One Soldier)
        one_full_tiers_match = template_match_coordinates(src_img, one_full_tiers_template, threshold=0.9)
        if one_full_tiers_match:
            # print("1 Full Tiers preset is selected. Clicking to cycle to Power First...")
            thread.adb_manager.tap(*one_full_tiers_match)
            time.sleep(1)
            attempts += 1
            continue

        # Check Power First (requires 1 click to reach One Soldier)
        power_first_match = template_match_coordinates(src_img, power_first_template, threshold=0.9)
        if power_first_match:
            # print("Power First preset is selected. Clicking to cycle to One Soldier...")
            thread.adb_manager.tap(*power_first_match)
            time.sleep(1)
            attempts += 1
            continue

        # If none of the presets are found, something is wrong
        # print("No preset template matched. Unable to cycle presets.")
        return False

    # print("Max attempts reached while trying to cycle to One Soldier preset.")
    return False

def validate_and_apply_stamina(thread):
    src_img = thread.capture_and_validate_screen(ads=False)
    stamina_confirm_img = cv2.imread("assets/540p/join rally/confirm_btn.png")

    if not is_template_match(src_img,stamina_confirm_img):
        # print("Stamina already available")
        return True

    # print("Insufficient stamina to join the rally.")
    thread.log_message(f"Insufficient stamina to join the rally.", level="info")

    # Get auto use stamina settings
    auto_use_stamina = thread.cache['join_rally_controls']['settings']['auto_use_stamina']

    # If auto_use_stamina is not enabled
    if not auto_use_stamina['enabled']:
        # print("Auto-use stamina option is not enabled, so skipping the operation")
        thread.log_message(f"Auto-use stamina is disabled. Skipping operation due to insufficient stamina.", level="info")
        thread.adb_manager.press_back()
        return False

    # If enabled, then proceed with applying the stamina
    # print("Stamina will be automatically refilled to continue joining rallies.")
    thread.log_message(f"Auto-use stamina is enabled. Refilling stamina to continue joining rallies.", level="info")

    # Get the matched cords to tap the button
    stamina_confirm_match = template_match_coordinates(src_img,stamina_confirm_img)

    thread.adb_manager.tap(*stamina_confirm_match)
    time.sleep(1)

    # Refill stamina
    if not refill_stamina(thread,auto_use_stamina['option']):
        # print("No available stamina found for refill.")
        thread.log_message(f"No available stamina found for refill.", level="info")
        thread.adb_manager.press_back()
        thread.adb_manager.press_back()
        time.sleep(1)
        return False
    return True

def refill_stamina(thread,option):
    stamina_packs = [{'quantity': 100, 'path': 'assets/540p/join rally/stamina_100.png'},
                     {'quantity': 50, 'path': 'assets/540p/join rally/stamina_50.png'},
                     {'quantity': 25, 'path': 'assets/540p/join rally/stamina_25.png'},
                     {'quantity': 10, 'path': 'assets/540p/join rally/stamina_10.png'}]

    stamina_use = cv2.imread('assets/540p/join rally/stamina_use.png')
    confirm_use = cv2.imread('assets/540p/join rally/confirm_use.png')
    max_stamina = cv2.imread('assets/540p/join rally/max_stamina.png')
    add_max_stamina = cv2.imread('assets/540p/join rally/add_max_stamina.png')

    thread.adb_manager.swipe(250, 810, 250, 520, 1500)
    time.sleep(1)
    src_img = thread.capture_and_validate_screen()

    # Loop the stamina list
    for stamina in stamina_packs:
        if not thread.thread_status():
            return False
        # print(stamina['quantity'], " ", stamina['path'])
        stamina_img = cv2.imread(stamina['path'])
        # print(stamina['quantity'])
        if not is_template_match(src_img, stamina_img):
            # print(stamina['quantity'], "Pack not found")
            # print(f"{stamina['quantity']} vit stamina pack not found")
            thread.log_message(f"{stamina['quantity']} vit stamina pack not found.", level="info")
            continue
        result = cv2.matchTemplate(src_img, stamina_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + src_img.shape[0], top_left[1] + stamina_img.shape[1])
        roi = (src_img[top_left[1]:bottom_right[1], 0:bottom_right[0]].copy())
        # Cropping roi to get the second half to eliminate text "use" in the description
        roi_h, roi_w = roi.shape[:2]
        roi = roi[0:roi_h, roi_w // 2:roi_w]
        # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\roi_{get_current_datetime_string()}.png", roi)
        apply_stamina = template_match_coordinates(roi, stamina_use)
        if not apply_stamina:
            stamina_use = cv2.imread('assets/540p/join rally/stamina_use_alt.png')
            apply_stamina = template_match_coordinates(roi, stamina_use)
            if not apply_stamina:
                # print(f"{stamina['quantity']} vit stamina pack is empty")
                thread.log_message(f"{stamina['quantity']} vit stamina pack is empty", level="info")
                continue
        thread.adb_manager.tap(int((roi_w / 2) + apply_stamina[0]), int(apply_stamina[1] + top_left[1]))
        time.sleep(1)
        src_img = thread.capture_and_validate_screen()
        if option == 'Min Stamina':
            # print("Utilizing upto 100 vit stamina for the operation.")
            thread.log_message(f"Utilizing upto 100 vit stamina for the operation.", level="info")
            max_stamina_btn = template_match_coordinates(src_img, max_stamina)
            if max_stamina_btn:
                thread.adb_manager.tap(*max_stamina_btn)
        else:
            # print("Utilizing maximum stamina for the operation.")
            thread.log_message(f"Utilizing maximum stamina for the operation.", level="info")
            max_stamina_btn = template_match_coordinates(src_img, add_max_stamina)
            if max_stamina_btn:
                thread.adb_manager.tap(*max_stamina_btn)

        confirm_stamina = template_match_coordinates(src_img, confirm_use)
        if confirm_stamina:
            thread.adb_manager.tap(*confirm_stamina)
            time.sleep(0.5)
            thread.adb_manager.press_back()
            time.sleep(1)
            src_img = thread.capture_and_validate_screen(ads=False)
            march_btn = cv2.imread("assets/540p/join rally/march_btn.png")
            march_btn_match = template_match_coordinates(src_img, march_btn, convert_gray=False)
            if not march_btn_match:
                return False
            thread.adb_manager.tap(*march_btn_match)
            time.sleep(2)
            return True
    # If execution reaches this line, it means no stamina found/used
    # print("No Stamina Found")
    return False


def extract_monster_power_from_image(img):
    monster_power_icon_img = cv2.imread("assets/540p/join rally/monster_power_icon.png")

    # Get image dimensions
    height, width = img.shape[:2]

    # Crop the top-right quadrant
    x_start = width // 2  # Start from the middle horizontally
    y_start = 0  # Start from the top
    x_end = width  # End at full width
    y_end = height // 2  # End at the middle vertically
    top_right_img = img[y_start:y_end, x_start:x_end]  # Crop top-right quadrant

    # Convert top-right image to grayscale for template matching
    src_gray = cv2.cvtColor(top_right_img, cv2.COLOR_BGR2GRAY)
    icon_gray = cv2.cvtColor(monster_power_icon_img, cv2.COLOR_BGR2GRAY)

    # Perform template matching to find the power icon
    result = cv2.matchTemplate(src_gray, icon_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8  # Match confidence threshold
    if max_val < threshold:
        print("⚠️ Power icon not found in the image.")
        return None

    # Crop the power text based on the icon's position
    match_x, match_y = max_loc  # Top-left coordinates of the match
    icon_h, icon_w = icon_gray.shape[:2]

    x1 = match_x + icon_w  # Start just after the icon
    y1 = match_y  # Align with the icon
    x2 = x1 + 150  # Approximate width for power text
    y2 = y1 + icon_h  # Keep same height as icon

    cropped_power_text = top_right_img[y1:y2, x1:x2]  # Crop the power text area

    # Refine the cropped image (trim extra right-side parts)
    hsv = cv2.cvtColor(cropped_power_text, cv2.COLOR_BGR2HSV)
    # lower_blue = np.array([90, 50, 50])
    # upper_blue = np.array([130, 255, 255])
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Define HSV range for white
    lower_white = np.array([0, 0, 200])  # Low hue, low saturation, high value (brightness)
    upper_white = np.array([180, 50, 255])  # Full hue range, low saturation, max brightness
    mask = cv2.inRange(hsv, lower_white, upper_white)

    cols = np.any(mask, axis=0)  # Find white background columns
    if np.any(cols):
        x2 = np.max(np.where(cols)) + 3  # Get rightmost white pixel
    else:
        x2 = cropped_power_text.shape[1]  # Default to full width if no white detected

    refined_cropped_power_text = cropped_power_text[:, :x2]  # Crop up to the detected white area

    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\crop_{get_current_datetime_string()}.png", refined_cropped_power_text)

    # Extract text using OCR
    gray = cv2.cvtColor(refined_cropped_power_text, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    extracted_text = pytesseract.image_to_string(binary, config="--psm 7").strip()

    return extracted_text



def get_valid_rallies_area_cords(thread):
    """
    Return the cords of the image area which contains the monster tag, cords(map icon) and join button with time
    """
    # Capture the current screen
    src_img = thread.capture_and_validate_screen(ads=False)

    # Load template images
    boss_monster_tag_img = cv2.imread("assets/540p/join rally/boss_monster_tag.png")
    join_btn_img = cv2.imread("assets/540p/join rally/join_btn.png")
    map_pinpoint_img = cv2.imread("assets/540p/join rally/map_pinpoint_tag.png")

    # Get the boss monster rallies matches
    boss_monster_tag_matches = template_match_coordinates_all(src_img, boss_monster_tag_img)
    valid_cords = []
    # Loop through each boss monster tag match
    for (x1, y1) in boss_monster_tag_matches:
        # Define a limited ROI: From (x1, y1) to (end of width, y1 + 200)
        roi_y_end = min(y1 + 200, src_img.shape[0])  # Ensure it wont exceed the image height to avoid wrong set matching
        roi = src_img[y1:roi_y_end, x1:]

        # Check for join button within the ROI
        join_btn_matches = template_match_coordinates(roi, join_btn_img, False)

        if not join_btn_matches:
            continue

        # Get the first match coordinates for join_btn inside the ROI
        match_x1, match_y1 = join_btn_matches

        # Define the region for the cords icon(map pinpoint icon) template match
        combined_roi_x1 = x1
        combined_roi_y1 = y1
        combined_roi_x2 = x1 + match_x1 + join_btn_img.shape[1]  # add join_btn_img width
        combined_roi_y2 = y1 + match_y1 + join_btn_img.shape[0] * 2  # add join_btn_img height twice

        # Create an image area to scan for the map pinpoint icon (to get the cords of the monsters)
        combined_roi = src_img[combined_roi_y1:combined_roi_y2, combined_roi_x1:combined_roi_x2]

        # Search for the map pinpoint icon inside the combined ROI
        map_pinpoint_match = template_match_coordinates(combined_roi, map_pinpoint_img, False)

        if not map_pinpoint_match:
            continue

        # Get the map pinpoint coordinates relative to the combined ROI
        map_pinpoint_x1, map_pinpoint_y1 = map_pinpoint_match

        # Adjust combined ROI to start from the map pinpoint match coordinates
        adjusted_x1 = combined_roi_x1 + map_pinpoint_x1
        adjusted_y1 = combined_roi_y1 + map_pinpoint_y1
        adjusted_x2 = combined_roi_x2  # Keep the previous x2 boundary
        adjusted_y2 = combined_roi_y2  # Keep the previous y2 boundary

        # Create the adjusted combined ROI
        # adjusted_combined_roi = src_img[adjusted_y1:adjusted_y2, adjusted_x1:adjusted_x2]
        # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\{x1},{y1}.png",adjusted_combined_roi)

        valid_cords.append((adjusted_x1, adjusted_y1, adjusted_x2, adjusted_y2))

    return valid_cords

def check_skipped_rallies(thread,src_img):
    """
    Validate before proceeding to join
    """
    scales = np.arange(0.3, 1, 0.01)

    # Check skipped list
    for i, cords_img in enumerate(thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img']):
        # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\src_img_{get_current_datetime_string()}.png", src_img)

        match_result, _ = template_match_multiple_sizes(src_img, cords_img, scales, return_center=False, convert_gray=False)

        if match_result:
            # print("Already skipped one")
            return False

    return True

def add_rally_cord_to_skip_list(thread, boss_text_img):
    map_pinpoint_tag_img = cv2.imread("assets/540p/join rally/map_pinpoint_tag.png")

    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\skip_rally_{get_current_datetime_string()}.png", boss_text_img)

    # Find the top-left corner of the match
    map_pinpoint_match = template_match_coordinates(boss_text_img, map_pinpoint_tag_img, return_center=False)
    if map_pinpoint_match is None:
        # print("No match found.")
        return None

    # Unpack the top-left corner (x1, y1)
    x1, y1 = map_pinpoint_match

    # Set x2 and y2 to the bottom-right corner of the boss_text_img
    h, w = boss_text_img.shape[:2]
    x2 = w - 23
    y2 = h

    # Crop the image from (x1, y1) to the end of the image
    cropped_img = boss_text_img[y1:y2, x1:x2]
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\template_img_{get_current_datetime_string()}.png", cropped_img)

    thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img'].append(cropped_img)