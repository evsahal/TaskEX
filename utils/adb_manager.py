import os
import subprocess
import adbutils
from typing import Optional

class ADBManager:
    def __init__(self, port: str):
        self.device = None
        self.port = port
        self.connect_to_device()

    @staticmethod
    def initialize_adb() -> None:
        """
        Initialize the ADB environment: set the ADB path and start the ADB server.
        This function should be called when starting the bot.
        """
        ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ADB_PATH: str = os.path.join(ROOT_DIR, 'platform-tools')
        # print(f"ADB Path: {ADB_PATH}")
        os.environ["PATH"] += os.pathsep + ADB_PATH

        try:
            # print("Starting ADB server...")
            subprocess.run(["adb", "start-server"], check=True)
            print("ADB server started.")
        except subprocess.CalledProcessError as e:
            # print(f"Failed to start ADB server: {e}")
            exit(1)

    def connect_to_device(self) -> None:
        """
        Connect to an emulator using a specific port and store the device instance.
        """
        client: adbutils.AdbClient = adbutils.AdbClient()
        ip_address: str = f"127.0.0.1:{self.port}"

        try:
            # print(f"Connecting to emulator on port {self.port}...")
            subprocess.run(["adb", "connect", ip_address], check=True)
            # print(f"Connected to emulator on port {self.port}.")
            self.device: Optional[adbutils.AdbDevice] = client.device(serial=ip_address)
        except subprocess.CalledProcessError as e:
            # print(f"Failed to connect to emulator on port {self.port}: {e}")
            self.device = None

    def disconnect_device(self) -> None:
        """
        Disconnect the connected device from ADB.
        """
        if self.device:
            ip_address = f"127.0.0.1:{self.port}"
            try:
                subprocess.run(["adb", "disconnect", ip_address], check=True)
                self.device = None
                # print(f"Disconnected device on port {self.port}.")
            except subprocess.CalledProcessError as e:
                # print(f"Failed to disconnect device on port {self.port}: {e}")
                pass
        else:
            # print("No device to disconnect.")
            pass

    def tap(self, x: int, y: int) -> None:
        """
        Perform a tap operation on the specified device at (x, y) coordinates.
        """
        if self.device:
            self.device.shell(f"input tap {x} {y}")
            # print(f"Tapped on device {self.device.serial} at ({x}, {y}).")
        else:
            # print("Device not connected or found.")
            pass

    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration: int = 500) -> None:
        """
        Perform a swipe operation on the specified device from (x1, y1) to (x2, y2) over a duration (ms).
        """
        if self.device:
            self.device.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")
            # print(f"Swiped on device {self.device.serial} from ({x1}, {y1}) to ({x2}, {y2}) over {duration} ms.")
        else:
            # print("Device not connected or found.")
            pass

    def take_screenshot(self) -> Optional[bytes]:
        """
        Take a screenshot of the specified device and return the screenshot data.
        """
        if self.device:
            output = self.device.shell("screencap -p", encoding=None)
            # print(f"Screenshot taken for device {self.device.serial}.")
            return output
        else:
            # print("Device not connected or found.")
            return None

    def launch_evony(self, start: bool = True) -> None:
        """
        Start or stop the Evony app on the connected device using adbutils.
        By default, it is configured to start the Evony app.

        :param start: True to start the app, False to stop the app.
        """
        package_name: str = "com.topgamesinc.evony"
        main_activity: str = "com.topgamesinc.androidplugin.UnityActivity"

        if self.device:
            if start:
                if main_activity:
                    # Start the app by launching the main activity
                    self.device.shell(f"am start -n {package_name}/{main_activity}")
                    # print(f"Started {package_name} with main activity {main_activity}.")
                else:
                    # print("Main activity is required to start the app.")
                    pass
            else:
                # Stop the app
                self.device.shell(f"am force-stop {package_name}")
                # print(f"Stopped {package_name}.")
        else:
            # print("Device not connected or found.")
            pass