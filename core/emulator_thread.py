from PySide6.QtCore import QThread, Signal

from core.features.bm_scan_generals import start_scan_generals
from db.models import General
from utils.adb_manager import ADBManager


class EmulatorThread(QThread):
    # Define signals to communicate with the main thread
    finished = Signal(int, bool)  # Signal to emit when the thread is finished (with success flag)
    error = Signal(int, str)  # Signal to emit when an error occurs, passing the instance index and error message
    add_general_signal = Signal(General)
    scan_general_finished = Signal()
    scan_general_console = Signal(str)
    scan_general_error = Signal()

    def __init__(self, main_window, port: str, index: int, operation_type: str, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.port = port
        self.index = index
        self.adb_manager = ADBManager(port)
        self.operation_type = operation_type
        self._running = True

    def run(self):
        """
        Code to be executed when the thread starts. This function runs in a separate thread.
        """
        try:
            # Check if the device is connected
            if not self.adb_manager.device:
                # If scan general, then console on the scan general window
                if self.index == 999:
                    self.scan_general_console.emit(f"No device found on port {self.port}")
                    # Stop the thread
                    self.scan_general_error.emit()
                else:
                    self.error.emit(self.index, f"No device found on port {self.port}")
                self._running = False
                return

            # Start emulator instance operations
            if self.operation_type == "emu":
                self.run_emulator_instance()
            elif self.operation_type == "scan_general":
                self.scan_generals()

        except Exception as e:
            self.error.emit(self.index, str(e))
        finally:
            # Emit finished signal (False if it was stopped due to error)
            self.finished.emit(self.index, self._running)
            self.stop()

    def run_emulator_instance(self):
        """
        Run the emulator instance based on the index.
        """
        count = 0
        while self._running:
            if self.index == 1:
                self.adb_manager.swipe(100, 300, 500, 300)
            else:
                self.adb_manager.swipe(250, 100, 250, 700)

            count += 1
            if count > 20:
                break

    def scan_generals(self):
        """
        Start scanning generals.
        """
        start_scan_generals(self)

    def stop(self):
        """
        Stop the thread safely.
        """
        self._running = False
        self.adb_manager.disconnect_device()