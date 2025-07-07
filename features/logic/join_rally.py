import glob
import time
from datetime import timedelta
from time import sleep

import cv2
from features.utils.join_rally_helper_utils import crop_middle_portion, crop_image_fixed_height, crop_boss_text_area, \
    extract_monster_name_from_image, lookup_boss_by_name, click_join_alliance_war_btn, preset_option_skip_no_general, \
    preset_option_reset_to_one_troop, validate_and_apply_stamina, preset_option_use_selected_generals, \
    extract_monster_power_from_image, get_valid_rallies_area_cords, check_skipped_rallies, add_rally_cord_to_skip_list
from utils.get_controls_info import get_join_rally_controls
from utils.helper_utils import parse_timer_to_timedelta, get_current_datetime_string
from utils.image_recognition_utils import is_template_match, template_match_coordinates_all, \
    template_match_coordinates, detect_red_color
from utils.navigate_utils import navigate_join_rally_window
from utils.text_extraction_util import extract_remaining_rally_time_from_image, extract_join_rally_time_from_image


def run_join_rally(thread):
    # Get the controls and store it in the thread cache
    if 'join_rally_controls' not in thread.cache:
        thread.cache['join_rally_controls'] = get_join_rally_controls(thread.main_window, thread.index)
    # print(thread.cache['join_rally_controls']['settings']['join_oldest_rallies_first'])
    join_oldest_rallies_first = thread.cache['join_rally_controls']['settings']['join_oldest_rallies_first']
    # Set the rally joining position based on the oldest rallies checkbox value
    scroll_through_rallies(thread,join_oldest_rallies_first,4,True)
    # Switch the swipe direction after setting up the join_oldest_rallies_first option
    swipe_direction = False if join_oldest_rallies_first else True

    swipe_iteration  = 0
    max_swipe_iteration  = 0
    # Initialize the cache to store the skipped monster cords images
    thread.cache['join_rally_controls'].setdefault('cache', {}).setdefault('skipped_monster_cords_img', [])

    while thread.thread_status():
        try:
            # print(thread.cache['join_rally_controls']['settings']['selected_presets']['general_preset_config'])
            # Process boss monster rallies
            process_monster_rallies(thread,join_oldest_rallies_first)

            # print(f"Swipe Direction : {swipe_direction} :: iteration : {swipe_iteration} itr cap : {max_swipe_iteration}")

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
            if max_swipe_iteration >= 40:
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
        except Exception as e:
            print(e)


def process_monster_rallies(thread,scan_direction):

    rally_cords = get_valid_rallies_area_cords(thread)
    # Reorder the cords based on the scan direction
    if scan_direction:
        rally_cords.reverse()
    # print(rally_cords)
    for cords in rally_cords:
        # Recapture the  screen
        src_img = thread.capture_and_validate_screen(ads=False)
        # print(f"Count: {len(rally_cords)} :: {cords}")
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
        src_img = thread.capture_and_validate_screen(ads=False)
        # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\src_img_{get_current_datetime_string()}.png", src_img)
        # Proceed to join the rally
        join_alliance_war_btn_img = cv2.imread("assets/540p/join rally/join_alliance_war_btn.png")
        join_alliance_war_btn_match = template_match_coordinates(src_img, join_alliance_war_btn_img)

        if not join_alliance_war_btn_match:
            # print("Unable to locate the alliance war join button. Joining next rally.")
            thread.log_message(f"Unable to locate the alliance war join button. Joining next rally.", level="info")
            thread.adb_manager.press_back()
            time.sleep(1)
            return False

        # CLick the join alliance war to proceed with the rallies
        thread.adb_manager.tap(*join_alliance_war_btn_match)
        time.sleep(1)

        # Check if it opens the preset selection window
        src_img = thread.capture_and_validate_screen(ads=False)
        select_a_preset_img = cv2.imread("assets/540p/join rally/select_a_preset.png")
        if not is_template_match(src_img,select_a_preset_img):
            # print("Cant locate preset selection window")
            thread.log_message(f"Preset selection unavailable. Possibly due to busy marches.", level="info")
            thread.adb_manager.press_back()
            time.sleep(1)
            return False

        # Select the preset based on the settings
        is_preset_selection_valid = validate_preset_and_join(thread)

        if not is_preset_selection_valid:
            # print("Preset Selection/Validation Failed")
            thread.adb_manager.press_back()
            time.sleep(0.4)
            thread.adb_manager.press_back()
            time.sleep(1)
            return False

        thread.log_message("Joining...",level="info")


def scan_rally_info(thread,roi_src):
    # Load template images
    boss_monster_flag_img = cv2.imread("assets/540p/join rally/boss_monster_flag.png")

    # Capture the current screen
    src_img = thread.capture_and_validate_screen(ads=False)

    # Get the boss monster text area
    boss_text_img = crop_boss_text_area(src_img)

    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\roi_img_{get_current_datetime_string()}.png", roi_src)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\src_img_{get_current_datetime_string()}.png", src_img)

    # Make sure the rally is in progress
    if not is_template_match(src_img,boss_monster_flag_img):
        # print("Not an ongoing rally(Rally march already started)")
        thread.log_message(f"Rally has already departed; cannot join at this time.", level="info")
        return False
    # Make sure there is enough time to join the rally
    remaining_time = get_remaining_rally_time(src_img)
    if not remaining_time:
        # print("Skipping, not enough time to join/invalid time/cant read time")
        thread.log_message(f"Unable to read remaining join time; Joining next rally.", level="info")
        return False
    # Check whether the timer is above 5 mins
    if remaining_time > timedelta(minutes=5):
        # print("Timer is more than 5 mins")
        thread.log_message(f"Time exceeds 5 mins; Joining next rally.", level="info")
        # Add rally to skipped list
        add_rally_cord_to_skip_list(thread,boss_text_img)
        return False
    # Get the Timer on the join rally button
    march_time = get_march_join_time(thread,roi_src)
    if not march_time:
        # print("Invalid March time")
        thread.log_message(f"Unable to read march join time; Joining next rally.", level="info")
        add_rally_cord_to_skip_list(thread, boss_text_img)
        return False
    # print(f"Remaining Time: {remaining_time} :: March Time {march_time}")
    # Add buffer time to march time
    total_march_time = march_time + timedelta(seconds=10)
    # print(f"Total march time after adding buffer seconds {total_march_time}")
    thread.log_message(f"Total march time is {total_march_time} with 10 sec buffer time", level="info")
    # Check if march time + buffer is within remaining rally time
    if total_march_time >= remaining_time:
        # print("March exceeds join time; Unable to join.")
        thread.log_message(f"March exceeds join time; Unable to join.", level="info")
        # Add rally to skipped list
        add_rally_cord_to_skip_list(thread, boss_text_img)
        return False

    # Read the boss
    extracted_boss_data = read_monster_data(thread,src_img.copy())
    if not extracted_boss_data:
        return False

    return True

def read_monster_data(thread,src_img):

    boss_text_img = crop_boss_text_area(src_img)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\boss_text_img_{get_current_datetime_string()}.png",boss_text_img)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\src_img_{get_current_datetime_string()}.png",src_img)

    # Get the text from the image
    extracted_monster_name = extract_monster_name_from_image(boss_text_img)
    # print(f" Extracted Text: {extracted_monster_name}")
    thread.log_message(f"Extracted monster name is {extracted_monster_name}", level="debug")

    # Check and skip dawn monster
    if "dawn" in extracted_monster_name:
        # print("Skipping Shadow of Dawn Monsters")
        thread.log_message(f"Skipping Shadow of Dawn Monsters; Joining next rally.", level="info")
        # Add rally to skipped list
        add_rally_cord_to_skip_list(thread, boss_text_img)
        return None

    # Get the all the matching boss objects from the extracted text
    bosses = lookup_boss_by_name(extracted_monster_name)

    if not bosses:
        # print("Cannot find the boss in the db")
        thread.log_message(f"Cannot locate the monster in the system; Joining next rally.", level="info")
        return None

    selected_boss_levels = thread.cache['join_rally_controls']['data']
    # print(selected_boss_levels)
    extracted_power = None
    for boss,logic in bosses:
        if boss.boss_monster_id not in selected_boss_levels:
            # print(f"Boss {boss.boss_monster.preview_name} is not in the selected list to join.")
            thread.log_message(f"Boss {boss.boss_monster.preview_name} is not in the selected list to join. Joining next rally.", level="info")
            # Add rally to skipped list
            add_rally_cord_to_skip_list(thread, boss_text_img)
            return None
        # print(f"Matched Boss: {boss.name}, Level: {boss.level} Logic: {logic}")

        # Get selected level IDs for this boss
        selected_levels = selected_boss_levels[boss.boss_monster_id]
        # print(f"Selected  levels {(selected_levels)}")
        # Do the logic check
        if logic == 1 or logic == 3:# Single level & Variant level Check
            # Make sure there is only one data is found
            if len(bosses) == 1 and boss.id in selected_levels:
                # print(f"Match Found: {boss.name} (Level {boss.level})")
                thread.log_message(f"Lv{boss.level} {boss.name} is in the selected list. Attempting to join rally.", level="info")
                # print(extract_monster_power_from_image(src_img.copy()))
                return True

            thread.log_message(f"Lv{boss.level} {boss.name} is not in the selected rally list. Skipping this rally.", level="info")
            # Add rally to skipped list
            add_rally_cord_to_skip_list(thread, boss_text_img)
            return None
        elif logic == 2 or logic == 4: # Multi level & Custom Level Check
            # Read the monster power
            if not extracted_power:
                extracted_power = extract_monster_power_from_image(src_img.copy()).strip().lower()
                # print(extracted_power)
            # print(f"Category :: {boss.boss_monster.monster_category_id}")
            # Check if extracted power matches any boss in the matched list
            if boss.power.strip().lower() == extracted_power:
                # print(f"Power '{extracted_power}' matches Boss: {boss.name} (Level {boss.level})")
                # Ensure the matched level is in the selected list
                if boss.id in selected_levels:
                    # print(f"Level {boss.level} is selected. Proceeding with rally!")
                    # msg = f"{f'Lv{boss.level} ' if boss.boss_monster.monster_category_id != 3 else ''}{boss.name} is in the selected list. Attempting to join rally."
                    if boss.boss_monster.monster_category_id == 3 and boss.boss_monster.monster_logic_id == 4:  # (for viking)
                        thread.log_message(f"Lv{boss.level} {boss.boss_monster.preview_name} is in the selected list. Attempting to join rally.", level="info")
                    else:
                        thread.log_message(f"Lv{boss.level} {boss.name} is in the selected list. Attempting to join rally.", level="info")

                    return True
                # print(f"Lv{boss.level} {boss.name} is NOT in the selected list.")
                if boss.boss_monster.monster_category_id == 3 and boss.boss_monster.monster_logic_id == 4:  # (for viking)
                    thread.log_message(f"Lv{boss.level} {boss.boss_monster.preview_name} is  not in the selected rally list. Skipping this rally.", level="info")
                else:
                    thread.log_message(f"Lv{boss.level} {boss.name} is not in the selected rally list. Skipping this rally.", level="info")
                # Add rally to skipped list
                add_rally_cord_to_skip_list(thread, boss_text_img)
                return None

    return None

def validate_preset_and_join(thread):

    confirm_btn = cv2.imread("assets/540p/join rally/confirm_btn.png")

    # Get selected presets
    selected_presets = thread.cache['join_rally_controls']['settings']['selected_presets']['presets']

    preset_list = list(selected_presets.keys())  # Ordered list of selected presets

    # Get last used preset
    last_preset = thread.cache['join_rally_controls']['cache'].get('previous_preset_number')

    # If no previous preset, start from the first one
    if last_preset is None:
        current_index = 0
        is_first_iteration = True
    else:
        current_index = preset_list.index(last_preset)  # Get index of last used preset
        is_first_iteration = False

    # Loop through presets in cycle
    for _ in range(len(preset_list)):  # Ensures it check all presets once
        src_img = thread.capture_and_validate_screen()

        # Move to the next preset in order (cycling through)
        if not is_first_iteration:
            current_index = (current_index + 1) % len(preset_list)
        else:
            is_first_iteration = False
        current_preset = preset_list[current_index]
        preset_settings = selected_presets[current_preset]
        # print(f"Current preset: {current_preset}")

        # Check if the preset is present to select (loop through all 8 possible icons)
        preset_icons = glob.glob(f"assets/540p/presets/march_{current_preset}_*.png") # Get all matching preset icon files dynamically
        preset_match = None
        for icon in preset_icons:
            # print(selected_presets)
            # print(icon)
            icon_img = cv2.imread(icon)
            preset_match = template_match_coordinates(src_img, icon_img,threshold=0.9)
            if preset_match:
                thread.adb_manager.tap(*preset_match)
                time.sleep(1)
                # if the preset is not set, then skip it
                src_img = thread.capture_and_validate_screen()
                if is_template_match(src_img,confirm_btn):
                    thread.adb_manager.press_back()
                    time.sleep(1)
                    src_img = thread.capture_and_validate_screen()
                    # Remove the preset from the selected options
                    if len(thread.cache['join_rally_controls']['settings']['selected_presets']['presets']) > 1:
                        # print("Preset not set... removing it from the selected options")
                        thread.log_message(f"Preset {current_index} is not configured. It will no longer be used for rally joins.", level="info")
                        thread.cache['join_rally_controls']['settings']['selected_presets']['presets'].pop(current_preset,None)
                    else:
                        # print("Current preset is not set")
                        thread.log_message(f"Preset {current_preset} is not set.", level="info")
                    continue
                # print("Preset match found")
                thread.log_message(f"Preset {current_preset} found in selection. Proceeding with it.", level="info")
                break
        if not preset_match:
            # print(f"Preset {current_preset} is disabled. Skipping...")
            thread.log_message(f"Preset {current_preset} is locked or disabled. Skipping this preset.", level="info")
            continue  # Move to next preset

        # Use selected general if selected
        if preset_settings['use_selected_generals']:
            if not preset_option_use_selected_generals(thread):
                # print(f"Cannot Select the General from the list. ")
                thread.log_message(f"Failed to select the General from the list.", level="info")

        # Check skip no general option
        if preset_settings['skip_no_general']:
            # print(f"Skip no general :: {preset_settings['skip_no_general']}")
            if not preset_option_skip_no_general(thread):
                # print(f"Preset {current_preset}: No general found. Skipping...")
                thread.log_message(f"No general selected. Trying the next available preset.", level="info")
                continue  # Move to next preset

        # Check reset to one troop option
        if preset_settings['reset_to_one_troop']:
            # print(f"Reset to one troop :: {preset_settings['reset_to_one_troop']}")
            if not preset_option_reset_to_one_troop(thread):
                # print("Cannot reset to one troop. Trying the next available preset.")
                thread.log_message(f"Unable to reset to one troop. Trying the next available preset.", level="info")
                continue

        # If a valid preset is found, update cache and click on the march button
        thread.cache['join_rally_controls']['cache']['previous_preset_number'] = current_preset
        march_btn = cv2.imread("assets/540p/join rally/march_btn.png")
        march_btn_match = template_match_coordinates(src_img,march_btn,convert_gray=False)
        if not march_btn_match:
            return None
        thread.adb_manager.tap(*march_btn_match)
        time.sleep(1)
        # Validate and apply the stamina
        if not validate_and_apply_stamina(thread):
            return False
        return True

    # If no presets are valid
    # print("Preset validation failed... Skipping the rally.")
    thread.log_message(f"Preset check unsuccessful. Skipping the rally.", level="info")
    return None


def get_march_join_time(thread, src_img):
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

    # Check if the join time is already exceeded (red text)
    if detect_red_color(src_img):
        # print("Red color, join time exceeded the march time to join the rally")
        thread.log_message(f"Join timer turned red; not enough time left to join.", level="info")
        return False

    return parse_timer_to_timedelta(extract_join_rally_time_from_image(src_img))


def get_remaining_rally_time(src_img):
    # Crop the image row wise 3 times and retain the middle portion
    src_img = crop_middle_portion(src_img,True)
    # Crop the image column wise 3 times and retain the middle portion
    src_img = crop_middle_portion(src_img,False)
    # Crop the image with a fixed height of 50 pixels to extract just the timer portion
    src_img = crop_image_fixed_height(src_img,50)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\timer{get_current_datetime_string()}.png", src_img)
    return  parse_timer_to_timedelta(extract_remaining_rally_time_from_image(src_img))


def scroll_through_rallies(thread,swipe_direction,swipe_limit=1,initial_swipe = False):
    """
    swipe_direction True = scroll down, False = scroll up
    Dynamically swipes through rallies, changing direction when the end is reached.
    """
    # Swipe coordinates based on direction
    swipe_cords = [250, 810, 250, 320] if swipe_direction else [250, 320, 250, 810]
    # Navigate to the alliance war window
    if not navigate_join_rally_window(thread):
        # print("Cannot navigate to join rally window")
        thread.log_message(f"Unable to locate join rally window", level="info")
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
            time.sleep(1.5)
            break
        thread.adb_manager.swipe(*swipe_cords, 1500)
        time.sleep(1)
    return True


