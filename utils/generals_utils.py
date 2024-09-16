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
    # cv2.imwrite(r"C:\Users\evsah\OneDrive\Pictures\temp\src.png", src_img)

    # Check if the view is already selected or not
    template_img = cv2.imread(view_templates[view])
    # cv2.imwrite(r"C:\Users\evsah\OneDrive\Pictures\temp\tmp.png", template_img)

    if is_template_match(src_img,template_img,threshold=0.9):
        return True

    # Select the opposite view
    opposite_view = None
    if view == "details view":
        opposite_view = "list view"
    elif view == "list view":
        opposite_view = "details view"

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

    # Define the templates for each category (paths to the template images)
    category_templates = {
        "all": "category_all",
        "military": "category_military",
        "development": "category_development",
        "duty": "category_duty",
        "subordinate city": "category_subordinate_city"
    }

    # Capture a screenshot
    src_img = device.take_screenshot()

    # Check if the category is already selected or not
    template_img = cv2.imread(f"{template_loc}\\{category_templates[category]}_selected.png")

    if is_template_match(src_img,template_img):
        # print("Already selected")
        return True

    # Select the category
    template_img = cv2.imread(f"{template_loc}\\{category_templates[category]}.png")

    category_match = template_match_coordinates(src_img,template_img)

    if category_match:
        device.tap(category_match[0],category_match[1])
        # print(f"Selecting {category}")
        return True
    return False


def apply_general_filter(device):
    pass