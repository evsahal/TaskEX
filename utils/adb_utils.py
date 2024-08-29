import os
import subprocess
import adbutils
from typing import Optional

def initialize_adb() -> None:
    """
    Initialize the ADB environment: set the ADB path and start the ADB server.
    This function should be called when starting the bot.
    """
    # Get the absolute path of the root directory (one level up from the current file's directory)
    ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the path to the platform-tools directory in the root directory
    ADB_PATH: str = os.path.join(ROOT_DIR, 'platform-tools')

    # Print the ADB_PATH to verify the path
    print(f"ADB Path: {ADB_PATH}")

    # Set the environment path for adb
    os.environ["PATH"] += os.pathsep + ADB_PATH

    # Start ADB server
    try:
        print("Starting ADB server...")
        subprocess.run(["adb", "start-server"], check=True)
        print("ADB server started.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start ADB server: {e}")
        exit(1)

def connect_to_device_by_port(port: str) -> Optional[adbutils.AdbDevice]:
    """
    Connect to an emulator using a specific port and return the device instance.

    :param port: The port number as a string to connect to the emulator.
    :return: An instance of adbutils.AdbDevice if connected, else None.
    """
    client: adbutils.AdbClient = adbutils.AdbClient()

    # Use adb connect with IP and port
    ip_address: str = f"127.0.0.1:{port}"
    try:
        print(f"Connecting to emulator on port {port}...")
        subprocess.run(["adb", "connect", ip_address], check=True)
        print(f"Connected to emulator on port {port}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to emulator on port {port}: {e}")
        return None

    # Now find the device using the serial number (which will include the port)
    device: Optional[adbutils.AdbDevice] = client.device(serial=ip_address)
    if device:
        return device
    else:
        print(f"Device at {ip_address} not found.")
        return None

def tap(device: adbutils.AdbDevice, x: int, y: int) -> None:
    """
    Perform a tap operation on the specified device at (x, y) coordinates.

    :param device: The adbutils.AdbDevice instance to perform the tap on.
    :param x: The x-coordinate for the tap.
    :param y: The y-coordinate for the tap.
    """
    if device:
        device.shell(f"input tap {x} {y}")
        print(f"Tapped on device {device.serial} at ({x}, {y}).")
    else:
        print("Device not connected or found.")

def swipe(device: adbutils.AdbDevice, x1: int, y1: int, x2: int, y2: int, duration: int = 500) -> None:
    """
    Perform a swipe operation on the specified device from (x1, y1) to (x2, y2) over a duration (ms).

    :param device: The adbutils.AdbDevice instance to perform the swipe on.
    :param x1: The starting x-coordinate for the swipe.
    :param y1: The starting y-coordinate for the swipe.
    :param x2: The ending x-coordinate for the swipe.
    :param y2: The ending y-coordinate for the swipe.
    :param duration: The duration of the swipe in milliseconds.
    """
    if device:
        device.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")
        print(f"Swiped on device {device.serial} from ({x1}, {y1}) to ({x2}, {y2}) over {duration} ms.")
    else:
        print("Device not connected or found.")

# def zoom(device: adbutils.AdbDevice, x1: int, y1: int, x2: int, y2: int, zoom_in: bool = True, duration: int = 500) -> None:
#     """
#     Perform a zoom operation on the specified device.
#
#     :param device: The adbutils.AdbDevice instance to perform the zoom on.
#     :param x1: The starting x-coordinate for the first finger.
#     :param y1: The starting y-coordinate for the first finger.
#     :param x2: The starting x-coordinate for the second finger.
#     :param y2: The starting y-coordinate for the second finger.
#     :param zoom_in: True for zoom in, False for zoom out.
#     :param duration: The duration of the zoom in milliseconds.
#     """
#     if device:
#         if zoom_in:
#             # Zoom in: move fingers apart
#             device.shell(f"input swipe {x1} {y1} {x1-100} {y1-100} {duration} & input swipe {x2} {y2} {x2+100} {y2+100} {duration}")
#             print(f"Zoomed in on device {device.serial} from ({x1}, {y1}) and ({x2}, {y2}) over {duration} ms.")
#         else:
#             # Zoom out: move fingers together
#             device.shell(f"input swipe {x1} {y1} {x1} {y1+270} {duration} & input swipe {x2} {y2} {x2} {y2-270} {duration}")
#             print(f"Zoomed out on device {device.serial} from ({x1}, {y1}) and ({x2}, {y2}) over {duration} ms.")
#     else:
#         print("Device not connected or found.")



def take_ss(device: adbutils.AdbDevice) -> Optional[bytes]:
    """
    Take a screenshot of the specified device and return the screenshot data.

    :param device: The adbutils.AdbDevice instance to take the screenshot from.
    :return: The screenshot data as bytes, or None if the device is not connected.
    """
    if device:
        # Execute screencap command and get the output
        output = device.shell("screencap -p", encoding=None)
        print(f"Screenshot taken for device {device.serial}.")
        return output
    else:
        print("Device not connected or found.")
        return None

# later change this to generic and create another function for game operations like launchEvony and use this there
def manage_app(
    device: adbutils.AdbDevice,
    package_name: str = "com.topgamesinc.evony",
    main_activity: str = "com.topgamesinc.androidplugin.UnityActivity",
    start: bool = True
) -> None:
    """
    Generic function to start or stop an app on an Android device using adbutils.
    By default, it is configured to manage the Evony app.

    :param device: The adbutils.AdbDevice instance to interact with.
    :param package_name: The package name of the app to start or stop (default is Evony).
    :param main_activity: The main activity to start (default is Evony's main activity, required only if starting the app).
    :param start: True to start the app, False to stop the app.
    """
    if start:
        if main_activity:
            # Start the app by launching the main activity
            device.shell(f"am start -n {package_name}/{main_activity}")
            print(f"Started {package_name} with main activity {main_activity}.")
        else:
            print("Main activity is required to start the app.")
    else:
        # Stop the app
        device.shell(f"am force-stop {package_name}")
        print(f"Stopped {package_name}.")