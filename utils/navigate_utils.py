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
