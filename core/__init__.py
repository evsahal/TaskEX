import os
import ctypes
import sys

from PySide6.QtGui import QGuiApplication


def set_approximate_dpi():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    print(f"Reported resolution: {screen_width}x{screen_height}")



    # Map screen sizes to DPI
    # Approximate DPI based on screen width and height
    if screen_width >= 5120 or screen_height >= 2880:  # 5K Displays
        dpi = 192
    elif screen_width >= 3840 or screen_height >= 2160:  # 4K Displays
        dpi = 144
    elif screen_width >= 2560 or screen_height >= 1440:  # 2K Displays
        dpi = 120

    elif screen_width >= 1920 or screen_height >= 1080:  # 1680x1050 Displays
        dpi = 96
    elif screen_width >= 1680 or screen_height >= 1050:  # 1680x1050 Displays
        print("CP - 1")
        dpi = 110
    elif screen_width >= 1600 or screen_height >= 900:  # 1600x900 Displays
        print("CP - 2... 1600x900::1600x900(dpi 82),1440x900::1440x900(dpi 77)")
        dpi = 77
    elif screen_width >= 1440 or screen_height >= 900:  # 1440x900 Displays
        print("CP - 3... 1536x864::1920x1080")
        dpi = 96
    elif screen_width >= 1400 or screen_height >= 1050:  # 1400x1050 Displays
        print("CP - 4")
        dpi = 96
    elif screen_width >= 1366 or screen_height >= 768:  # 1366x768 Displays
        print("CP - 5... 1344x840::1680x1050(dpi 86),1120x840::1400x1050(dpi 86),1366x768::1366x768(dpi 75)")
        dpi = 75
    elif screen_width >= 1280 or screen_height >= 1024:  # 1280x1024 Displays
        print("CP - 6")
        dpi = 96
    elif screen_width >= 1280 or screen_height >= 960:  # 1280x960 Displays
        print("CP - 7")
        dpi = 96
    elif screen_width >= 1280 or screen_height >= 800:  # 1280x800 Displays
        print("CP - 8")
        dpi = 96
    elif screen_width >= 1280 or screen_height >= 768:  # 1280x768 Displays
        print("CP - 9")
        dpi = 96
    elif screen_width >= 1280 or screen_height >= 720:  # 1280x720 Displays
        print("CP - 10")
        dpi = 96
    else:  # For lower resolutions
        print("CP - 11")
        dpi = 72

    # Set QT_FONT_DPI environment variable
    os.environ["QT_FONT_DPI"] = str(dpi)

# Call the function to set DPI before creating QApplication
set_approximate_dpi()
