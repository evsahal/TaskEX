import os
import re
import shutil

from PySide6.QtWidgets import QFileDialog

from config.settings import BASE_DIR


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

def image_chooser(button,line_edit):
    """Opens a file dialog to select an image file and updates the line edit with the selected file name."""
    # Set the file dialog options
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Set the dialog to read-only

    # Open the file dialog to select an image file
    file_name, _ = QFileDialog.getOpenFileName(
        button,
        "Select Image File",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
        options=options
    )

    if file_name:
        # Update the line edit with just the file name
        line_edit.setText(os.path.basename(file_name))

        # Create the file_path property
        line_edit.setProperty("file_path", file_name)

        # print(f"File path set: {line_edit.property('file_path')}")  # Debugging line

def copy_image_to_preview(file,file_name):
    if os.path.exists(file):
        # Get the preview folder path
        preview_path = os.path.join(BASE_DIR, 'assets', 'preview')

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
        template_path = os.path.join(BASE_DIR, 'assets', '540p', 'monsters')

        # Define the new destination path for the file
        destination_path = os.path.join(template_path, file_name)
        try:
            # Copy the file to the new destination
            shutil.copy(file, destination_path)
        except Exception as e:
            print(f"Error copying file: {e}")

