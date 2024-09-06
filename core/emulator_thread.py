from PySide6.QtCore import QThread, Signal

from utils.adb_manager import ADBManager


class EmulatorThread(QThread):
    # Define signals to communicate with the main thread
    finished = Signal(int)  # Signal to emit when the thread is finished
    error = Signal(int, str)  # Signal to emit when an error occurs, passing the instance index and error message

    def __init__(self, port: str, index: int, emulator_index, parent=None):
        super().__init__(parent)
        self.port = port
        self.index = index
        self.emulator_index = emulator_index
        self.device = ADBManager(port)
        self._running = True

    def run(self):
        """
        Code to be executed when the thread starts. This function runs in a separate thread.
        """
        try:
            # Connect to the port
            self.device.connect_to_device()

            while self._running:
                # Add your emulator-related operations here
                # Example operation: self.adb_manager.tap(100, 200)
                pass


        except Exception as e:
            self.error.emit(self.index, str(e))
        finally:
            self.finished.emit(self.index)

    def stop(self):
        """
        Stop the thread safely.
        """
        self._running = False
        self.device.disconnect_device()