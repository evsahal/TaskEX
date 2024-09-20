from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QLineEdit
from sqlalchemy import Boolean

from core.emulator_thread import EmulatorThread
from typing import Optional

from gui.controllers.bm_scan_generals_controller import add_general_to_frame, update_scan_console


def handle_run_button(main_window: 'MainWindow', index: int) -> None:
    """
    Handle the Run button click event for an instance.
    Start or stop the emulator instance and update the button icons.
    """
    emulator_thread: Optional[EmulatorThread] = getattr(main_window.widgets, f'emulator_thread_{index}', None)

    if emulator_thread and emulator_thread.isRunning():
        stop_emulator_instance(main_window, index)
    else:
        start_emulator_instance(main_window, index)


def start_emulator_instance(main_window: 'MainWindow', index: int) -> None:
    """
    Start the emulator instance thread for the given index.
    """
    # Get port number
    port: str = getattr(main_window.widgets, f"im_emu_port_{index}").text()
    emulator_thread: EmulatorThread = EmulatorThread(main_window, port, index, "emu")

    # Store the thread in the main_window for reference
    setattr(main_window.widgets, f'emulator_thread_{index}', emulator_thread)

    # Initialize a list to track running instance indices if not already initialized
    if not hasattr(main_window.widgets, 'running_instance_indices'):
        main_window.widgets.running_instance_indices = set()  # Use a set for fast membership checks

    # Add the index to the list of running instances
    main_window.widgets.running_instance_indices.add(index)

    # Connect signals for thread finished and error handling
    emulator_thread.finished.connect(lambda idx: on_emulator_finished(main_window, idx))
    emulator_thread.error.connect(lambda idx, error: on_emulator_error(main_window, idx, error))

    # Start the emulator thread
    emulator_thread.start()

    # Update button icons to "Stop" in both instance manager and run tab
    update_run_button_icon(main_window, index, running=True)


def stop_emulator_instance(main_window: 'MainWindow', index: int) -> None:
    """
    Stop the emulator instance thread for the given index.
    If index is 999, update the scan generals button instead of the run button.
    """
    emulator_thread: Optional[EmulatorThread] = getattr(main_window.widgets, f'emulator_thread_{index}', None)
    if emulator_thread:
        emulator_thread.stop()

    # Remove the index from the list of running instances
    if hasattr(main_window.widgets, 'running_instance_indices'):
        # Safely remove the index if it exists
        main_window.widgets.running_instance_indices.discard(index)

    # Update button icons to "Run" in both instance manager and run tab for normal instances
    update_run_button_icon(main_window, index, running=False)


def handle_scan_general_button(main_window: 'MainWindow') -> None:
    """
    Handle the Scan General button click event.
    Start or stop the scan general operation and update the button text.
    """
    index = 999  # Set index for scan general
    emulator_thread: Optional[EmulatorThread] = getattr(main_window.widgets, f'emulator_thread_{index}', None)

    if emulator_thread and emulator_thread.isRunning():
        # If already running, stop it
        stop_general_scan_instance(main_window)
        emulator_thread.scan_general_finished.emit()
    else:
        # Start a new emulator thread for scanning generals
        if start_general_scan_instance(main_window):
            main_window.widgets.scan_generals_btn.setText("Stop Scanning")


def start_general_scan_instance(main_window: 'MainWindow') -> bool:
    """
    Start the scan general thread for the given index.
    """
    index = 999
    # Get port number
    port: str = main_window.widgets.scan_generals_port.text()

    # Check if the port is already in use
    if check_port_already_in_use(main_window,port):
        # emit a signal to print the error to the console
        main_window.scan_general_console.emit("Port is already in use")
        return False

    emulator_thread: EmulatorThread = EmulatorThread(main_window, port, index, "scan_general")

    # Store the thread in the main_window for reference
    setattr(main_window.widgets, f'emulator_thread_{index}', emulator_thread)

    # Connect signals
    emulator_thread.scan_general_finished.connect(lambda : on_general_scan_finished(main_window))
    emulator_thread.scan_general_error.connect(lambda : stop_general_scan_instance(main_window))
    emulator_thread.scan_general_console.connect(lambda message: update_scan_console(main_window, message))
    emulator_thread.add_general_signal.connect(lambda general: add_general_to_frame(main_window, general))

    # Start the emulator thread
    emulator_thread.start()

    return True

def stop_general_scan_instance(main_window: 'MainWindow') -> None:
    """
    Stop the emulator instance thread for the given index.
    If index is 999, update the scan generals button instead of the run button.
    """
    emulator_thread: Optional[EmulatorThread] = getattr(main_window.widgets, f'emulator_thread_999', None)
    if emulator_thread:
        emulator_thread.stop()
        main_window.widgets.scan_generals_btn.setText("Scan Generals")

def update_run_button_icon(main_window: 'MainWindow', index: int, running: bool) -> None:
    """
    Update the run/stop button icons for both the instance manager and run tab.
    :param running: True if the instance is running, False if stopped.
    """
    run_icon: QIcon = QIcon(":/icons/images/icons/cil-media-play.png")
    stop_icon: QIcon = QIcon(":/icons/images/icons/cil-media-pause.png")

    # Get the buttons from both the instance manager and run tab
    run_button_instance_manager: Optional[QPushButton] = getattr(main_window.widgets, f'im_run_btn_{index}', None)
    run_button_run_tab: Optional[QPushButton] = getattr(main_window.widgets, f'run_btn_{index}', None)

    # Update the icons
    if running:
        if run_button_instance_manager:
            run_button_instance_manager.setIcon(stop_icon)
        if run_button_run_tab:
            run_button_run_tab.setIcon(stop_icon)
    else:
        if run_button_instance_manager:
            run_button_instance_manager.setIcon(run_icon)
        if run_button_run_tab:
            run_button_run_tab.setIcon(run_icon)

def check_port_already_in_use(main_window: 'MainWindow', port: str) -> bool:
    """
    Check if the given port is already in use by any running emulator instance.

    :param main_window: The main window containing references to running emulator instances.
    :param port: The port number to check.
    :return: True if the port is already in use, otherwise False.
    """
    # Check if there are running instances
    if hasattr(main_window.widgets, 'running_instance_indices'):
        for index in main_window.widgets.running_instance_indices:
            # Access the emulator thread for the given index
            emulator_thread: EmulatorThread = getattr(main_window.widgets, f'emulator_thread_{index}', None)
            if emulator_thread and emulator_thread.isRunning() and emulator_thread.port == port:
                return True  # Port is already in use

    return False  # No matching port in running instances

def on_general_scan_finished(main_window: 'MainWindow') -> None:

    emulator_thread: Optional[EmulatorThread] = getattr(main_window.widgets, f'emulator_thread_999', None)
    main_window.widgets.scan_generals_btn.setText("Scan Generals")
    emulator_thread.scan_general_console.emit("General scanning is now complete.\n"
                                              "Kindly review the list of scanned generals and remove any unwanted or duplicated entries.\n")

def on_emulator_finished(main_window: 'MainWindow', index: int) -> None:
    """
    Handle when the emulator thread finishes.
    If index is 999, update the Scan Generals button and print success message.
    Otherwise, update the run button icon.
    """
    update_run_button_icon(main_window, index, running=False)


def on_emulator_error(main_window: 'MainWindow', index: int, error: str) -> None:
    """
    Handle any errors in the emulator thread.
    Log or display the error message and stop the instance.
    """
    print(f"Error in Emulator {index}: {error}")
    stop_emulator_instance(main_window, index)


def sync_lineedits(lineedit1: QLineEdit, lineedit2: QLineEdit, button: QPushButton = None) -> None:
    """
    Synchronize two QLineEdits so that changes in one are reflected in the other.
    Optionally, update the button text when the name QLineEdit changes.
    """
    def update_lineedit2(text: str):
        # Block the signal to avoid an infinite loop
        if not lineedit2.signalsBlocked():
            lineedit2.blockSignals(True)
            lineedit2.setText(text)
            lineedit2.blockSignals(False)
        if button:
            button.setText(text)

    def update_lineedit1(text: str):
        # Block the signal to avoid an infinite loop
        if not lineedit1.signalsBlocked():
            lineedit1.blockSignals(True)
            lineedit1.setText(text)
            lineedit1.blockSignals(False)

    # Connect signals from both lineedits to each other
    lineedit1.textChanged.connect(update_lineedit2)
    lineedit2.textChanged.connect(update_lineedit1)
