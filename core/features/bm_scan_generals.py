from unicodedata import category

from utils.adb_manager import ADBManager
from utils.generals_utils import select_general_category, select_general_view, apply_general_filter
from utils.navigate_utils import navigate_generals_window


def start_scan_generals(main_window):
    # TODO check if the port is already in use
    # Check all the options are selected
    is_general_scan_options_valid(main_window)

    # TODO update the scan generals button text

    # Initialize adb and connect
    port = getattr(main_window.widgets, "scan_generals_port").text()
    device = ADBManager(port)
    device.connect_to_device()

    # Navigate to the generals window
    if not navigate_generals_window(device):
        # TODO :: stop the program
        pass

    # Select general view
    select_general_view(device,getattr(main_window.widgets, "scan_generals_view").currentText().lower())

    # Select category.
    select_general_category(device,getattr(main_window.widgets, "scan_generals_category").currentText().lower())

    # Get the selected filters
    filters = getattr(main_window.widgets, "scan_generals_filter")

    # Get the indices of the checked items
    checked_indices = filters.checkedIndices()
    # print(checked_indices) # [0, 1]

    # Get the corresponding item texts for the checked indices
    # checked_items = [filters.itemText(i) for i in checked_indices]

    # Print or use the selected values
    # print(f"Selected items: {checked_items}") # ['Favorite', 'Idle']

    # Apply Filters
    apply_general_filter(device,0 in checked_indices,1 in checked_indices)

    # Start Scanning.
    scan_view = getattr(main_window.widgets, "scan_generals_view")
    if scan_view.currentIndex() == 0:
        scan_generals_details_view(main_window)
    else:
        scan_generals_list_view(main_window)

def scan_generals_details_view(main_window):
    pass

def scan_generals_list_view(main_window):
    pass

def is_general_scan_options_valid(main_window):
    # Get references to the widgets
    scan_category = getattr(main_window.widgets, "scan_generals_category")  # QComboBox
    scan_view = getattr(main_window.widgets, "scan_generals_view")          # QComboBox
    scan_type = getattr(main_window.widgets, "scan_generals_type")     # QCheckComboBox
    scan_filter = getattr(main_window.widgets, "scan_generals_filter")      # QCheckComboBox
    port_input = getattr(main_window.widgets, "scan_generals_port")    # QLineEdit

    # Validate the category
    if not scan_category.currentText() or scan_category.currentIndex() == -1:
        print("Error: Please select a valid scan category.")
        return False

    # Validate the view
    if not scan_view.currentText() or scan_view.currentIndex() == -1:
        print("Error: Please select a valid scan view.")
        return False

    # Validate scan types (at least one option must be selected in the QCheckComboBox)
    if len(scan_type.checkedIndices()) == 0:
        print("Error: Please select at least one scan type.")
        return False

    # Validate filters (at least one option must be selected in the QCheckComboBox)
    if len(scan_filter.checkedIndices()) == 0:
        print("Error: Please select at least one filter option.")
        return False

    # Validate port Check if the port is not empty and contains only digits
    if not port_input.text().isdigit():
        print("Error: Port must contain only numbers and cannot be empty.")
        return False

    # All validations passed
    return True
