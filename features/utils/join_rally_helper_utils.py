import re

import cv2
import numpy as np
from pytesseract import pytesseract
from sqlalchemy import func

from db.db_setup import get_session
from db.models import MonsterLevel


def crop_middle_portion(image, mode):
    """
    Crop the image into three parts (row-wise or column-wise) and store the middle portion.
    :return: The middle portion of the cropped image.
    """
    # Get image dimensions
    height, width, _ = image.shape

    if mode:  # Row-wise cropping
        third_height = height // 3
        middle_crop_top = third_height
        middle_crop_bottom = third_height * 2
        # Crop the middle portion (second third row-wise)
        return image[middle_crop_top:middle_crop_bottom, :]

    else:  # Column-wise cropping
        third_width = width // 3
        middle_crop_left = third_width
        middle_crop_right = third_width * 2
        # Crop the middle portion (second third column-wise)
        return image[:, middle_crop_left:middle_crop_right]


def crop_image_fixed_height(image, height):
    """
    Crop the image starting from the top-left corner (0, 0) with a fixed height (custom height).

    :param image: The image to crop.
    :param height: The height to crop.
    :return: The cropped image.
    """
    # Get image dimensions
    height_img, width_img, _ = image.shape

    # Starting point (0, 0) is fixed
    x1, y1 = 0, 0

    # Define x2 as the width of the image
    x2 = width_img

    # Define y2 as y1 + height (fixed vertical crop distance)
    y2 = min(y1 + height, height_img)  # Ensure y2 does not exceed the image height

    # Crop the image using the defined coordinates
    cropped_img = image[y1:y2, x1:x2]

    return cropped_img


def crop_boss_text_area(src_img):
    """Dynamically crop the marked green rectangle area based on proportional values."""

    # Get image dimensions
    height, width = src_img.shape[:2]

    # Define cropping ratios (based on analysis of the 540p image)
    left_ratio = 0.55  # Start column (percentage of width)
    right_ratio = 0.95  # End column (percentage of width)
    top_ratio = 0.22  # Start row (percentage of height)
    bottom_ratio = 0.37  # End row (percentage of height)

    # Convert ratios to pixel values
    left = int(width * left_ratio) + 25
    right = int(width * right_ratio) + 13
    top = int(height * top_ratio)
    bottom = int(height * bottom_ratio) - 75

    # Ensure cropping remains within valid bounds
    left = min(left, width - 1)
    right = min(right, width)
    top = min(top, height - 1)
    bottom = min(bottom, height)

    # Crop the region of interest (ROI)
    cropped_img = src_img[top:bottom, left:right]

    return cropped_img


def extract_monster_name_from_image(src_img):
    # Yellow text to black and rest to white
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for the yellow color
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Create a mask for the yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Replace the yellow color with black
    result = cv2.bitwise_and(src_img, src_img, mask=mask)
    result[mask > 0] = (0, 0, 0)

    # Replace the remaining pixels with white
    result[mask == 0] = (255, 255, 255)

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # gray = cv2.medianBlur(gray, 3)
    # new code(uncomment medianBlur and comment the following if there is an issue)
    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adjust the contrast of the image
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(blurred, alpha=alpha, beta=beta)

    # Apply adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(adjusted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    # Apply dilation and erosion to enhance text
    kernel = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(adaptive_thresh, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)

    kernel_sharpen = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
    sharpened = cv2.filter2D(erosion, -1, kernel_sharpen)

    # Apply adaptive thresholding to make text stand out
    processed = cv2.adaptiveThreshold(sharpened, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)


    # cv2.imwrite(r"C:\Users\evsah\Jupyter\assets\output\boss_name.png",processed)
    # OCR Configuration (allow letters & numbers, but not special characters except .)
    custom_config = '--oem 3 --psm 6 -c tessedit_char_whitelist=a-zA-Z0-9.'
    monster_info_text = pytesseract.image_to_string(processed, config=custom_config).replace(" ", "").replace("\n",
                                                                                                                  "").lower()
    pattern = re.compile(r'[^a-zA-Z0-9\s]+') # TODO fix regex coding
    monster_info_text = re.sub(pattern, '', monster_info_text)
    return monster_info_text

def lookup_boss_by_name(extracted_text):
    session = get_session()
    # Apply normalization to the database values at query time
    bosses = session.query(MonsterLevel).filter(
        func.lower(
            func.regexp_replace(
                MonsterLevel.name, r'[^a-zA-Z0-9]', '', 'g'  # Remove special chars & spaces
            )
        ).like(f"%{extracted_text}%")
    ).all()

    if not bosses:
        return None

    return bosses



