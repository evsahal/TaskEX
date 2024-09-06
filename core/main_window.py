import os
import time
from tkinter import font

from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QMainWindow, QHeaderView, QScrollArea, QVBoxLayout, QLabel, QSizePolicy, QFrame, \
    QPushButton

from core.app_settings import Settings
from core.instance_manager import setup_port_display_table, get_available_ports, reload_ports
from core.menu_button import connect_buttons, initialize_instances
from core.ui_functions import UIFunctions
from gui.generated.ui_main import Ui_MainWindow
from utils.adb_manager import ADBManager

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

class MainWindow(QMainWindow):
    def __init__(self, splash_screen):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widgets = self.ui

        # Connect the splash screen's guest login signal to a method to start initialization
        splash_screen.load_signal.connect(lambda: self.perform_initialization(splash_screen))

    def perform_initialization(self, splash_screen):
        # print("Loading...")
        # List of initialization steps with corresponding messages
        init_steps = [
            ("Loading UI Settings",self.load_ui_settings),
            # ("Loading Configurations", self.load_configurations),
            ("Initializing ADB", self.init_adb),
            ("Initializing Instances", self.init_instance),
            ("Finalizing Setup", self.finalize_setup)
        ]

        splash_screen.ui.progressBar.setMaximum(len(init_steps))


        for i, (message, function) in enumerate(init_steps):
            QTimer.singleShot(i * 1000,
                              lambda msg=message, func=function, idx=i + 1: self.load_step(splash_screen, msg, func,
                                                                                           idx))

    def load_ui_settings(self):
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APPLY TEXTS
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(Settings.TITLE)
        self.widgets.titleLeftApp.setText(Settings.TITLE)
        self.widgets.titleLeftDescription.setText(Settings.TITLE_DESCRIPTION)
        # widgets.titleRightInfo.setText(Settings.DESCRIPTION)
        self.widgets.creditsLabel.setText(Settings.CREDITS)
        self.widgets.version.setText(Settings.VERSION)

        # Create a scroll area for the topMenu
        self.scroll_area = QScrollArea(self.widgets.leftMenuFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setStyleSheet("background-color: rgb(37, 41, 48);")
        self.scroll_area.setWidget(self.widgets.topMenu)

        # Get the layout of leftMenuFrame
        layout = self.widgets.leftMenuFrame.layout()
        self.widgets.topMenu.layout().setAlignment(Qt.Alignment.AlignTop)

        # Add widgets to the layout in the desired order
        layout.addWidget(self.widgets.toggleBox)  # Toggle box at the top
        layout.addWidget(self.scroll_area)  # Scroll area next
        # layout.addStretch()
        layout.addWidget(self.widgets.bottomMenu)  # Instance Manager at the bottom

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # LEFT MENUS
        # Connect buttons directly to click events
        connect_buttons(self)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        self.widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        self.widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        #Remove this
        self.widgets.pushButton.clicked.connect(self.test)

        # SCREEN SIZE
        UIFunctions.screen_size(self)

        # Load Active Ports UI Setup
        setup_port_display_table(self)

        # Load Open Emulator Ports
        reload_ports(self)
        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)
        self.widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(self.widgets.btn_home.styleSheet()))

    def finalize_setup(self):
        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)
        self.widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(self.widgets.btn_home.styleSheet()))

        # Test
        # print(getattr(self.widgets, f"im_emu_1").text())

    def init_adb(self):

        # call the iniitializer for adb
        ADBManager.initialize_adb()


    def test(self):
        # swipe
        # self.adb_instance.swipe(30,300,500,300)
        pass

    def init_instance(self):
        # Load the Default Instances
        initialize_instances(self, 1)

    def load_step(self, splash_screen, message, function, index):
        splash_screen.ui.progressBar.setValue(index)
        splash_screen.ui.label_loading.setText(message)
        function()  # Execute the initialization function

        if index == splash_screen.ui.progressBar.maximum():
            splash_screen.close()
            # SHOW MAIN APP
            # ///////////////////////////////////////////////////////////////
            self.show()


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')
