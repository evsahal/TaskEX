import os

import cv2
import numpy as np
from pytesseract import pytesseract

from config.settings import BASE_DIR


def setup_tesseract():
    # For Windows, you need to specify the path to the tesseract executable
    if os.name == 'nt':  # Check if the OS is Windows
        pytesseract.tesseract_cmd = rf'{BASE_DIR}\Tesseract-OCR\tesseract.exe'


def template_match_coordinates(src_image, template_image, return_center=True, convert_gray=True, threshold=0.85):
    """
    Get the coordinates of the best template match in the source image.

    :param src_image: Source image where the template will be searched.
    :param template_image: Template image to search for in the source image.
    :param return_center: Whether to return the center coordinates of the match.
    :param convert_gray: Convert both images to grayscale if True.
    :param threshold: Matching threshold (0 to 1).
    :return: (x, y) coordinates of the best match.
    """
    if convert_gray:
        src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(src_image, template_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        if return_center:
            h, w = template_image.shape[:2]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            return center_x, center_y
        return max_loc
    return None


def is_template_match(src_image, template_image, convert_gray=True, threshold=0.8):
    """
    Check if the template is found in the source image.

    :param src_image: Source image where the template will be searched.
    :param template_image: Template image to search for in the source image.
    :param convert_gray: Convert both images to grayscale if True.
    :param threshold: Matching threshold (0 to 1).
    :return: True if template match is found, otherwise False.
    """
    # Convert both images to grayscale if convert_gray is True
    if convert_gray:
        src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(src_image, template_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Return True if the maximum correlation value is greater than or equal to the threshold
    return max_val >= threshold


# Apply filtering to the image based on the specified filter type
def apply_filter(src_image, filter_type=None, **kwargs):
    if filter_type == 'gaussian':
        return apply_gaussian_blur(src_image, **kwargs)
    elif filter_type == 'median':
        return apply_median_filter(src_image, **kwargs)
    elif filter_type == 'bilateral':
        return apply_bilateral_filter(src_image, **kwargs)
    elif filter_type == 'nl_means':
        return apply_nl_means_filter(src_image, **kwargs)
    elif filter_type == 'threshold':
        return apply_threshold_filter(src_image, **kwargs)
    else:
        return src_image  # If no filter is specified, return the original image


# Apply thresholding filter
def apply_threshold_filter(src_image, threshold_value=150, max_value=255, threshold_type=cv2.THRESH_BINARY_INV):
    """
    Applies a thresholding filter to the image.

    :param src_image: Source image to which the threshold will be applied.
    :param threshold_value: Threshold value for binarization.
    :param max_value: Maximum pixel value after thresholding.
    :param threshold_type: OpenCV thresholding type (default is THRESH_BINARY_INV).
    :return: Thresholded image.
    """
    gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    _, thresh_img = cv2.threshold(gray, threshold_value, max_value, threshold_type)  # Apply threshold
    return thresh_img

# Apply Gaussian Blur to reduce noise
def apply_gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

# Apply Median Filtering to reduce salt-and-pepper noise
def apply_median_filter(image, kernel_size=5):
    return cv2.medianBlur(image, kernel_size)

# Apply Bilateral Filtering to reduce noise while preserving edges
def apply_bilateral_filter(image, d=9, sigma_color=75, sigma_space=75):
    return cv2.bilateralFilter(image, d, sigma_color, sigma_space)

# Apply Non-Local Means Denoising to reduce patterned noise
def apply_nl_means_filter(image, h=10, h_for_color=10, template_window_size=7, search_window_size=21):
    return cv2.fastNlMeansDenoisingColored(image, None, h, h_for_color, template_window_size, search_window_size)
