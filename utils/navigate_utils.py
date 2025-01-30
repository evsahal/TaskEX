import time

import cv2

from utils.image_recognition_utils import is_template_match, template_match_coordinates


def navigate_generals_window(thread):
    generals_btn_img = cv2.imread('assets/540p/other/generals_window_btn.png')
    menu_btn_img = cv2.imread('assets/540p/other/three_dots_menu_btn.png')

    # Make sure its inside alliance city
    if not ensure_alliance_city_or_world_map_screen(thread):
        return False
    # Take the ss
    src_img = thread.capture_and_validate_screen()

    # Check if menu button is present
    menu_btn_match = template_match_coordinates(src_img, menu_btn_img)
    if menu_btn_match:
        # Check if Generals button is already visible
        generals_btn_match = template_match_coordinates(src_img, generals_btn_img)
        if generals_btn_match:
            thread.adb_manager.tap(generals_btn_match[0], generals_btn_match[1])
            time.sleep(1)
            return True
        else:
            # Tap the 3-dots menu button to reveal options
            thread.adb_manager.tap(menu_btn_match[0], menu_btn_match[1])
            time.sleep(1)
            # Capture a new screenshot
            src_img = thread.capture_and_validate_screen()
            # Recheck for the Generals button
            generals_btn_match = template_match_coordinates(src_img, generals_btn_img)
            if generals_btn_match:
                # Tap the Generals button and return success
                thread.adb_manager.tap(generals_btn_match[0], generals_btn_match[1])
                time.sleep(1)
                return True
    # Return failure if the Generals window could not be opened
    return False

def navigate_join_rally_window(thread):
    # Check if it already opened the right window by checking for the battle logs button and verify the options selected
    inside_alliance_war = ensure_and_setup_pvp_war_window_screen(thread)
    # Else, then make sure the game screen is inside alliance city or world map
    if inside_alliance_war:
        return True
    elif not ensure_alliance_city_or_world_map_screen(thread):
        return False
    # Take the ss
    src_img = thread.capture_and_validate_screen()

    ongoing_rally_btn_img = cv2.imread('assets/540p/join rally/ongoing_rally_btn.png')
    ongoing_rally_btn_match = template_match_coordinates(src_img,ongoing_rally_btn_img)
    if ongoing_rally_btn_match:
        # Tap the ongoing rally button and return success
        thread.adb_manager.tap(ongoing_rally_btn_match[0], ongoing_rally_btn_match[1])
        time.sleep(1)
        # Now Make sure it opened the right window
        if not ensure_and_setup_pvp_war_window_screen(thread):
            return False
        return True
    # if no ongoing rally, manually navigate to the alliance war window
    alliance_btn_img = cv2.imread('assets/540p/other/alliance_btn.png')
    alliance_btn_match = template_match_coordinates(src_img, alliance_btn_img)
    if not alliance_btn_match:
        return False
    # Tap the alliance button
    thread.adb_manager.tap(alliance_btn_match[0], alliance_btn_match[1])
    time.sleep(1)
    src_img = thread.capture_and_validate_screen()
    alliance_war_window_option_img = cv2.imread('assets/540p/join rally/alliance_war_window_option.png')
    alliance_war_window_option_match = template_match_coordinates(src_img, alliance_war_window_option_img)
    if not alliance_war_window_option_match:
        return False
    # Tap the alliance war window icon
    thread.adb_manager.tap(alliance_war_window_option_match[0], alliance_war_window_option_match[1])
    time.sleep(1)
    # src_img = thread.capture_and_validate_screen()
    if ensure_and_setup_pvp_war_window_screen(thread):
        return True
    else:
        return False

def ensure_and_setup_pvp_war_window_screen(thread):
    alliance_war_window_tag_img = cv2.imread('assets/540p/join rally/alliance_war_window_tag.png')
    battle_logs_btn_img = cv2.imread('assets/540p/join rally/battle_logs_btn.png')
    pvp_war_tab_img = cv2.imread('assets/540p/join rally/pvp_war_tab.png')
    src_img = thread.capture_and_validate_screen()
    # Make sure it opened the right window, return false it not
    if not is_template_match(src_img, alliance_war_window_tag_img):
        return False
    # Make sure battle logs button is present
    if not is_template_match(src_img, battle_logs_btn_img):
        pvp_war_tab_match = template_match_coordinates(src_img,pvp_war_tab_img)
        if pvp_war_tab_match:
            # print("Moving to pvp war window")
            thread.adb_manager.tap(pvp_war_tab_match[0], pvp_war_tab_match[1])
            time.sleep(1)
            src_img = thread.capture_and_validate_screen()

    # Check again if the battle logs button is present, if not then return false
    if not is_template_match(src_img, battle_logs_btn_img):
        # print("Cannot find the battle logs btn")
        return False
    # Now verify only Monster War option is selected
    war_checked_img = cv2.imread('assets/540p/join rally/war_checked.png')
    war_unchecked_img = cv2.imread('assets/540p/join rally/war_unchecked.png')

    # Crop the monster war and war option checkbox image area
    src_img_height,src_img_width,_ = src_img.shape

    # Calculate the height and width of src_image to crop
    piece_height = src_img_height // 5
    piece_width = src_img_width // 3

    # Extract the top piece (cropping the src image 5 times horizontally and take the top piece)
    top_piece = src_img[:piece_height, :, :]

    # Extract the first 2 pieces from the top_piece(cropping the top_piece 3 times vertically)
    monster_war_checkbox_src_img = top_piece[:, :piece_width, :]
    war_checkbox_src_img = top_piece[:, piece_width:2 * piece_width, :]

    # Check if monster war checkbox is checked or not, then check it if needed
    if is_template_match(monster_war_checkbox_src_img,war_unchecked_img):
        # print("Monster war option is not checked")
        # Check the monster war checkbox
        monster_war_checkbox_match = template_match_coordinates(monster_war_checkbox_src_img,war_unchecked_img)
        if monster_war_checkbox_match:
            # print(f"Checking monster war option {monster_war_checkbox_match[0]} {monster_war_checkbox_match[1]}")
            thread.adb_manager.tap(monster_war_checkbox_match[0], monster_war_checkbox_match[1])

    # Uncheck the war checkbox
    if is_template_match(war_checkbox_src_img, war_checked_img):
        # print("War option is checked")
        war_checkbox_match = template_match_coordinates(war_checkbox_src_img,war_checked_img)
        if war_checkbox_match:
            # print("Unchecking the war checkbox")
            thread.adb_manager.tap(war_checkbox_match[0]+piece_width, war_checkbox_match[1])
    return True


def ensure_alliance_city_or_world_map_screen(thread, ac=True, wm=True):
    """
    Ensures the screen is either Alliance City or World Map based on the parameters.

    Parameters:
        thread: The bot thread instance.
        ac (bool): If True, ensure the screen is in Alliance City.
        wm (bool): If True, ensure the screen is in World Map.

    Returns:
        bool: True if the desired screen is ensured, False otherwise.
    """
    # Load templates
    ac_btn_img = cv2.imread(
        'assets/540p/other/explore_alliance_city_btn.png')  # Common for both World Map and Ideal Land
    wm_btn_img = cv2.imread(
        'assets/540p/other/explore_world_map_btn.png')
    alliance_btn_img = cv2.imread('assets/540p/other/alliance_btn.png')  # World Map validation

    counter = 0
    max_attempts = 15  # Prevent infinite loops

    while counter < max_attempts:
        src_img = thread.capture_and_validate_screen()

        # Check Alliance City
        if ac:
            if is_template_match(src_img, wm_btn_img):  # Alliance City detected
                return True
            if not wm:  # Only Alliance City is required
                thread.adb_manager.press_back()
                time.sleep(1)
                counter += 1
                continue

        # Check World Map
        if wm:
            ac_btn_match = template_match_coordinates(src_img, ac_btn_img)  # Check for World Map/Ideal Land
            wm_alliance_match = is_template_match(src_img, alliance_btn_img)

            if ac_btn_match and wm_alliance_match:  # World Map detected
                return True
            elif ac_btn_match and not wm_alliance_match:  # Ideal Land case
                thread.adb_manager.tap(ac_btn_match[0], ac_btn_match[1])  # Navigate to Alliance City
                time.sleep(4)
                continue

        # If neither is detected, press back
        thread.adb_manager.press_back()
        time.sleep(1)
        counter += 1

    # Failed to ensure desired screen
    return False
