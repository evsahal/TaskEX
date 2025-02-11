import os

import cv2
import numpy as np
from PySide6.QtGui import QImage
from pytesseract import pytesseract


def setup_tesseract():
    # For Windows, you need to specify the path to the tesseract executable
    if os.name == 'nt':  # Check if the OS is Windows
        pytesseract.tesseract_cmd = rf'Tesseract-OCR\tesseract.exe'


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

def template_match_coordinates_all(src_image, template_image, return_center=False, convert_gray=True, threshold=0.85):
    """
    Get the coordinates of all template matches in the source image.

    :param src_image: Source image where the template will be searched.
    :param template_image: Template image to search for in the source image.
    :param return_center: Whether to return the center coordinates of the match.
    :param convert_gray: Convert both images to grayscale if True.
    :param threshold: Matching threshold (0 to 1).
    :return: List of (x, y) coordinates of all matches above the threshold, sorted by top-to-bottom.
    """
    if convert_gray:
        src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(src_image, template_image, cv2.TM_CCOEFF_NORMED)

    # Get locations above the threshold
    loc = np.where(result >= threshold)

    matches = []
    h, w = template_image.shape[:2]

    # Iterate through all matches
    for pt in zip(*loc[::-1]):  # Switch to x, y order
        if return_center:
            center_x = pt[0] + w // 2
            center_y = pt[1] + h // 2
            matches.append((center_x, center_y))
        else:
            matches.append(pt)

    # Sort matches by the y-coordinate (top to bottom)
    matches = sorted(matches, key=lambda x: x[1])

    return matches

def template_match_multiple_sizes(src_image, template_image, scales, return_center=True, convert_gray=True, threshold=0.85):
    """
    Get the coordinates of the best template match in the source image by resizing the template to different scales.

    :param src_image: Source image where the template will be searched.
    :param template_image: Template image to search for in the source image.
    :param scales: List of scales to resize the template (e.g., [0.5, 0.75, 1.0, 1.25]).
    :param return_center: Whether to return the center coordinates of the match.
    :param convert_gray: Convert both images to grayscale if True.
    :param threshold: Matching threshold (0 to 1).
    :return: (x, y) coordinates of the best match and the best scale.
    """
    best_match = None
    best_value = 0
    best_scale = 1.0
    best_position = None

    if convert_gray:
        src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    for scale in scales:
        # Resize the template
        resized_template = cv2.resize(template_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

        # Perform template matching
        result = cv2.matchTemplate(src_image, resized_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Update the best match if the current scale has a better match
        if max_val > best_value and max_val >= threshold:
            best_value = max_val
            best_position = max_loc
            best_match = resized_template
            best_scale = scale

    if best_match is not None and best_position is not None:
        # Get dimensions of the best matching template
        h, w = best_match.shape[:2]

        # Calculate the center or top-left coordinates
        if return_center:
            center_x = best_position[0] + w // 2
            center_y = best_position[1] + h // 2
            return (center_x, center_y), best_scale
        return best_position, best_scale

    return None, None

def is_template_match(src_image, template_image, convert_gray=True, threshold=0.8):
    """
    Check for exact template matches with basic noise handling

    :param src_image: Source image (BGR format)
    :param template_image: Template image (BGR format)
    :param convert_gray: Convert to grayscale for matching
    :param threshold: Confidence threshold (0-1)
    :return: True if exact match found, False otherwise
    """
    # Basic dimension check
    if src_image.shape[0] < template_image.shape[0] or \
            src_image.shape[1] < template_image.shape[1]:
        return False

    # Convert to grayscale if requested
    if convert_gray:
        src = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    else:
        src = src_image.copy()
        template = template_image.copy()

    # Apply basic noise reduction
    src = cv2.GaussianBlur(src, (3, 3), 0)
    template = cv2.GaussianBlur(template, (3, 3), 0)

    # Template matching using normalized correlation
    result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return max_val >= threshold

def draw_template_match(src_image, template_image, convert_gray=True, threshold=0.8):
    """
    Check if the template is found in the source image and draw a rectangle around the matched area.

    :param src_image: Source image where the template will be searched.
    :param template_image: Template image to search for in the source image.
    :param convert_gray: Convert both images to grayscale if True.
    :param threshold: Matching threshold (0 to 1).
    :return: The image with a rectangle drawn around the matched area, or the original image if no match is found.
    """
    # Convert both images to grayscale if convert_gray is True
    if convert_gray:
        src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        template_image = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    # Perform template matching
    result = cv2.matchTemplate(src_image, template_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # If the match exceeds the threshold, draw a rectangle around the matched area
    if max_val >= threshold:
        # Get the width and height of the template image
        h, w = template_image.shape[:2]

        # Draw a rectangle on the source image
        cv2.rectangle(src_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
    # Return the image with the rectangle drawn (or the original image if no match)
    return src_image

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


def convert_cv_to_qimage(cv_img):
    """Convert a NumPy image to QImage."""
    height, width, channel = cv_img.shape
    bytes_per_line = channel * width
    q_image = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_BGR888)
    return q_image

def crop_image(image: np.ndarray,selection_area) -> np.ndarray:
    """Crop the image based on the selection area."""
    x, y, w, h = selection_area
    return image[y:y + h, x:x + w]