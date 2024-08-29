import sys
import time

from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QProgressBar, QMainWindow, QWidget
from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QPoint, QEasingCurve, QTimer

from core.app_settings import Settings
from gui.generated.splash_screen import Ui_SplashScreen


class SplashScreen(QMainWindow):

    # Define a signal to continue loading the splash screen
    load_signal = Signal()

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

        self.ui.btn_login_guest.clicked.connect(self.login_as_guest)
        self.ui.btn_exit.clicked.connect(lambda: sys.exit())

        #  :: check and see if the option is remembered, so the login will be skipped
        self.logged_in = True

        if self.logged_in:

            self.hide_login_frame()

            # Emit signal after event loop starts
            QTimer.singleShot(0, self.load_signal.emit)

        else:
            # Set Splash screen window height for login
            self.setFixedHeight(450)

        self.show()  # Display the splash screen

    def hide_login_frame(self):
        # Hide the login frame
        self.ui.login_frame.setMaximumHeight(0)

        # Unhide the progress frame
        self.ui.progress_frame.setMaximumHeight(16777215)

        # Set Splash screen window height
        self.setFixedHeight(320)


    def login_as_guest(self):
        # print("Logged in as Guest")

        self.hide_login_frame()

        # Emit the signal to indicate guest login
        self.load_signal.emit()

        # # Start animations
        # self.animate_login_frame_hide()
        # self.animate_header_frame_move()


    # def animate_login_frame_hide(self):
    #     """ Animate hiding of the login frame by shrinking its height. """
    #     login_frame = self.ui.login_frame
    #     height = login_frame.height()
    #
    #     # Create an animation that changes the maximum height from current to 0
    #     animation = QPropertyAnimation(login_frame, b"maximumHeight")
    #     animation.setDuration(500)  # Animation duration in milliseconds
    #     animation.setStartValue(height)
    #     animation.setEndValue(0)
    #     animation.setEasingCurve(QEasingCurve.InOutQuad)  # easing for smooth animation
    #     animation.start()
    #
    #     # Adjust the main window height after animation completes
    #     animation.finished.connect(self.adjust_window_height(-height))
    #
    #     # Hide the login_frame completely after the animation
    #     animation.finished.connect( self.ui.login_frame.setMaximumHeight(0))
    #
    #
    # def animate_header_frame_move(self):
    #     """ Animate the header frame to move down slightly. """
    #     header_frame = self.ui.header_frame
    #     y_position = header_frame.pos().y()
    #
    #     # Create an animation to move the header_frame downwards
    #     animation = QPropertyAnimation(header_frame, b"pos")
    #     animation.setDuration(500)  # Animation duration in milliseconds
    #     animation.setStartValue(header_frame.pos())
    #     animation.setEndValue(header_frame.pos() + QPoint(0, 20))
    #     animation.start()
    #
    # def adjust_window_height(self, delta_height):
    #     """ Adjust the height of the QMainWindow. """
    #     # Set Splash screen window height
    #     self.setFixedHeight(350)