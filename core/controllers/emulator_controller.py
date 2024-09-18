from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QLineEdit
from core.emulator_thread import EmulatorThread
from typing import Optional

from gui.controllers.bm_scan_generals_controller import add_general_to_frame


def handle_run_button(main_window: 'MainWindow', index: int) -> None:
    """
    Handle the Run button click event for an instance.
    Start or stop the emulator instance and update the button icons.
    """
    # Check if the emulator thread for this instance is already running
    if hasattr(main_window.widgets, f'emulator_thread_{index}') and getattr(main_window.widgets, f'emulator_thread_{index}').isRunning():
        # If the thread is running, stop it
        stop_emulator_instance(main_window, index)
    else:
        # Start a new emulator thread
        start_emulator_instance(main_window, index)


def start_emulator_instance(main_window: 'MainWindow', index: int) -> None:
    """
    Start the emulator instance thread for the given index.
    """
    # Get port number
    port: str = getattr(main_window.widgets, f"im_emu_port_{index}").text()
    emulator_thread: EmulatorThread = EmulatorThread(main_window,port, index,"emu")

    # Store the thread in the main_window for reference
    setattr(main_window.widgets, f'emulator_thread_{index}', emulator_thread)

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
    """
    emulator_thread: Optional[EmulatorThread] = getattr(main_window.widgets, f'emulator_thread_{index}', None)
    if emulator_thread:
        emulator_thread.stop()

    # Check if the index is not for scan generals
    if index != 999:
        # Update button icons to "Run" in both instance manager and run tab
        update_run_button_icon(main_window, index, running=False)


def handle_scan_general_button(main_window: 'MainWindow') -> None:
    # Index = 999 for scan general
    index = 999
    # Check if the emulator thread for this instance is already running
    if hasattr(main_window.widgets, f'emulator_thread_{index}') and getattr(main_window.widgets, f'emulator_thread_{index}').isRunning():
        # If the thread is running, stop it
        stop_emulator_instance(main_window, index)
        # Update the button text and console.
        main_window.widgets.scan_generals_btn.setText("Scan Generals")
        main_window.widgets.scan_general_console.appendPlainText("General scanning is now complete.\n"
                                                                 "Kindly review the list of scanned generals and remove any unwanted or duplicated entries.\n")
    else:
        # Start a new emulator thread
        start_general_scan_instance(main_window, index)
        # Change the button text to stop scanning
        main_window.widgets.scan_generals_btn.setText("Stop Scanning")

def start_general_scan_instance(main_window: 'MainWindow', index: int) -> None:
    """
    Start the emulator instance thread for the given index.
    """
    # Get port number
    port : str = main_window.widgets.scan_generals_port.text()
    # TODO check if the port is already in use
    emulator_thread: EmulatorThread = EmulatorThread(main_window,port, index,"scan_general")

    # Store the thread in the main_window for reference
    setattr(main_window.widgets, f'emulator_thread_{index}', emulator_thread)

    # Connect signals
    emulator_thread.finished.connect(lambda idx: on_emulator_finished(main_window, idx))
    emulator_thread.error.connect(lambda idx, error: on_emulator_error(main_window, idx, error))
    emulator_thread.add_general_signal.connect(lambda general:add_general_to_frame(main_window,general))

    # Start the emulator thread
    emulator_thread.start()


def stop_general_scan_error(main_window: 'MainWindow') -> None:
    # Index = 999 for scan general
    index = 999
    # Check if the emulator thread for this instance is already running
    if hasattr(main_window.widgets, f'emulator_thread_{index}') and getattr(main_window.widgets,
                                                                            f'emulator_thread_{index}').isRunning():
        # If the thread is running, stop it
        stop_emulator_instance(main_window, index)
        # Update the button text and console.
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


def on_emulator_finished(main_window: 'MainWindow', index: int) -> None:
    """
    Handle when the emulator thread finishes.
    Update the button icons back to the "Run" icon.
    """
    update_run_button_icon(main_window, index, running=False)


def on_emulator_error(main_window: 'MainWindow', index: int, error: str) -> None:
    """
    Handle any errors in the emulator thread.
    You can display an error message in the UI or log it.
    """
    print(f"Error in Emulator {index}: {error}")


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
        # Update the button text if provided and if the lineedit1 (name) was changed
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
