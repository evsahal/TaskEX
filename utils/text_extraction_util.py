import re

import cv2
import numpy as np
from pytesseract import pytesseract

from utils.helper_utils import get_current_datetime_string


def filter_general_name(text):
    # Replace newlines with spaces
    text = text.replace("\n", " ")

    # Handle common OCR misinterpretations of "Lv"
    # Remove patterns that look like "Lv" followed by numbers or common misreadings
    text = re.sub(r"^[a-zA-Z]{2}[\d]+", "", text, flags=re.IGNORECASE)

    # Remove special characters except dash (-) and parentheses ()
    text = re.sub(r"[^\w\s\(\)-]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Strip whitespace from both ends of the string
    text = text.strip()

    return text

def extract_remaining_rally_time_from_image(img):
    thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)[1]
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\rt_og_{get_current_datetime_string()}.png", img)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\rt_thresh{get_current_datetime_string()}.png", thresh)
    # Configure Tesseract for numeric detection
    custom_config = r'--oem 3 --psm 6 outputbase digits -c tessedit_char_whitelist=0123456789:'
    extracted_text = pytesseract.image_to_string(thresh, config=custom_config).strip()
    print(f"Remaining march time::before {extracted_text}")

    # Match 00:00:00 or 00:00 format
    match = re.search(r'\b\d{2}:\d{2}:\d{2}\b', extracted_text) or re.search(r'\b\d{2}:\d{2}\b', extracted_text)

    print(f"Remaining march time::after {match.group(0) if match else None}")
    return match.group(0) if match else None

def extract_join_rally_time_from_image(img):
    # TODO work on this
    return "00:00:01"

def extract_monster_power_from_image(img):
    monster_power_icon_img = cv2.imread("assets/540p/join rally/monster_power_icon.png")

    # Get image dimensions
    height, width = img.shape[:2]

    # Crop the top-right quadrant
    x_start = width // 2  # Start from the middle horizontally
    y_start = 0  # Start from the top
    x_end = width  # End at full width
    y_end = height // 2  # End at the middle vertically
    top_right_img = img[y_start:y_end, x_start:x_end]  # Crop top-right quadrant

    # Convert top-right image to grayscale for template matching
    src_gray = cv2.cvtColor(top_right_img, cv2.COLOR_BGR2GRAY)
    icon_gray = cv2.cvtColor(monster_power_icon_img, cv2.COLOR_BGR2GRAY)

    # Perform template matching to find the power icon
    result = cv2.matchTemplate(src_gray, icon_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8  # Match confidence threshold
    if max_val < threshold:
        print("⚠️ Power icon not found in the image.")
        return None

    # Crop the power text based on the icon's position
    match_x, match_y = max_loc  # Top-left coordinates of the match
    icon_h, icon_w = icon_gray.shape[:2]

    x1 = match_x + icon_w  # Start just after the icon
    y1 = match_y  # Align with the icon
    x2 = x1 + 150  # Approximate width for power text
    y2 = y1 + icon_h  # Keep same height as icon

    cropped_power_text = top_right_img[y1:y2, x1:x2]  # Crop the power text area

    # Refine the cropped image (trim extra right-side parts)
    hsv = cv2.cvtColor(cropped_power_text, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cols = np.any(mask, axis=0)  # Find blue background columns
    if np.any(cols):
        x2 = np.max(np.where(cols))  # Get rightmost blue pixel
    else:
        x2 = cropped_power_text.shape[1]  # Default to full width if no blue detected

    refined_cropped_power_text = cropped_power_text[:, :x2]  # Crop up to the detected blue area

    cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\crop_{get_current_datetime_string()}.png", refined_cropped_power_text)

    # Extract text using OCR
    gray = cv2.cvtColor(refined_cropped_power_text, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    extracted_text = pytesseract.image_to_string(binary, config="--psm 7").strip()

    return extracted_text

def preprocess_white_text(img):
    """
    Extracts white text from an image using thresholding.
    """
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    white_text_mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY_INV)[1]
    return white_text_mask


def extract_timer_white_text(img):
    """
    Extracts the timer text from an image, ensuring only valid formats are returned.
    """
    processed_mask = preprocess_white_text(img)

    # OCR Configuration for numeric detection
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789:'
    extracted_text = pytesseract.image_to_string(processed_mask, config=custom_config).strip()

    # Clean unwanted characters and ensure valid format
    extracted_text = ''.join(filter(lambda x: x in '0123456789:', extracted_text))
    print(f"Ext Text march time: {extracted_text}")

    # If the extracted text is purely numeric, insert a colon (MM:SS format or H:MM:SS if needed)
    if extracted_text.isdigit():
        extracted_text = extracted_text.lstrip("0") or "0"  # Remove leading zeros but keep at least one digit
        if len(extracted_text) == 3:
            extracted_text = f"0{extracted_text[0]}:{extracted_text[1:]}"
        elif len(extracted_text) == 4:
            extracted_text = f"{extracted_text[:2]}:{extracted_text[2:]}"
        elif len(extracted_text) == 5:
            extracted_text = f"{extracted_text[0]}:{extracted_text[1:3]}:{extracted_text[3:]}"

    match = re.search(r'\b(?:\d{1,2}:)?\d{2}:\d{2}\b', extracted_text)
    print(f"March time {match.group(0) if match else None}")

    return match.group(0) if match else None