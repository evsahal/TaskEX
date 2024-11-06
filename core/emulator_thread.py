import cv2
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QIcon

from core.services.bm_monsters_service import generate_monster_template, start_simulate_monster_click
from core.services.bm_scan_generals_service import start_scan_generals
from db.models import General
from utils.adb_manager import ADBManager
from utils.image_recognition_utils import convert_cv_to_qimage, crop_image


class EmulatorThread(QThread):
    # Define signals to communicate with the main thread
    finished = Signal(int, bool)  # Signal to emit when the thread is finished (with success flag)
    error = Signal(int, str)  # Signal to emit when an error occurs, passing the instance index and error message

    add_general_signal = Signal(General)
    scan_general_finished = Signal()
    scan_general_console = Signal(str)
    scan_general_error = Signal()



    def __init__(self, main_window, port: str, index: int, operation_type: str, parent=None,ref=None):
        super().__init__(parent)
        self.main_window = main_window
        self.port = port
        self.index = index
        self.adb_manager = ADBManager(port)
        self.operation_type = operation_type
        self.ref = ref
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
                elif self.index == 998:
                    pass
                else:
                    self.error.emit(self.index, f"No device found on port {self.port}")
                self._running = False
                return

            # Start emulator instance operations
            if self.operation_type == "emu":
                self.run_emulator_instance()
            elif self.operation_type == "scan_general":
                self.scan_generals()
            elif self.operation_type == "capture_template_ss":
                self.capture_template_ss()
            elif self.operation_type == "generate_template_image":
                self.generate_template_image()
            elif self.operation_type == "simulate_monster_click":
                self.simulate_monster_click()

        except Exception as e:
            print(e)
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

    def capture_template_ss(self):
        # Capture the image
        captured_image = self.adb_manager.take_screenshot()

        # Emit the signal to update the Selection Tool Widget
        self.ref.frame_ready.emit(convert_cv_to_qimage(captured_image))

    def generate_template_image(self):
        """Generate the monster template image """
        try:
            # Change the icon to loading and disable the button
            self.ref.find_template_btn.setIcon(QIcon.fromTheme("sync-synchronizing"))
            self.ref.find_template_btn.blockSignals(True)

            captured_images = []
            for i in range(20):  # Capture 20 frames
                if not self._running:
                    break

                # Capture and crop the screenshot
                cropped = crop_image(
                    self.adb_manager.take_screenshot(),
                    self.ref.selection_tool.selected_area
                )

                # Ensure the cropped image is valid before saving
                if cropped is not None:
                    # cv2.imwrite(rf"E:\Projects\PyCharmProjects\TaskEX\temp\test\t_{i}.png", cropped)
                    captured_images.append(cropped)

            # Generate the template from the captured images
            template, best_threshold = generate_monster_template(captured_images)

            # Emit the template and threshold once processing is done
            self.ref.template_ready.emit(template, best_threshold)

        except Exception as e:
            print(f"[ERROR] Failed to generate template: {e}")

        finally:
            # Reset the icon and re-enable the button
            self.ref.reset_template_btn.emit()

    def simulate_monster_click(self):

        start_simulate_monster_click(self)


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