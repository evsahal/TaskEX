import time

import cv2

from utils.generals_utils import select_general_category
from utils.image_recognition_utils import template_match_coordinates_all, template_match_coordinates


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
    # General Category
    select_general_category(thread, general_preset_config['general_category'])
    # General View

    # General Filter

    # Swipe Attempts
    pass


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
