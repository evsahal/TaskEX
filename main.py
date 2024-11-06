import os
import sys

from PySide6.QtWidgets import QApplication

from PySide6.QtGui import QIcon

from core.main_window import MainWindow
from core.splash_screen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    splash = SplashScreen()  # Create and show the splash screen

    window = MainWindow(splash)  # Pass the splash screen instance to the main window
    splash.show()  # Ensure the splash screen is on top during initialization
    sys.exit(app.exec())