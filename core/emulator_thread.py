from datetime import datetime
import os

import ntplib
from PySide6.QtCore import QThread, Signal

from config.settings import get_expire
from core.services.bm_monsters_service import start_simulate_monster_click, \
    generate_template_image, capture_template_ss
from core.services.bm_scan_generals_service import start_scan_generals
from db.models import General
from utils.adb_manager import ADBManager
import logging

from utils.get_controls_info import get_join_rally_controls


class EmulatorThread(QThread):
    # Define signals to communicate with the main thread
    finished = Signal(int, bool)  # Emits when the thread is finished (index, success flag)
    error = Signal(int, str)  # Emits when an error occurs (index, error message)
    add_general_signal = Signal(General)
    scan_general_finished = Signal()
    scan_general_console = Signal(str)
    scan_general_error = Signal()

    def __init__(self, main_window, port: str, index: int, operation_type: str, parent=None, ref=None):
        super().__init__(parent)
        self.main_window = main_window
        self.port = port
        self.index = index
        self.operation_type = operation_type
        self.ref = ref
        self._running = True
        self.adb_manager = ADBManager(port)
        self.logger = self.configure_logger()

    def configure_logger(self):
        """
        Configures and returns a logger based on the operation type and ensures unique logger instances.
        Logs to both a file and optionally a QTextEdit widget for "emu".
        """
        # Create a unique logger name based on operation_type and index
        if self.operation_type == "emu":
            # Get the emulator name from the LineEdit
            emulator_name = getattr(self.main_window.widgets, f"emu_name_{self.index}").text()
            logger_name = f"{emulator_name}"
        else:
            logger_name = f"{self.operation_type}"

        # Create a logger with the unique name
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # Ensure handlers are not duplicated
        if not logger.handlers:  # Only add handlers if none exist
            # File handler
            log_file_path = f"logs.log"
            # Create the file if it does not exist
            if not os.path.exists(log_file_path):
                with open(log_file_path, "w") as f:
                    pass  # Create an empty file
            file_handler = logging.FileHandler(log_file_path, mode="a")
            file_formatter = logging.Formatter('[%(name)s] [%(asctime)s] [%(levelname)s]: %(message)s')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Stream handler for console (optional for emu)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(file_formatter)
            logger.addHandler(stream_handler)

            # QTextEdit handler (for "emu" only)
            if self.operation_type == "emu":
                console_widget = getattr(self.main_window.widgets, f"console_{self.index}", None)
                if console_widget:
                    class QTextEditHandler(logging.Handler):
                        def emit(self, record):
                            msg = self.format(record)
                            console_widget.append(msg)

                    text_edit_handler = QTextEditHandler()
                    text_edit_handler.setFormatter(file_formatter)
                    logger.addHandler(text_edit_handler)

        return logger

    def validate_run(self):
        """
        Validates the emulator environment before running operations.
        Checks expiry, device connection and screen resolution.
        """
        # Check expiry date
        if not self.validate_expiry():
            return False

        # Check if the device is connected
        if not self.adb_manager.device:
            error_message = f"No device found on port {self.port}"
            self.logger.error(error_message)
            if self.index == 999:
                self.scan_general_console.emit(error_message)
                self.scan_general_error.emit()
            elif self.index == 998:
                pass
            else:
                self.error.emit(self.index, error_message)
            return False

        # Validate screen resolution
        resolution = self.adb_manager.get_screen_resolution()
        print(resolution)
        if resolution != (540, 960) and resolution != (960, 540):
            error_message = f"Unsupported screen resolution: {resolution}. Expected: (540, 960)."
            self.logger.error(error_message)
            self.error.emit(self.index, error_message)
            return False

        self.logger.info("Validation passed. Device is now connected.")
        return True

    def validate_expiry(self):
        """
        Validates the bot's expiry date using an NTP server.
        Returns True if valid, False if expired or unable to verify.
        """
        try:
            # Query current time from NTP server
            ntp_client = ntplib.NTPClient()
            response = ntp_client.request('pool.ntp.org', version=3)
            current_utc = datetime.utcfromtimestamp(response.tx_time)
        except Exception as e:
            self.logger.error(f"Error fetching time from NTP server: {e}")
            return False  # Validation fails if unable to fetch time

        # Compare current date with expiry date
        print(get_expire())
        expiry_date = datetime.strptime(get_expire(), "%Y-%m-%d")
        if current_utc.date() > expiry_date.date():
            self.logger.error(f"Bot expired on {expiry_date.date()}")
            return False
        # self.logger.info(f"Expiry check passed. Current date: {current_utc.date()}, Expiry date: {expiry_date.date()}.")
        return True

    def run(self):
        """
        Code to be executed when the thread starts. Runs in a separate thread.
        """
        try:
            if not self.validate_run():
                self._running = False
                return

            # Perform the operation based on the type
            if self.operation_type == "emu":
                self.run_emulator_instance()
            elif self.operation_type == "scan_general":
                start_scan_generals(self)
            elif self.operation_type == "capture_template_ss":
                capture_template_ss(self)
            elif self.operation_type == "generate_template_image":
                generate_template_image(self)
            elif self.operation_type == "simulate_monster_click":
                start_simulate_monster_click(self)

        except Exception as e:
            self.logger.exception("An error occurred during the emulator thread execution.")
            self.error.emit(self.index, str(e))
        finally:
            self.finished.emit(self.index, self._running)
            self.stop()

    def stop(self):
        """
        Stops the thread safely.
        """
        if self._running:
            self._running = False
            self.adb_manager.disconnect_device()
            self.logger.info("Thread stopped and disconnected.")

    def run_emulator_instance(self):
        """
        Runs the emulator instance based on the mode.
        """
        self.run_join_rally()

    def run_join_rally(self):
        controls = get_join_rally_controls(self.main_window, self.index)
        print(controls)
        # count = 0
        # while self._running:
        #     try:
        #         if self.index == 1:
        #             self.adb_manager.swipe(100, 300, 500, 300)
        #         else:
        #             self.adb_manager.swipe(250, 100, 250, 700)
        #
        #         count += 1
        #         if count > 20:
        #             break
        #     except Exception as e:
        #         self.logger.error(f"Error during emulator operation: {e}")
        #         self.error.emit(self.index, str(e))
        #         break

