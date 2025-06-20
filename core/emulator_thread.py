import time
from datetime import datetime
import os

import cv2
import ntplib
import numpy as np
from PySide6.QtCore import QThread, Signal

from core.services.bm_monsters_service import start_simulate_monster_click, \
    generate_template_image, capture_template_ss
from core.services.bm_scan_generals_service import start_scan_generals
from db.models import General
from features.logic.join_rally import run_join_rally
from utils.adb_manager import ADBManager
import logging

from utils.get_controls_info import get_game_settings_controls
from utils.helper_utils import get_current_datetime_string
from utils.image_recognition_utils import is_template_match, template_match_coordinates


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
        self.game_settings = {}
        self.cache = {}

    def configure_logger(self):
        """
        Configures and returns a logger with separate file and console handlers.
        """
        logger_name = self.operation_type if self.operation_type != "emu" else getattr(self.main_window.widgets,
                                                                                       f"emu_name_{self.index}").text()
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # Ensure handlers are not duplicated
        if not logger.handlers:
            # File handler setup
            log_file_path = f"logs.log"
            if not os.path.exists(log_file_path):
                with open(log_file_path, "w") as f:
                    pass  # Create an empty log file
            file_handler = logging.FileHandler(log_file_path, mode="a")
            if self.operation_type == "emu":
                file_formatter = logging.Formatter('[%(name)s] [%(asctime)s] [%(levelname)s]: %(message)s')
            elif self.operation_type == "scan_general":
                file_formatter = logging.Formatter('%(message)s')

            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Emulator console handler setup (for operation_type == "emu" with QTextEdit)
            if self.operation_type == "emu":
                console_widget = getattr(self.main_window.widgets, f"console_{self.index}", None)
                if console_widget:
                    class QTextEditHandler(logging.Handler):
                        def emit(self, record):
                            msg = self.format(record)
                            console_widget.append(msg)

                    self.console_handler = QTextEditHandler()
                    self.console_handler.setFormatter(file_formatter)
                    logger.addHandler(self.console_handler)

            # General scan console handler setup (for operation_type == "scan_general" with QPlainTextEdit)
            if self.operation_type == "scan_general":
                console_widget = getattr(self.main_window.widgets, "scan_general_console", None)
                if console_widget:
                    class GeneralScanHandler(logging.Handler):
                        def __init__(self, thread):
                            super().__init__()
                            self.thread = thread

                        def emit(self, record):
                            msg = self.format(record)
                            console_widget.appendPlainText(msg)

                    self.console_handler = GeneralScanHandler(self)
                    self.console_handler.setFormatter(file_formatter)
                    logger.addHandler(self.console_handler)

        return logger

    def log_message(self, message: str, level: str = "info", console: bool = True):
        """
        Logs a message at the specified level and optionally to the console.

        :param message: The log message.
        :param level: Log level ("info", "debug", "warning", "error", "critical").
        :param console: Whether to log to the QTextEdit console.
        """
        # Temporarily detach the console handler if console logging is disabled
        # if not console and hasattr(self, 'console_handler'):
        #     self.logger.removeHandler(self.console_handler)
        #
        # # Dynamically get the log method based on the level
        # log_method = getattr(self.logger, level.lower(), self.logger.info)
        # log_method(message)  # Perform the logging
        #
        # # Reattach the console handler if it was temporarily removed
        # if not console and hasattr(self, 'console_handler'):
        #     self.logger.addHandler(self.console_handler)
        pass


    def validate_run(self):
        """
        Validates the emulator environment before running operations.
        Checks device connection and screen resolution.
        """
        # Check if the device is connected
        if not self.adb_manager.device:
            error_message = f"No device found on port {self.port}"
            self.log_message(error_message,"error")
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
        # print(resolution)
        if resolution != (540, 960) and resolution != (960, 540):
            error_message = f"Unsupported screen resolution: {resolution[0]}x{resolution[1]}. Expected: 540x960."
            self.logger.error(error_message)
            self.error.emit(self.index, error_message)
            return False

        self.logger.info("Validation passed. Device is now connected.")
        return True


    def run(self):
        """
        Code to be executed when the thread starts. Runs in a separate thread.
        """
        try:
            if not self.validate_run():
                self._running = False
                return

            # Load the game settings
            self.game_settings = get_game_settings_controls(self.main_window, self.index)

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
            self.log_message(f"Thread Run : {e}",level="error",console=False)
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
            self.cache = {}
            self.logger.info("Thread stopped and disconnected.")

    def thread_status(self):
        return self._running

    def run_emulator_instance(self):
        """
        Runs the emulator instance based on the mode.
        """
        run_join_rally(self)

    def capture_and_validate_screen(self,kick_timer=True, ads=True):
        try:
            src_img = self.adb_manager.take_screenshot()
            restart_img = cv2.imread("assets/540p/other/restart_btn.png")
            world_map_btn = cv2.imread("assets/540p/other/explore_world_map_btn.png")

            if kick_timer and is_template_match(src_img, restart_img,threshold=0.9):
                # print(f"kick timer activated {self.game_settings['kick_reload']}")
                self.logger.info(f"Kick & Reload activated for {self.game_settings['kick_reload']} min(s)")
                time.sleep(self.game_settings['kick_reload'] * 60)

                # print("kick timer done")
                self.logger.info("Kick timer done. Restart initiated")
                # Restart the game
                src_img = self.adb_manager.take_screenshot()
                restart = template_match_coordinates(src_img, restart_img)
                if restart:
                    self.adb_manager.tap(restart[0], restart[1])
                    time.sleep(7)
                    src_img = self.adb_manager.take_screenshot()
                else:
                    # When restart button is gone, restart the game by starting it again
                    self.adb_manager.launch_evony(False)
                    time.sleep(1)
                    self.adb_manager.launch_evony(True)
                start_time = time.time()
                timeout = 60

                while not is_template_match(src_img, world_map_btn):
                    # Wait a bit before the next screenshot to reduce CPU usage
                    time.sleep(1)
                    # Check if the timeout has been reached
                    elapsed_time = time.time() - start_time
                    if elapsed_time > timeout:
                        # print("Game stuck in loading screen. Restarting...")
                        self.logger.info("Game stuck in loading screen. Restarting...")
                        self.adb_manager.launch_evony(False)  # Close the game
                        time.sleep(1)  # Wait for a few seconds before relaunching
                        self.adb_manager.launch_evony(True)  # Relaunch the game
                        start_time = time.time()  # Reset the start time after relaunching

                    # print("Still loading")
                    # Capture the new image
                    src_img = self.adb_manager.take_screenshot()

            if ads:
                for i in range(1, 7):
                    ads_img = cv2.imread(f"assets/540p/other/x{i}.png")
                    if is_template_match(src_img, ads_img):
                        if i == 6:
                            pair_image = cv2.imread(f"assets/540p/other/x{i}_pair.png")
                            if not is_template_match(src_img, pair_image):
                                continue
                        # print("Ads found")

                        ads_match = template_match_coordinates(src_img, ads_img)
                        if not ads_match:
                            continue
                        self.logger.info("Closing the ads/pop-ups")
                        self.adb_manager.tap(ads_match[0], ads_match[1])
                        time.sleep(1)
                        src_img = self.adb_manager.take_screenshot()
                        break
            return src_img
        except Exception as e:
            print(e)
            return None



