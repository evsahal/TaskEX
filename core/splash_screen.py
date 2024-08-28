from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QProgressBar, QMainWindow
from PySide6.QtCore import Qt

from core.app_settings import Settings
from gui.generated.splash_screen import Ui_SplashScreen


class SplashScreen(QMainWindow):
    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)
        self.ui = Ui_SplashScreen()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Initialize the UI on this QMainWindow

        # Set up the central widget using the generated UI setup
        self.setCentralWidget(self.ui.centralwidget)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Optional: Hide the window frame for a splash effect

        # Set Splash Screen Version
        self.ui.label_title_version.setText(
            f'<html><head/><body><p>TaskEnforcerX <span style=" font-size:16pt;">{Settings.VERSION}</span></p></body></html>')

        # Customize UI elements
        # self.ui.guest_button.clicked.connect(self.login_as_guest)


    def login_as_guest(self):
        print("Logged in as Guest")
        self.accept()  # Close splash screen

