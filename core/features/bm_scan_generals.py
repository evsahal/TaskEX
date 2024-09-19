import os
import random
import string
from datetime import datetime
from time import sleep

import cv2
from adbutils import device
from pytesseract import pytesseract

from config.settings import BASE_DIR
from db.db_setup import get_session
from db.models import General
from db.models.general import GeneralType
from utils.generals_utils import select_general_category, select_general_view, apply_general_filter
from utils.helper_utils import crop_bottom_half
from utils.image_recognition_utils import template_match_coordinates, is_template_match, apply_filter, \
    template_match_coordinates_all
from utils.navigate_utils import navigate_generals_window
from utils.text_extraction_util import filter_general_name


def start_scan_generals(thread):
    main_window = thread.main_window
    device = thread.adb_manager
    # Check all the options are selected
    if not is_general_scan_options_valid(thread):
        return False

    # Navigate to the generals window
    if not navigate_generals_window(device):
        thread.scan_general_console.emit("Failed to navigate to generals window.")
        thread.scan_general_error.emit()
        return False

    # Select general view
    select_general_view(device,main_window.widgets.scan_generals_view.currentText().lower())

    # Select category.
    select_general_category(device,main_window.widgets.scan_generals_category.currentText().lower())

    # Get the selected filters
    filters = main_window.widgets.scan_generals_filter

    # Get the indices of the checked items
    checked_indices = filters.checkedIndices()
    # print(checked_indices) # [0, 1]

    # Get the corresponding item texts for the checked indices
    # checked_items = [filters.itemText(i) for i in checked_indices]

    # Print or use the selected values
    # print(f"Selected items: {checked_items}") # ['Favorite', 'Idle']

    # Apply Filters
    apply_general_filter(device,0 in checked_indices,1 in checked_indices)

    # Start Scanning.
    scan_view = main_window.widgets.scan_generals_view
    if scan_view.currentIndex() == 0:
        scan_generals_details_view(thread)
    else:
        scan_generals_list_view(thread)

def scan_generals_details_view(thread):
    main_window = thread.main_window
    device = thread.adb_manager
    scan_types = main_window.widgets.scan_generals_type
    # print(scan_types.checkedIndices())

    # Get the frame templates
    scan_frames = get_general_scan_frames(scan_types.checkedIndices())
    counter = 0
    previous_src_img = None
    try:
        while True:
            sleep(1)
            # Take screenshot
            src_img = device.take_screenshot()
            # cv2.imwrite(f"E:\\Projects\\PyCharmProjects\\TaskEX\\temp\\tmp\\{generate_unique_filename("src")}.png", src_img)
            # Loop through the frames
            for frame_type, frame_images in scan_frames.items():
                # Get the top match
                matches = template_match_coordinates_all(src_img,frame_images["top_left"],return_center=False,threshold=0.75)
                if matches:
                    top_frame_match = matches[0]
                else:
                    # Skip the rest when no matching frame found
                    continue
                # print("Top match found")
                frame_width, frame_height = 207, 320
                # Crop the general image with frame
                roi = src_img[top_frame_match[1]:top_frame_match[1] + frame_height,
                      top_frame_match[0]:top_frame_match[0] + frame_width].copy()

                # Checking whether the whole frame is present in the roi
                if is_template_match(roi, frame_images["bottom_right"], threshold=0.7):
                    # Crop the general name
                    general_info_img = src_img[top_frame_match[1] - 5:top_frame_match[1] + 50,
                                       top_frame_match[0] + frame_width:].copy()

                    # Preprocess the image (apply threshold)
                    processed_image = apply_filter(general_info_img, filter_type='threshold', threshold_value=180, max_value=255)
                    # Use pytesseract to extract text from the preprocessed image
                    text = filter_general_name(pytesseract.image_to_string(processed_image, config='--psm 6',lang='eng'))
                    print(f"Extracted Text: {text}")
                    # verify the general name
                    if is_general_name_exists(text):
                        thread.scan_general_console.emit(f"General '{text}' already exists")
                        break
                    new_general = General(
                        name=text,
                        details_image_name=generate_random_general_image_name(text),
                        type=GeneralType[get_general_type(frame_type)]  # Convert string to enum type
                    )

                    if save_general_to_db(new_general, roi):
                        # print(f"Adding new general widget for {new_general.name}")
                        thread.add_general_signal.emit(new_general)
                        thread.scan_general_console.emit(f"Added General '{text}'.")
                        break


            # Swipe logic for scrolling through the list
            if counter == 0:
                device.swipe(330, 680, 330, 580, 1000)
            else:
                device.swipe(330, 680, 330, 350, 3800)

            # Check the end of generals list
            if previous_src_img is not None:
                if is_template_match(crop_bottom_half(src_img), previous_src_img, threshold=0.95):
                    # print("Reached the end of generals list")
                    thread.scan_general_console.emit("Reached the end of generals list.")
                    # Stop the search
                    # After scanning is complete, stop the thread and emit the finished signal
                    thread.scan_general_finished.emit()  # Emit finished signal to indicate success
                    thread.stop()  # Stop the thread properly
                    return True
            previous_src_img = crop_bottom_half(src_img)
            counter += 1

    except Exception as e:
        # emit stop
        thread.scan_general_error.emit()
        thread.stop()  # Stop the thread
        print(e)



def scan_generals_list_view(thread):
    pass

def is_general_name_exists(general_name):
    """
    Check if the general's name already exists in the database.

    :param general_name: Name of the general to check.
    :return: True if the general exists, False otherwise.
    """
    session = get_session()
    try:
        # Query the database to check if a general with the given name exists
        exists = session.query(General).filter_by(name=general_name).first()

        # Return True if a record is found, otherwise return False
        return exists is not None
    except Exception as e:
        # print(f"Error checking general name: {e}")
        return False
    finally:
        session.close()

def generate_random_general_image_name(general_name):
    # Shuffle the characters of the general's name
    name_list = list(general_name)
    random.shuffle(name_list)
    shuffled_name = ''.join(name_list)

    # Generate random characters (letters and digits)
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Combine the shuffled name with the random characters
    random_image_name = f"{shuffled_name}_{random_chars}.png"

    # Replace spaces with underscores in the general name (if needed)
    random_image_name = random_image_name.replace(" ", "_")

    return random_image_name

def save_general_to_db(general,image):

    # Define the directory to save the image
    image_directory = f"{BASE_DIR}\\assets\\540p\\generals\\"
    # Create the directory if it doesn't exist
    os.makedirs(image_directory, exist_ok=True)

    # Add and commit the new record to the database
    session = get_session()
    try:
        session.add(general)
        session.commit()
        # print(f"General '{general.name}' saved successfully.")
        # Save the image
        cv2.imwrite(f"{image_directory}{general.details_image_name}", image)
        # print(f"{image_directory}{general.details_image_name}")
        return general
    except Exception as e:
        session.rollback()  # Rollback in case of error
        # print(f"Error saving general: {e}")
        return None
    finally:
        session.close()

def get_general_scan_frames(options):
    # Define the template location
    template_loc = os.path.join(BASE_DIR, "assets", "540p", "other")

    # Frame templates for both epic and legendary generals
    frame_templates = {
        "epic_gold_1": {
            "top_left": cv2.imread(os.path.join(template_loc, "epic_gold_frame_top_1.png")),
            "bottom_right": cv2.imread(os.path.join(template_loc, "epic_frame_bottom.png")),
        },
        "epic_red": {
            "top_left": cv2.imread(os.path.join(template_loc, "epic_red_frame_top.png")),
            "bottom_right": cv2.imread(os.path.join(template_loc, "epic_frame_bottom.png")),
        },
        "epic_gold_2": {
            "top_left": cv2.imread(os.path.join(template_loc, "epic_gold_frame_top_2.png")),
            "bottom_right": cv2.imread(os.path.join(template_loc, "epic_frame_bottom.png")),
        },
        "legendary_purple": {
            "top_left": cv2.imread(os.path.join(template_loc, "legendary_frame_top.png")),
            "bottom_right": cv2.imread(os.path.join(template_loc, "legendary_frame_bottom.png")),
        }
    }

    # Select frames based on user options
    selected_frames = {}

    # If 0 is in options, add all epic frames (including both epic gold frames and epic red frame)
    if 0 in options:
        selected_frames["epic_gold_1"] = frame_templates["epic_gold_1"]
        selected_frames["epic_gold_2"] = frame_templates["epic_gold_2"]
        selected_frames["epic_red"] = frame_templates["epic_red"]

    # If 1 is in options, add legendary frames
    if 1 in options:
        selected_frames["legendary_purple"] = frame_templates["legendary_purple"]

    return selected_frames

def get_general_type(frame_type):
    if "epic" in frame_type:
        return "epic"
    elif "legendary" in frame_type:
        return "legendary"

def is_general_scan_options_valid(thread):
    main_window = thread.main_window
    # Get references to the widgets
    scan_category = main_window.widgets.scan_generals_category  # QComboBox
    scan_view = main_window.widgets.scan_generals_view     # QComboBox
    scan_type = main_window.widgets.scan_generals_type    # QCheckComboBox
    port_input = main_window.widgets.scan_generals_port # QLineEdit

    # Validate the category
    if not scan_category.currentText() or scan_category.currentIndex() == -1:
        # print("Error: Please select a valid scan category.")
        thread.scan_general_console.emit("Please select a valid scan category.")
        thread.scan_general_error.emit()
        return False

    # Validate the view
    if not scan_view.currentText() or scan_view.currentIndex() == -1:
        # print("Error: Please select a valid scan view.")
        thread.scan_general_console.emit("Please select a valid scan view.")
        thread.scan_general_error.emit()
        return False

    # Validate scan types (at least one option must be selected in the QCheckComboBox)
    if len(scan_type.checkedIndices()) == 0:
        # print("Error: Please select at least one scan type.")
        thread.scan_general_console.emit("Please select at least one scan type.")
        thread.scan_general_error.emit()
        return False

    # Validate port Check if the port is not empty and contains only digits
    if not port_input.text().isdigit():
        # print("Error: Port must contain only numbers and cannot be empty.")
        thread.scan_general_console.emit("Port must contain only numbers and cannot be empty.")
        thread.scan_general_error.emit()
        return False

    # All validations passed
    return True
