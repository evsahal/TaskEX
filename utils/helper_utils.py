import ctypes
import os
import re
import shutil
from datetime import timedelta, datetime


def extract_number_from_string(string: str) -> int:
    """
    Extracts all integers from the given string, combines them, and returns
    the result as a single integer.

    Args:
        string (str): The input string containing numbers and other characters.

    Returns:
        int: A single integer formed by combining all the numbers found in the string.
        Returns 0 if no numbers are found.
    """
    matches = re.findall(r'\d+', string)
    if matches:
        # Combine all the number matches as strings and convert to an integer
        combined_number = int(''.join(matches))
        return combined_number
    else:
        return 0  # Return 0 if no numbers are found

def crop_bottom_half(image):
    # Get the size of the image
    width, height = image.shape[:-1]
    # Define the points for cropping
    start_row, start_col = int(height * .5), int(0)
    end_row, end_col = int(height), int(width)
    # Crop the image
    cropped_img = image[start_row:end_row, start_col:end_col].copy()
    return cropped_img


def copy_image_to_preview(file,file_name):
    if os.path.exists(file):
        # Get the preview folder path
        preview_path = os.path.join( 'assets', 'preview')

        # Define the new destination path for the file
        destination_path = os.path.join(preview_path, file_name)
        try:
            # Copy the file to the new destination
            shutil.copy(file, destination_path)
        except Exception as e:
            print(f"Error copying file: {e}")

def copy_image_to_template(file, file_name):
    if os.path.exists(file):
        # Get the template folder path
        template_path = os.path.join( 'assets', '540p', 'monsters')

        # Define the new destination path for the file
        destination_path = os.path.join(template_path, file_name)
        try:
            # Copy the file to the new destination
            shutil.copy(file, destination_path)
        except Exception as e:
            print(f"Error copying file: {e}")

def get_screen_resolution():
    """Fetch the real screen resolution."""
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return f"{screen_width}x{screen_height}"

def is_valid_timer_format(text):
    # Check if text matches a timer format (e.g., HH:MM:SS or H:MM:SS)
    if not text or len(text.split(':')) != 3:
        return False
    hours, minutes, seconds = text.split(':')
    return (hours.isdigit() and 0 <= int(hours) <= 23 and
            minutes.isdigit() and 0 <= int(minutes) <= 59 and
            seconds.isdigit() and 0 <= int(seconds) <= 59)

def parse_timer_to_timedelta(timer_text):
    """
    Convert timer text in the format 'HH:MM:SS' or 'MM:SS' to a timedelta object.
    Handles different cases like None, empty strings, or incorrect formats.
    """
    if not timer_text or not isinstance(timer_text, str):
        return None  # Return None if input is None or not a string

    parts = timer_text.split(":")

    try:
        # Handle different formats
        if len(parts) == 3:  # 'HH:MM:SS' format
            hours, minutes, seconds = map(int, parts)
        elif len(parts) == 2:  # 'MM:SS' format
            hours = 0
            minutes, seconds = map(int, parts)
        else:
            return None  # Return None for invalid format

        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    except ValueError:
        return None  # Return None if conversion to int fails

def get_current_datetime_string():
    """
    Returns the current datetime as a formatted string.
    """
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
