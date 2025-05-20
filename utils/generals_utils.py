import os
from pathlib import Path

import cv2

from utils.image_recognition_utils import is_template_match, template_match_coordinates

# Get the template directory location
template_loc = os.path.join('assets', '540p', 'other')

def select_general_view(thread,view):
    view_templates={
        "details view"  : f"{template_loc}\\details_view.png",
        "list view": f"{template_loc}\\list_view.png"
    }
    # Capture a screenshot
    src_img = thread.capture_and_validate_screen(ads=False)

    #  Load the template image
    template_img = cv2.imread(view_templates[view])

    # Check if the view is already selected or not
    if is_template_match(src_img,template_img,threshold=0.9):
        thread.logger.info(f"{view.capitalize()} is already selected.")
        return True

    # Select the opposite view
    opposite_view = None
    if view == "details view":
        opposite_view = "list view"
    elif view == "list view":
        opposite_view = "details view"

    #  Load the template image again
    template_img = cv2.imread(view_templates[opposite_view])

    # Select the view
    view_match = template_match_coordinates(src_img, template_img,threshold=0.9)

    if view_match:
        thread.adb_manager.tap(view_match[0], view_match[1])
        thread.logger.info(f"Selecting {opposite_view}.")
        return True
    return False

def select_general_category(thread,category):

    # Define the templates name for each category
    category_templates = {
        "all": f"{template_loc}\\category_all",
        "military": f"{template_loc}\\category_military",
        "development": f"{template_loc}\\category_development",
        "duty": f"{template_loc}\\category_duty",
        "subordinate city": f"{template_loc}\\category_subordinate_city"
    }

    # Capture a screenshot
    src_img = thread.capture_and_validate_screen(ads=False)

    # Load the template image to verify
    template_img = cv2.imread(f"{category_templates[category]}_selected.png")

    # Check if the category is already selected or not
    if is_template_match(src_img,template_img):
        thread.logger.info(f"Category {category} is already selected.")
        return True

    # Load the template image to select
    template_img = cv2.imread(f"{category_templates[category]}.png")

    # Select the category
    category_match = template_match_coordinates(src_img,template_img)

    if category_match:
        thread.adb_manager.tap(category_match[0],category_match[1])
        thread.logger.info(f"Selecting {category.capitalize()} category.")
        return True
    return False

def apply_general_filter(thread,favorite=False, idle=False):


    # Define all the template images
    favorite_checked_img = cv2.imread(f"{template_loc}\\favorite_checked.png")
    favorite_unchecked_img = cv2.imread(f"{template_loc}\\favorite_unchecked.png")
    idle_checked_img = cv2.imread(f"{template_loc}\\idle_checked.png")
    idle_unchecked_img = cv2.imread(f"{template_loc}\\idle_unchecked.png")

    # Capture a screenshot
    src_img = thread.capture_and_validate_screen(ads=False)

    if favorite:
        # Check if favorite is checked,if not check it
        if is_template_match(src_img, favorite_checked_img):
            thread.logger.info("Favorite filter is already applied.")
            # print("Favorite already selected")
        else:
            src_img_match = template_match_coordinates(src_img, favorite_unchecked_img)
            if src_img_match:
                thread.logger.info("Applying favorite filter now.")
                # print("Selecting Favorite Filter")
                # self.invokeScanGeneralsConsole("Applying the favorite filter")
                thread.adb_manager.tap(src_img_match[0],src_img_match[1])
    else:
        # Check if favorite is unchecked,if not uncheck it
        if is_template_match(src_img, favorite_unchecked_img):
            thread.logger.info("Favorite filter is not applied already.")
                # print("Favorite already not selected")
        else:
            src_img_match = template_match_coordinates(src_img, favorite_checked_img)
            if src_img_match:
                # print("Clearing Favorite Filter")
                thread.logger.info("Clearing the favorite filter.")
                thread.adb_manager.tap(src_img_match[0],src_img_match[1])

    if idle:
        # Check if idle is checked,if not check it
        if is_template_match(src_img, idle_checked_img):
            thread.logger.info("Idle filter is already applied.")
            # print("Idle already selected")
            # self.invokeScanGeneralsConsole("Idle filter is already applied")
        else:
            src_img_match = template_match_coordinates(src_img, idle_unchecked_img)
            if src_img_match:
                thread.logger.info("Applying idle filter now.")
                # print("Selecting Idle Filter")
                # self.invokeScanGeneralsConsole("Applying the idle filter")
                thread.adb_manager.tap(src_img_match[0], src_img_match[1])
    else:
        # Check if idle is unchecked,if not uncheck it
        if is_template_match(src_img, idle_unchecked_img):
            thread.logger.info("Idle filter is not applied already.")
            # print("Idle already not selected")
        else:
            src_img_match = template_match_coordinates(src_img, idle_checked_img)
            if src_img_match:
                thread.logger.info("Clearing the idle filter.")
                # print("Clearing Idle Filter")
                thread.adb_manager.tap(src_img_match[0], src_img_match[1])

def crop_general_template_list_view(image):
    # Get the image dimensions
    height, width, _ = image.shape

    # Define the size of the template
    crop_width, crop_height = 40, 40

    # Calculate the center coordinates
    center_x = width // 2
    center_y = height // 2

    # Calculate a bit above the center (for the y-coordinate)
    center_y_above = center_y - (crop_height // 2) - 12

    # Calculate the bounding box for the crop
    left = center_x - (crop_width // 2)
    top = center_y_above
    right = left + crop_width
    bottom = top + crop_height

    # Crop the image
    cropped_img = image[top:bottom, left:right]

    return cropped_img