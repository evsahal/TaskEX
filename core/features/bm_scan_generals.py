from utils.adb_manager import ADBManager
from utils.generals_utils import select_general_category, select_general_view, apply_general_filter
from utils.navigate_utils import navigate_generals_window


def start_scan_generals(main_window):
    # TODO :: Check & Validate all the options are selected.

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

    # Apply Filters
    apply_general_filter(device)

    # Start Scanning.
