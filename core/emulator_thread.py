from time import sleep

from PySide6.QtCore import QThread, Signal

from core.features.bm_scan_generals import start_scan_generals
from db.models import General
from utils.adb_manager import ADBManager


class EmulatorThread(QThread):
    # Define signals to communicate with the main thread
    finished = Signal(int)  # Signal to emit when the thread is finished
    error = Signal(int, str)  # Signal to emit when an error occurs, passing the instance index and error message
    add_general_signal = Signal(General)

    def __init__(self, main_window,port: str, index: int, operation_type:str, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.port = port
        self.index = index
        self.device = ADBManager(port)
        self.operation_type = operation_type
        self._running = True

    def run(self):
        """
        Code to be executed when the thread starts. This function runs in a separate thread.
        """
        try:
            # Connect to the port
            self.device.connect_to_device()
            # print("running")
            if self.operation_type == "emu":
                count = 0
                while self._running:
                    # Add your emulator-related operations here
                    # Example operation: self.adb_manager.tap(100, 200)

                    if self.index == 1:
                        self.device.swipe(100,300,500,300)
                    else:
                        self.device.swipe(250, 100, 250, 700)

                    count += 1
                    if count > 20:
                        break
            elif self.operation_type == "scan_general":
                start_scan_generals(self)



        except Exception as e:
            self.error.emit(self.index, str(e))
        finally:
            self.finished.emit(self.index)
            if self._running:
                self.stop()

    def stop(self):
        """
        Stop the thread safely.
        """
        print("Stopped")
        self._running = False
        self.device.disconnect_device()