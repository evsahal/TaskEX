import os
from pathlib import Path

import cv2

from utils.image_recognition_utils import is_template_match, template_match_coordinates


def select_general_view(device,view):
    # Get the project root directory dynamically
    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    template_loc = os.path.join(PROJECT_ROOT, r'assets\540p\other')

    view_templates={
        "details view"  : f"{template_loc}\\details_view.png",
        "list view": f"{template_loc}\\list_view.png"
    }

    # Capture a screenshot
    src_img = device.take_screenshot()

    #  Load the template image
    template_img = cv2.imread(view_templates[view])

    # Check if the view is already selected or not
    if is_template_match(src_img,template_img,threshold=0.9):
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
        device.tap(view_match[0], view_match[1])
        return True
    return False


def select_general_category(device,category):

    # Get the project root directory dynamically
    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    template_loc = os.path.join(PROJECT_ROOT, r'assets\540p\other')
    # print(template_loc)

    # Define the templates name for each category
    category_templates = {
        "all": f"{template_loc}\\category_all",
        "military": f"{template_loc}\\category_military",
        "development": f"{template_loc}\\category_development",
        "duty": f"{template_loc}\\category_duty",
        "subordinate city": f"{template_loc}\\category_subordinate_city"
    }

    # Capture a screenshot
    src_img = device.take_screenshot()

    # Load the template image to verify
    template_img = cv2.imread(f"{category_templates[category]}_selected.png")

    # Check if the category is already selected or not
    if is_template_match(src_img,template_img):
        return True

    # Load the template image to select
    template_img = cv2.imread(f"{category_templates[category]}.png")

    # Select the category
    category_match = template_match_coordinates(src_img,template_img)

    if category_match:
        device.tap(category_match[0],category_match[1])

        return True
    return False


def apply_general_filter(device,favorite=False, idle=False):
    # Get the template directory location
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    template_loc = os.path.join(PROJECT_ROOT, r'assets\540p\other')

    # Define all the template images
    favorite_checked_img = cv2.imread(f"{template_loc}\\favorite_checked.png")
    favorite_unchecked_img = cv2.imread(f"{template_loc}\\favorite_unchecked.png")
    idle_checked_img = cv2.imread(f"{template_loc}\\idle_checked.png")
    idle_unchecked_img = cv2.imread(f"{template_loc}\\idle_unchecked.png")

    # Capture a screenshot
    src_img = device.take_screenshot()

    if favorite:
        # Check if favorite is checked,if not check it
        if is_template_match(src_img, favorite_checked_img):
            print("Favorite already selected")
            # self.invokeScanGeneralsConsole("Favorite filter is already applied")
        else:
            src_img_match = template_match_coordinates(src_img, favorite_unchecked_img)
            if src_img_match:
                print("Selecting Favorite Filter")
                # self.invokeScanGeneralsConsole("Applying the favorite filter")
                device.tap(src_img_match[0],src_img_match[1])
    else:
        # Check if favorite is unchecked,if not uncheck it
        if is_template_match(src_img, favorite_unchecked_img):
            print("Favorite already not selected")
            # self.invokeScanGeneralsConsole("Favorite already not selected")
        else:
            src_img_match = template_match_coordinates(src_img, favorite_checked_img)
            if src_img_match:
                print("Clearing Favorite Filter")
                # self.invokeScanGeneralsConsole("Clearing the favorite filter")
                device.tap(src_img_match[0],src_img_match[1])

    if idle:
        # Check if idle is checked,if not check it
        if is_template_match(src_img, idle_checked_img):
            print("Idle already selected")
            # self.invokeScanGeneralsConsole("Idle filter is already applied")
        else:
            src_img_match = template_match_coordinates(src_img, idle_unchecked_img)
            if src_img_match:
                print("Selecting Idle Filter")
                # self.invokeScanGeneralsConsole("Applying the idle filter")
                device.tap(src_img_match[0], src_img_match[1])
    else:
        # Check if idle is unchecked,if not uncheck it
        if is_template_match(src_img, idle_unchecked_img):
            print("Idle already not selected")
            # self.invokeScanGeneralsConsole("Idle already not selected")
        else:
            src_img_match = template_match_coordinates(src_img, idle_checked_img)
            if src_img_match:
                print("Clearing Idle Filter")
                # self.invokeScanGeneralsConsole("Clearing the idle filter")
                device.tap(src_img_match[0], src_img_match[1])