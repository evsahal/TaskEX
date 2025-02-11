import re

import cv2
import numpy as np
from pytesseract import pytesseract


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

def extract_time_from_image(img):
    thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)[1]
    # # Convert to HSV color space for better color isolation
    # hsv = cv2.cvtColor(thresh, cv2.COLOR_BGR2HSV)
    # cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\test.png", thresh)
    #
    # # Define the white color range in HSV
    # lower_white = np.array([0, 0, 200])
    # upper_white = np.array([180, 30, 255])
    #
    # # Create a mask for white regions
    # mask = cv2.inRange(hsv, lower_white, upper_white)
    #
    # # Apply the mask to keep only white text and black out everything else
    # isolated = cv2.bitwise_and(thresh, thresh, mask=mask)

    # Configure Tesseract for numeric detection
    custom_config = r'--oem 3 --psm 6 outputbase digits -c tessedit_char_whitelist=012345789:'
    extracted_text = pytesseract.image_to_string(thresh, config=custom_config).strip()
    print(f"Ext Text: {extracted_text}")
    cv2.imwrite(fr"E:\Projects\PyCharmProjects\TaskEX\temp\test2.png", thresh)
    # Match 00:00:00 or 00:00 format
    match = re.search(r'\b\d{2}:\d{2}:\d{2}\b', extracted_text) or re.search(r'\b\d{2}:\d{2}\b', extracted_text)

    return match.group(0) if match else None