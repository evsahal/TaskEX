from time import sleep

from PySide6.QtCore import QThread, Signal

from utils.adb_manager import ADBManager


class EmulatorThread(QThread):
    # Define signals to communicate with the main thread
    finished = Signal(int)  # Signal to emit when the thread is finished
    error = Signal(int, str)  # Signal to emit when an error occurs, passing the instance index and error message

    def __init__(self, port: str, index: int, parent=None):
        super().__init__(parent)
        self.port = port
        self.index = index
        self.device = ADBManager(port)
        self._running = True

    def run(self):
        """
        Code to be executed when the thread starts. This function runs in a separate thread.
        """
        try:
            # Connect to the port
            self.device.connect_to_device()
            print("running")
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