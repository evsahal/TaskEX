import os
import ctypes

def set_approximate_dpi():
    # Detect screen resolution (works on Windows)
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    # print(f"{screen_width}x{screen_height}")
    # Approximate DPI based on resolution
    if screen_width >= 3840 or screen_height >= 2160:  # Roughly for 4K displays
        dpi = 144
    elif screen_width >= 2560 or screen_height >= 1440:  # Roughly for 2K displays
        dpi = 120
    else:  # For 1080p and lower
        dpi = 96

    # Set QT_FONT_DPI environment variable
    os.environ["QT_FONT_DPI"] = str(dpi)

# Call the function to set DPI before creating QApplication
set_approximate_dpi()
