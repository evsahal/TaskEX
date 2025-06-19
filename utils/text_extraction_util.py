import re

import cv2
import numpy as np
from pytesseract import pytesseract

from utils.helper_utils import get_current_datetime_string, is_valid_timer_format


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
    # print(f"Remaining march time::before {extracted_text}")

    # Match 00:00:00 or 00:00 format
    match = re.search(r'\b\d{2}:\d{2}:\d{2}\b', extracted_text) or re.search(r'\b\d{2}:\d{2}\b', extracted_text)

    # print(f"Remaining march time::after {match.group(0) if match else None}")
    return match.group(0) if match else None


def extract_join_rally_time_from_image(img):
    # Method 1: Grayscale with contrast enhancement and Otsu thresholding
    gray_full = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Enhance contrast
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0     # Brightness control
    contrasted = cv2.convertScaleAbs(gray_full, alpha=alpha, beta=beta)
    _, binary = cv2.threshold(contrasted, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    extracted_text = pytesseract.image_to_string(binary, config="--psm 7 --oem 3").strip()
    if is_valid_timer_format(extracted_text):
        # print(f"Timer extracted (Method 1): {extracted_text}")
        return extracted_text
    else:
        # print(f"Method 1 failed: Invalid timer format - {extracted_text}")
        pass

    # Method 2: Edge detection and morphological enhancement
    edges = cv2.Canny(gray_full, 50, 150)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    extracted_text2 = pytesseract.image_to_string(dilated, config="--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789:").strip()
    if is_valid_timer_format(extracted_text2):
        # print(f"Timer extracted (Method 2): {extracted_text2}")
        return extracted_text2
    else:
        # print(f"Method 2 failed: Invalid timer format - {extracted_text2}")
        pass

    # print("No valid timer format detected with any method.")
    return None

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
    # print(f"Ext Text march time: {extracted_text}")

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
    # print(f"March time {match.group(0) if match else None}")

    return match.group(0) if match else None