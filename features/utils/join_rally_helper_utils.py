import re

import cv2
import numpy as np
from pytesseract import pytesseract


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




