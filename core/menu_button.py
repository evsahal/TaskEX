import sys
from operator import indexOf
from turtledemo.sorting_animate import ssort

from PySide6.QtCore import QSize, Qt, QSettings
from PySide6.QtGui import QIcon, QCursor, QFont
from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, \
    QSpacerItem

from core.instance_manager import add_instance_controls
from core.ui_functions import UIFunctions
from gui.generated.instance_page import Ui_InstancePage


def handle_button_click(main_window, btn):
    """
    Handle the button click events.

    :param main_window: The instance of the main window to access widgets.
    :param btn: The QPushButton that was clicked.
    """
    btnName = btn.objectName()

    # SHOW HOME PAGE
    if btnName == "btn_home":
        main_window.widgets.stackedWidget.setCurrentWidget(main_window.widgets.home)
        UIFunctions.resetStyle(main_window, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    # SHOW CUSTOM TASKS PAGE
    if btnName == "btn_custom_task":
            main_window.widgets.stackedWidget.setCurrentWidget(main_window.widgets.custom_tasks)
            UIFunctions.resetStyle(main_window, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    # SHOW COLLECTIVE PAGE
    if btnName == "btn_coordinate_manager":
        main_window.widgets.stackedWidget.setCurrentWidget(main_window.widgets.coordinate_manager)
        UIFunctions.resetStyle(main_window, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    # SHOW BOT MANAGER PAGE
    elif btnName == "btn_bot_manager":
        main_window.widgets.stackedWidget.setCurrentWidget(main_window.widgets.bot_manager)  # SET PAGE
        UIFunctions.resetStyle(main_window, btnName)  # RESET ANOTHERS BUTTONS SELECTED
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

    # CALL ADD INSTANCE FUNCTION
    elif btnName == "btn_add":
        # Call function to add a new dynamic button
        add_new_menu_button(main_window)

    # CALL LOGOUT FUNCTION
    elif btnName == "btn_logout":
        # Call function to add a new dynamic button
        logout(main_window)

    # SHOW EMULATOR PAGE
    elif btnName.startswith("btn_emu_"):
        # Extract the number from the button name
        num = btnName.split("_")[-1]  # Get the last part after the last underscore
        page_name = f"page_emu_{num}"  # Create the corresponding page name

        # Find the page by object name
        page = getattr(main_window.widgets, page_name)
        # page = main_window.findChild(QWidget, page_name)


        if page:
            # Set the corresponding page in the stackedWidget
            main_window.widgets.stackedWidget.setCurrentWidget(page)

        # main_window.widgets.stackedWidget.setCurrentWidget(main_window.widgets.widgets)
        UIFunctions.resetStyle(main_window, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



def connect_buttons(main_window):
    """
    Connect buttons directly to the `handle_button_click` function.
    :param main_window: The instance of the main window to access widgets.
    """
    main_window.widgets.btn_home.clicked.connect(lambda: handle_button_click(main_window, main_window.widgets.btn_home))
    main_window.widgets.btn_custom_task.clicked.connect(lambda: handle_button_click(main_window, main_window.widgets.btn_custom_task))
    main_window.widgets.btn_coordinate_manager.clicked.connect(
        lambda: handle_button_click(main_window, main_window.widgets.btn_coordinate_manager))
    main_window.widgets.btn_add.clicked.connect(lambda: handle_button_click(main_window, main_window.widgets.btn_add))
    main_window.widgets.btn_bot_manager.clicked.connect(lambda: handle_button_click(main_window, main_window.widgets.btn_bot_manager))
    main_window.widgets.btn_logout.clicked.connect(lambda: handle_button_click(main_window, main_window.widgets.btn_logout))

def logout(main_window):
    settings = QSettings("TaskEnforceX", "TaskEX")
    settings.setValue("logged_in", False)
    sys.exit()


def add_new_menu_button(main_window,selection = True):
    """
    Add a new menu button dynamically with a specific stylesheet.
    :param main_window: The instance of the main window to access widgets.
    """
    # Get the next index for adding the instance
    next_index = get_next_btn_emu_number(main_window)

    # Create a new QPushButton
    new_button = QPushButton(f"Emulator {next_index}", main_window)
    new_button.setObjectName(f"btn_emu_{next_index}")

    # Set size policy
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    sizePolicy.setHeightForWidth(new_button.sizePolicy().hasHeightForWidth())
    new_button.setSizePolicy(sizePolicy)

    # Set minimum size
    new_button.setMinimumSize(QSize(0, 45))

    # Set font (assuming `font` is already defined)
    font = QFont()
    font.setFamily("Segoe UI")  # Adjust to your application's font if different
    font.setPointSize(10)
    new_button.setFont(font)

    # Set cursor
    new_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    # Set layout direction
    new_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

    # Set stylesheet with background image from resource pack
    new_button.setStyleSheet("background-image: url(:/icons/images/icons/cil-gamepad.png);")

    # Insert the new button before the 'new' button
    layout = main_window.widgets.topMenu.layout()  # topMenu is the container for buttons
    layout.insertWidget(layout.indexOf(main_window.widgets.btn_add), new_button)

    # Connect the new button to a click handler
    new_button.clicked.connect(lambda: handle_button_click(main_window, new_button))

    # Setup a new instance page
    add_new_instance_page(main_window,next_index)

    # Simulate a button click to trigger the event
    new_button.click()
    if not selection:
        UIFunctions.resetStyle(main_window, '')

    add_instance_controls(main_window,next_index)

def add_new_instance_page(main_window,index):

    # Create a new page for the stackedWidget
    new_page = QWidget()
    new_page.setObjectName(f"page_emu_{index}")

    # Initialize the instance page UI and set it up for the new_page
    instance_ui = Ui_InstancePage()
    instance_ui.setupUi(new_page)

    # Add the new page to the stackedWidget
    main_window.widgets.stackedWidget.addWidget(new_page)

    # Register dynamically created widgets to main_window.widgets
    setattr(main_window.widgets, new_page.objectName(), new_page)

    # Loop through all the attributes in instance_ui that are widgets and update the object name
    for attr_name in dir(instance_ui):
        # Ignore special methods and attributes
        if not attr_name.startswith('__'):
            widget = getattr(instance_ui, attr_name)
            # Check if it's a QWidget with objectName
            if hasattr(widget, 'objectName'):
                # Only update names that end with '_'
                if widget.objectName().endswith('_'):
                    # print(widget.objectName())
                    new_name = f"{widget.objectName()}{index}"
                    widget.setObjectName(new_name)
                    # Register the renamed widget
                    setattr(main_window, new_name, widget)
    getattr(main_window,f"label_{index}").setText(f"New Instance Page {index}")


def initialize_instances(main_window, num_instances):
    """
    Initialize a specified number of emulator instances upon loading.

    :param main_window: The instance of the main window to access widgets.
    :param num_instances: The number of instances to initialize.
    :param selection: The menu needs to be selected or not.
    """
    for _ in range(num_instances):
        add_new_menu_button(main_window,False)

# Function to find the next number for btn_emu_ buttons
def get_next_btn_emu_number(main_window):
    max_number = 0
    layout = main_window.widgets.topMenu.layout()
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget and widget.objectName().startswith("btn_emu_"):
            try:
                # Extract the number from the object name
                number = int(widget.objectName().split("_")[-1])
                max_number = max(max_number, number)
            except ValueError:
                pass  # Ignore buttons that don't have a number

    return max_number + 1