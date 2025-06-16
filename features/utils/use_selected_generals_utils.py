import time

import cv2

from utils.generals_utils import select_general_category, select_general_view, apply_general_filter
from utils.helper_utils import get_current_datetime_string
from utils.image_recognition_utils import template_match_coordinates_all, template_match_coordinates, is_template_match


def open_general_selection_list(thread,main_general):
    general_info_magnifier_icon_img = cv2.imread("assets/540p/join rally/general_info_magnifier_icon.png")
    general_empty_slot_btn_img = cv2.imread("assets/540p/join rally/general_empty_slot_btn.png")

    src_img = thread.capture_and_validate_screen()

    # Check if any generals are already selected
    matched_general_magnifier_icons = template_match_coordinates_all(src_img, general_info_magnifier_icon_img)

    # Reverse the list of coord based on the type of general to select
    if not main_general:
        matched_general_magnifier_icons.reverse()
        # When only one match found, set the matches to None (Assistant General)
        if len(matched_general_magnifier_icons) == 1:
            matched_general_magnifier_icons = None

    # When no match found, look for the empty general slot icon
    if not matched_general_magnifier_icons:

        matched_general_empty_slot_btn = template_match_coordinates(src_img,general_empty_slot_btn_img)
        if matched_general_empty_slot_btn:

            thread.adb_manager.tap(*matched_general_empty_slot_btn)
            time.sleep(1)
            return True

        return False

    # When match found, then change and select the general from list
    if matched_general_magnifier_icons:

        matched_general_magnifier_icons = matched_general_magnifier_icons[0]

        # Find corresponding coordinates where the general icon is, to change it
        new_coord = find_corresponding_coordinates(*matched_general_magnifier_icons, *src_img.shape[:2])
        # print(new_coord)
        thread.adb_manager.tap(*new_coord)
        time.sleep(1)
        return True

    return False


def select_general_from_list(thread,generals_list,general_preset_config):
    selected_main_general_id = None
    # General View
    general_view = select_general_view(thread, general_preset_config['general_view'].lower())
    if not general_view:
        return False

    # General Category
    general_category = select_general_category(thread, general_preset_config['general_category'].lower())
    if not general_category:
        return False

    # General Filter
    favorite_filter = False if general_preset_config.get('general_filter') is None else 'favorite' in general_preset_config.get('general_filter', '')
    idle_filter = False if general_preset_config.get('general_filter') is None else 'idle' in general_preset_config.get('general_filter', '')
    apply_general_filter(thread,favorite_filter, idle_filter)

    # Search for the general in the list
    swipe_limit = general_preset_config['swipe_attempts']
    swipe_count = 0
    general_selected = False
    selected_view = True if 'details' in general_preset_config['general_view'].lower() else False

    while swipe_count < swipe_limit and not general_selected:
        # Capture the current screen
        src_img = thread.capture_and_validate_screen()

        # Loop through general templates
        for general in generals_list:
            general_template = general['details_image'] if selected_view else general['list_image']
            if is_template_match(src_img, general_template, threshold=0.9):
                # General match found, select it based on the view type
                if selected_view:
                    general_selected = details_view_select_general(thread, src_img, general)
                    # If buffer swipe added to adjust the select/resign button, call the function again
                    if general_selected is None:
                        src_img = thread.capture_and_validate_screen()
                        general_selected = details_view_select_general(thread, src_img, general)
                else:
                    general_selected = list_view_select_general(thread, src_img, general)
                selected_main_general_id = general['id']
                break

        if general_selected:
            break

        # General not found, swipe the list to reveal more generals
        if selected_view: # Detail View
            thread.adb_manager.swipe(270, 750, 270, 250, duration=1000)
        else: # List View
            thread.adb_manager.swipe(270, 800, 270, 250, duration=1000)

        time.sleep(1)  # Wait for the list to settle
        swipe_count += 1

    # Check if a general was selected
    if not general_selected:
        print("Reached swipe limit without finding any general from the list.")
        return False, None

    return True, selected_main_general_id

def list_view_select_general(thread, src_img, general):
    select_a_general_tag_img = cv2.imread("assets/540p/other/select_a_general_tag.png")
    general_template_match = template_match_coordinates(src_img, general['list_image'])
    if general_template_match:
        thread.adb_manager.tap(*general_template_match)
        print(f"Selecting {general['name']}")
        time.sleep(1)
        # Check if the general is already selected
        src_img = thread.capture_and_validate_screen(ads=False)
        if is_template_match(src_img,select_a_general_tag_img):
            print(f"General {general['name']} is already selected")
            thread.adb_manager.press_back()
            time.sleep(1)

        return True

    return False

def details_view_select_general(thread, src_img, general):

    select_general_btn_img = cv2.imread("assets/540p/other/select_general_btn.png")
    resign_general_btn_img = cv2.imread("assets/540p/other/resign_general_btn.png")

    general_template_match = template_match_coordinates(src_img, general['details_image'])
    if not general_template_match:
        return False
    # cv2.imwrite(f"temp/src_{get_current_datetime_string()}.png", src_img)
    # cv2.imwrite(f"temp/template_{get_current_datetime_string()}.png", general['details_image'])

    print(f"Match found : {general['name']}")
    # Get the coordinates to crop the matched location
    match_x, match_y = general_template_match[0], general_template_match[1]  # Top-left of match
    template_h, template_w = general['details_image'].shape[:2]  # Height and width of template

    # Define search region: from bottom of general match to end of image
    y1 = match_y + template_h  # Start just below the template
    x1 = match_x  # Start at the match's x
    y2 = src_img.shape[0]  # End at the bottom of the image
    x2 = src_img.shape[1]  # End at the right edge of the image
    roi = src_img[y1:y2, x1:x2].copy()

    # cv2.imwrite(f"temp/cropped_area_{get_current_datetime_string()}.png", roi)

    # Perform template matching for both buttons in the ROI
    resign_match = template_match_coordinates_all(roi, resign_general_btn_img,convert_gray=False)
    select_match = template_match_coordinates_all(roi, select_general_btn_img, convert_gray=False)

    # Check if any matches are found
    if not resign_match and not select_match:
        print("No Resign or Select button found, adjusting the swipe.")
        thread.adb_manager.swipe(270, 750, 270, 650, duration=1000)
        time.sleep(1)
        return None

    # Initialize variables for first match coordinates
    resign_x, resign_y = None, float('inf')  # Default to infinity if no match
    select_x, select_y = None, float('inf')  # Default to infinity if no match

    # Extract first match if present
    if resign_match:
        resign_x, resign_y = resign_match[0]
    if select_match:
        select_x, select_y = select_match[0]

    # Determine action based on matches
    if resign_y != float('inf') and select_y != float('inf'):
        # Both buttons found, compare y coordinates to find the closest
        general_bottom_y = match_y + template_h
        resign_distance = abs(resign_y - general_bottom_y)
        select_distance = abs(select_y - general_bottom_y)

        if resign_distance < select_distance:
            print("Resign button is closer, backing.")
            thread.adb_manager.press_back()
            time.sleep(1)
            return True
        else:
            print("Select button is closer, tapping.")
            thread.adb_manager.tap(select_x + x1, select_y + y1)  # Adjust for ROI offset
            time.sleep(1)
            return True
    elif resign_y != float('inf'):
        # Only Resign button found
        print("Resign button found, tapping.")
        thread.adb_manager.press_back()
        time.sleep(1)
        return True
    elif select_y != float('inf'):
        # Only Select button found
        print("Select button found, tapping.")
        thread.adb_manager.tap(select_x + x1, select_y + y1)  # Adjust for ROI offset
        time.sleep(1)
        return True

    return False



def find_corresponding_coordinates(x_match, y_match, image_height, image_width):
    # Find corresponding coordinate to find the general icon to open the general selection list
    # Validate input coordinates
    if not (0 <= x_match < image_width and 0 <= y_match < image_height):
        print(f"Invalid coordinates: ({x_match}, {y_match}) for image size {image_width}x{image_height}")
        return None

    # Calculate the midpoint of the image (split vertically into two equal halves)
    midpoint = image_width // 2

    # Determine which half the match is in and calculate the corresponding x-coordinate
    if x_match >= midpoint:
        # Match is in the second half (x >= midpoint)
        offset = x_match - midpoint
        # Mirror the offset into the first half
        # The end of the first half is at (midpoint - 1)
        x_corresponding = (midpoint - 1) - offset
    else:
        # Match is in the first half (x < midpoint)
        offset = x_match
        # Mirror the offset into the second half
        # The start of the second half is at midpoint
        x_corresponding = midpoint + offset

    # The y-coordinate remains the same
    y_corresponding = y_match

    # Ensure the corresponding x-coordinate is within bounds
    if not (0 <= x_corresponding < image_width):
        print(f"Corresponding x-coordinate {x_corresponding} is out of bounds for image width {image_width}")
        return None

    return x_corresponding, y_corresponding
