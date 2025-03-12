
import time
from datetime import timedelta

import cv2
from features.utils.join_rally_helper_utils import crop_middle_portion, crop_image_fixed_height, crop_boss_text_area, \
    extract_monster_name_from_image, lookup_boss_by_name
from utils.get_controls_info import get_join_rally_controls
from utils.helper_utils import parse_timer_to_timedelta, get_current_datetime_string
from utils.image_recognition_utils import is_template_match, draw_template_match, template_match_coordinates_all, \
    template_match_coordinates
from utils.navigate_utils import navigate_join_rally_window
from utils.text_extraction_util import extract_remaining_rally_time_from_image, extract_join_rally_time_from_image, \
    extract_monster_power_from_image


def run_join_rally(thread):
    # Get the controls and store it in the thread cache
    if 'join_rally_controls' not in thread.cache:
        thread.cache['join_rally_controls'] = get_join_rally_controls(thread.main_window, thread.index)
    # print(thread.cache['join_rally_controls']['settings']['join_oldest_rallies_first'])
    join_oldest_rallies_first = thread.cache['join_rally_controls']['settings']['join_oldest_rallies_first']
    # Set the rally joining position based on the oldest rallies checkbox value
    scroll_through_rallies(thread,join_oldest_rallies_first,5,True)
    # Switch the swipe direction after setting up the join_oldest_rallies_first option
    swipe_direction = False if join_oldest_rallies_first else True

    swipe_iteration  = 0
    max_swipe_iteration  = 0
    # Initialize the cache to store the skipped monster cords images
    thread.cache['join_rally_controls'].setdefault('cache', {}).setdefault('skipped_monster_cords_img', [])

    while thread.thread_status():
        try:
            # Process boss monster rallies
            process_monster_rallies(thread,join_oldest_rallies_first)
            print(
                f"Swipe Direction : {swipe_direction} :: iteration : {swipe_iteration} itr cap : {max_swipe_iteration}")

            # Swipe based on the direction
            scroll_through_rallies(thread, swipe_direction)

            # Update iterations
            swipe_iteration += 1
            max_swipe_iteration += 1

            # Switch direction if limit reached
            if swipe_iteration == 5:
                swipe_direction = not swipe_direction
                swipe_iteration = 0

            # Reset navigation after reaching max iteration
            if max_swipe_iteration >= 20:
                # Clear skipped cords images
                thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img'] = []
                # Press back
                thread.adb_manager.press_back()
                time.sleep(1)
                if not navigate_join_rally_window(thread):
                    break
                # Update the swipe to scroll down
                swipe_direction = True
                max_swipe_iteration = 0
        finally:
            # Clear skipped cords images
            thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img'] = []

def process_monster_rallies(thread,scan_direction):

    rally_cords = get_valid_rallies_area_cords(thread)
    # Reorder the cords based on the scan direction
    if scan_direction:
        rally_cords.reverse()
    # print(rally_cords)
    for cords in rally_cords:
        # Recapture the  screen
        src_img = thread.capture_and_validate_screen(ads=False)
        print(f"Count: {len(rally_cords)} :: {cords}")
        x1, y1, x2, y2 = cords
        roi_src = src_img[y1:y2, x1:x2]
        # validate before joining the rally
        if not check_skipped_rallies(thread,roi_src):
            continue
        # Click on the rally
        thread.adb_manager.tap(x1, y2)
        time.sleep(1)

        # Scan rally details
        rally_info = scan_rally_info(thread,roi_src)

        if not rally_info:
            thread.adb_manager.press_back()
            time.sleep(1)
            continue

        # Proceed to join the rally
        join_alliance_war_btn_img = cv2.imread("assets/540p/join rally/join_alliance_war_btn.png")
        join_alliance_war_btn_match = template_match_coordinates(src_img, join_alliance_war_btn_img)
        if not join_alliance_war_btn_match:
            # print("Cannot find the alliance war join button")
            return False
        thread.adb_manager.tap(*join_alliance_war_btn_match)

        time.sleep(1)
        thread.adb_manager.press_back()
        time.sleep(1)
        thread.adb_manager.press_back()
        time.sleep(1)




def scan_rally_info(thread,roi_src):
    # Load template images
    boss_monster_flag_img = cv2.imread("assets/540p/join rally/boss_monster_flag.png")
    map_pinpoint_img = cv2.imread("assets/540p/join rally/map_pinpoint_tag.png")


    # Capture the current screen
    src_img = thread.capture_and_validate_screen(ads=False)

    # Make sure the rally is in progress
    if not is_template_match(src_img,boss_monster_flag_img):
        # print("Not an ongoing rally")
        return False
    # Make sure there is enough time to join the rally
    remaining_time = get_remaining_rally_time(src_img)
    if not remaining_time:
        # print("Skipping, not enough time to join/invalid time/cant read time")
        return False
    # Check whether the timer is above 5 mins
    if remaining_time > timedelta(minutes=5):
        # print("Timer is more than 5 mins")
        return False
    # Get the Timer on the join rally button TODO fix the code to extract the correct timer always
    march_time = get_march_join_time(roi_src)
    if not march_time:
        print("Invalid March time")
        return False
    print(f"Remaining Time: {remaining_time} :: March Time {march_time}")
    # Add buffer time to march time
    total_march_time = march_time + timedelta(seconds=10)
    print(f"Total march time {total_march_time}")
    # Check if march time + buffer is within remaining rally time
    if total_march_time >= remaining_time:
        print("Cant join the rally on time")
        # TODO Store the cords img to cache to avoid opening the rally again
        return False

    # Read the boss
    extracted_boss_data = read_monster_data(thread,src_img.copy())
    if not extracted_boss_data:
        return False

    # Verify if the boss is in the selected join list
    if not verify_monster_join(thread,extracted_boss_data):
        return False


    return True

def read_monster_data(thread,src_img):

    boss_text_img = crop_boss_text_area(src_img)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\boss_text_img_{get_current_datetime_string()}.png",boss_text_img)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\src_img_{get_current_datetime_string()}.png",src_img)

    # Get the text from the image
    extracted_monster_name = extract_monster_name_from_image(boss_text_img)
    print(f" Extracted Text: {extracted_monster_name}")

    # Check and skip dawn monster
    if "dawn" in extracted_monster_name:
        # print("Skipping Dawn Monsters")
        return None

    # Get the all the matching boss objects from the extracted text
    bosses = lookup_boss_by_name(extracted_monster_name)

    if not bosses:
        # print("Cannot find the boss in the db \ read wrong name")
        return None

    selected_boss_levels = thread.cache['join_rally_controls']['data']
    # print(selected_boss_levels)
    for boss,logic in bosses:
        if boss.boss_monster_id not in selected_boss_levels:
            print(f"❌ Boss {boss.boss_monster.preview_name} is not in the selected list to join.")
            return None
        # print(f"Matched Boss: {boss.name}, Level: {boss.level} Logic: {logic}")

        # Get selected level IDs for this boss
        selected_levels = selected_boss_levels[boss.boss_monster_id]
        print(f"Selected  levels {(selected_levels)}")
        # Do the logic check
        if logic == 1 or logic == 3:
            # Single level & Variant level Check
            if len(bosses) == 1:
                print(f"✅ Match Found: {boss.name} (Level {boss.level})")
                print(extract_monster_power_from_image(src_img.copy()))
                return True
            return None
        elif logic == 2:
            # Multi level Check
            # Read the monster power
            power = extract_monster_power_from_image(src_img.copy())
            print(power)
            return

        elif logic == 4:
            # Custom level
            return

    return bosses

def verify_monster_join(thread,extracted_boss_data):
    pass






def get_march_join_time(src_img):
    join_btn = cv2.imread("assets/540p/join rally/join_btn.png")
    join_btn_match = template_match_coordinates(src_img,join_btn,return_center=False)
    if not join_btn_match:
        return False
    # Get template(join_btn) dimensions
    join_btn_height, join_btn_width = join_btn.shape[:2]

    # Define new starting and ending crop coordinates
    y1_new = join_btn_match[1] + join_btn_height
    x2 = join_btn_match[0] + join_btn_width
    y2 = y1_new + join_btn_height

    # Ensure crop is within image bounds
    height_img, width_img = src_img.shape[:2]
    x2 = min(x2, width_img)
    y2 = min(y2, height_img)

    # Perform cropping
    src_img = src_img[y1_new+2:y2-6, join_btn_match[0]+10:x2-10]
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\jb_{get_current_datetime_string()}.png",src_img)
    return parse_timer_to_timedelta(extract_join_rally_time_from_image(src_img))


def get_remaining_rally_time(src_img):
    # Crop the image row wise 3 times and retain the middle portion
    src_img = crop_middle_portion(src_img,True)
    # Crop the image column wise 3 times and retain the middle portion
    src_img = crop_middle_portion(src_img,False)
    # Crop the image with a fixed height of 50 pixels to extract just the timer portion
    src_img = crop_image_fixed_height(src_img,50)

    return  parse_timer_to_timedelta(extract_remaining_rally_time_from_image(src_img))


def check_skipped_rallies(thread,src_img):
    """
    Validate before proceeding to join
    """

    # Check skipped list
    for cords_img in thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img']:
        if is_template_match(src_img, cords_img):
            # print("Already skipped one")
            return False

    return True

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

def scroll_through_rallies(thread,swipe_direction,swipe_limit=1,initial_swipe = False):
    """
    swipe_direction True = scroll down, False = scroll up
    """
    # Swipe coordinates based on direction
    swipe_cords = [250, 810, 250, 320] if swipe_direction else [250, 320, 250, 810]
    # Navigate to the alliance war window
    if not navigate_join_rally_window(thread):
        print("Cannot navigate to join rally window")
        return False
    # If the join oldest rally is not checked, then skip this.
    if initial_swipe and not swipe_direction:
        return True
    # Load the template image
    background_img = cv2.imread("assets/540p/join rally/alliance_war_window_background.png")
    for i in range(swipe_limit):
        # Check if there is any rallies to scroll through
        src_img = thread.capture_and_validate_screen(ads=False)
        if is_template_match(src_img, background_img,False, 0.95):
            # print("No more rallies in the list")
            # cv2.imwrite(r"E:\Projects\PyCharmProjects\TaskEX\temp\demo.png",draw_template_match(src_img, background_img,False, 0.95))
            break
        thread.adb_manager.swipe(*swipe_cords, 1500)
        time.sleep(1)
    return True


