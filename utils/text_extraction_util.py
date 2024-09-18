import re

import cv2
import numpy as np
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