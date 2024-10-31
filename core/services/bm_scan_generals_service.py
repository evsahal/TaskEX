import os
import random
import string
from datetime import datetime
from time import sleep

import cv2
import numpy as np
import unicodedata
from adbutils import device
from pytesseract import pytesseract

from config.settings import BASE_DIR
from db.db_setup import get_session
from db.models import General
from db.models.general import GeneralType
from utils.generals_utils import select_general_category, select_general_view, apply_general_filter, \
    crop_general_template_list_view
from utils.helper_utils import crop_bottom_half
from utils.image_recognition_utils import template_match_coordinates, is_template_match, apply_filter, \
    template_match_coordinates_all, template_match_multiple_sizes
from utils.navigate_utils import navigate_generals_window
from utils.text_extraction_util import filter_general_name


def start_scan_generals(thread):
    main_window = thread.main_window
    device = thread.adb_manager
    # Check all the options are selected
    if not is_general_scan_options_valid(thread):
        return False

    # Check if scan view is list view and some generals are already present in the DB
    pending_generals = None
    if main_window.widgets.scan_generals_view.currentText() == "List View":
        session = get_session()
        # Get checked types for generals to search
        scan_types = main_window.widgets.scan_generals_type.checkedIndices()

        # Convert them to pass the types to the query
        general_type_filter = []
        if 0 in scan_types:
            general_type_filter.append(GeneralType.epic)
        if 1 in scan_types:
            general_type_filter.append(GeneralType.legendary)
        # If both 0 (Epic) and 1 (Legendary) are selected, return both types
        if len(general_type_filter) == 2:
            # No filter, returns both
            pending_generals = General.find_pending_list_view_generals(session)
        elif len(general_type_filter) == 1:
            # Filter by selected type
            pending_generals = General.find_pending_list_view_generals(session, general_type_filter[0])
        session.close()
        if not pending_generals:
            # Console message and exit the scan
            thread.scan_general_console.emit("No generals pending for list view scan.")
            thread.scan_general_error.emit()
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
        scan_generals_list_view(thread,pending_generals)

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
                matches = template_match_coordinates_all(src_img,frame_images["top_left"],threshold=0.75)
                if matches:
                    top_frame_match = matches[0]
                else:
                    # Skip the rest when no matching frame found
                    continue
                # print("Top match found")
                # Here instead of static measurement, find the both template loc and crop the image
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
                    # print(f"Extracted Text: {text}")
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
        # emit scan stop
        thread.scan_general_error.emit()
        thread.stop()  # Stop the thread
        print(e)



def scan_generals_list_view(thread,pending_generals):
    main_window = thread.main_window
    device = thread.adb_manager

    # Define the directory to save the image
    image_directory = f"{BASE_DIR}\\assets\\540p\\generals\\"

    # Get all the frame templates to scan
    selected_frames = get_general_scan_frames([0, 1])

    # Set up the scale array to resize the template image for matching
    scales = np.arange(0.65, 1, 0.01)
    previous_src_img = None
    session = get_session()
    try:
        while True:
            sleep(1)
            # Take screenshot
            src_img = device.take_screenshot()

            # Get all the generals with frames
            cropped_generals = extract_general_with_frames(src_img,selected_frames)

            # loop through the cropped images to find the match
            for crop_img in cropped_generals:
                # cv2.imwrite(f"E:\\Projects\\PyCharmProjects\\TaskEX\\temp\\{i}.png",crop_img)
                # Match the cropped images with the pending_generals images
                for general in pending_generals:
                    # print(general)
                    # <General(name=Elektra, type=Epic Historic General, resolution=540p, details_image=tElkare_ECa50.png,list_image=None)>
                    # Crop the detail view general template image to match
                    template_image = crop_general_template_list_view(cv2.imread(f"{image_directory}{general.details_image_name}"))
                    # Match the template in the src_img
                    match_cords, best_scale = template_match_multiple_sizes(crop_img, template_image, scales)
                    if not match_cords:
                        continue
                    # print(match_cords, best_scale)
                    # When a match found, update the data to db and save the image
                    general.scale = best_scale
                    general.list_image_name = general.details_image_name.replace(".png", "_lv.png")
                    # print(f"BEFORE: {general}")
                    # Save the changes to the database
                    session.add(general)
                    # Save the image to the path
                    cv2.imwrite(f"{image_directory}{general.list_image_name}",crop_img)
                    session.commit()
                    thread.scan_general_console.emit(f"Updated list view template for {general.name}.")

                    # Update the list view ui,
                    # print(getattr(main_window.widgets, "toggle_general_view").isChecked())
                    toggle = getattr(main_window.widgets, "toggle_general_view").isChecked()
                    getattr(main_window.widgets, f"general_profile_{general.id}").update_data.emit(general)
                    getattr(main_window.widgets, f"general_profile_{general.id}").update_view.emit(general.id,toggle)

                    # Remove that general from the loop list
                    pending_generals.remove(general)

            # if pending generals are empty
            if len(pending_generals) == 0:
                # After scanning is complete, stop the thread and emit the finished signal
                thread.scan_general_finished.emit()  # Emit finished signal to indicate success
                thread.stop()  # Stop the thread properly
                return True

            # Swipe for scrolling through the list
            device.swipe(330, 780, 330, 350, 3800)

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
            # break  # temp break to exit the program after taking one ss

    except Exception as e:
        print(e)
        # emit scan stop
        thread.scan_general_error.emit()
        # Stop the thread
        thread.stop()

    finally:
        session.close()

def extract_general_with_frames(src_img,selected_frames):
    # variable to store all the cropped images
    cropped_images = []
    # Custom Height and Width to crop the general image
    custom_height = 236
    custom_width = 159
    # Loop through all the frames to get all match coordinates
    for _, top_frame_image in selected_frames.items():
        # Get all the top frame match for the current looping frame
        match_cords = template_match_coordinates_all(src_img, top_frame_image['top_left'], threshold=0.65)
        # Loop through the matched cords
        for coord in match_cords:
            # Unpack the top-left coordinates
            top_left_x, top_left_y = coord
            # Calculate the bottom-right corner of the rectangle using custom dimensions
            bottom_right_x = top_left_x + custom_width
            bottom_right_y = top_left_y + custom_height
            # Crop the image...
            cropped_image = src_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x].copy()
            # Check if it's the whole image or just a portion
            if not cropped_image.shape[0] == custom_height:
                # Remove the matched area to avoid rematch
                src_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = 0 # Black
                continue
            # Check for the bottom frames(loop again to check with all types of bottom frames)
            for _, bottom_frame_image in selected_frames.items():
                if is_template_match(cropped_image, bottom_frame_image["bottom_right"], threshold=0.6):
                    cropped_images.append(cropped_image)
                    # Remove the matched area to avoid rematch
                    src_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = 0  # Black
                    break
    return cropped_images

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
    # Normalize the general's name (NFKD form separates accents from letters)
    normalized_name = unicodedata.normalize('NFKD', general_name).encode('ASCII', 'ignore').decode('ASCII')

    # Shuffle the characters of the normalized name
    name_list = list(normalized_name)
    random.shuffle(name_list)
    shuffled_name = ''.join(name_list)

    # Generate random characters (letters and digits)
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Combine the shuffled name with the random characters
    random_image_name = f"{shuffled_name}_{random_chars}.png"

    # Replace spaces with underscores
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
