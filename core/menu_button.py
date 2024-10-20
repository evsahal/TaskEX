import sys
from operator import indexOf
from turtledemo.sorting_animate import ssort

from PySide6.QtCore import QSize, Qt, QSettings
from PySide6.QtGui import QIcon, QCursor, QFont, QPalette
from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, \
    QSpacerItem, QMessageBox

from core.controllers.emulator_controller import handle_run_button
from core.instance_manager import add_instance_controls
from core.ui_functions import UIFunctions
from gui.controllers.run_tab_controller import setup_scheduler_table, init_icons
from gui.generated.instance_page import Ui_InstancePage
from utils.dialog_utils import show_error_dialog, show_confirmation_dialog
from utils.helper_utils import extract_number_from_string


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
    if btnName == "btn_task_manager":
            main_window.widgets.stackedWidget.setCurrentWidget(main_window.widgets.task_manager)
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
    main_window.widgets.btn_task_manager.clicked.connect(lambda: handle_button_click(main_window, main_window.widgets.btn_task_manager))
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

    setattr(main_window.widgets, new_button.objectName(), new_button)

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
                    setattr(main_window.widgets, new_name, widget)
    # getattr(main_window,f"label_{index}").setText(f"New Instance Page {index}")


    # Connect run button
    getattr(main_window.widgets, f"run_btn_{index}").clicked.connect(lambda: handle_run_button(main_window, index))

    # Connect delete instance button
    getattr(main_window.widgets, f"delete_instance_{index}").clicked.connect(lambda :delete_instance_check(main_window,index))

    # Setup Icons for Buttons
    # init_icons(main_window,index)

    # Setup Scheduler table UI
    setup_scheduler_table(main_window,index)

def delete_instance_check(main_window,index):
    total_instance = count_btn_emu_instances(main_window)
    if total_instance == 1:
        # print("Dont allow to delete")
        show_error_dialog(main_window, "Error", "Last instance can't be deleted.")
    else:
        if show_confirmation_dialog(main_window,"confirm","Are you sure you want to delete this instance?"):
            delete_instance(main_window,index)

def delete_instance(main_window,index):

    # Remove the emulator button from the menu
    remove_widget(getattr(main_window.widgets, f"btn_emu_{index}"))

    # Remove emulator name, port, and run button from instance manager
    remove_widget(getattr(main_window.widgets, f"im_widget_{index}"))

    # Remove the instance page from the stacked widget
    remove_widget(getattr(main_window.widgets, f"page_emu_{index}"))

    # Select the Menu button
    current_page = main_window.widgets.stackedWidget.currentWidget()

    if current_page:
        # Get the object name of the current page
        current_page_index = extract_number_from_string(current_page.objectName())
        # print(current_page_index)
        getattr(main_window.widgets, f"btn_emu_{current_page_index}").click()

    # print(f"Emulator instance {index} deleted.")

def remove_widget(widget):
    """
    Removes the given widget from its parent layout and calls deleteLater
    to free up memory.

    Args:
        widget (QWidget): The widget to be removed and deleted.
    """
    if widget is not None:
        # Remove the widget from its parent layout, if it exists
        parent_layout = widget.parentWidget().layout() if widget.parentWidget() else None
        if parent_layout:
            parent_layout.removeWidget(widget)

        # Delete the widget safely
        widget.setParent(None)  # Unset parent so it's no longer managed by the layout
        widget.deleteLater()    # Schedules the object for deletion
        # print(f"Widget {widget.objectName()} removed.")
    else:
        # print("Widget is None, nothing to remove.")
        pass

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

def count_btn_emu_instances(main_window):
    """
    Counts the number of instances where the button object name starts with 'btn_emu_'.

    Args:
        main_window: The main window object containing the widgets.

    Returns:
        int: The number of buttons with object names that start with 'btn_emu_'.
    """
    count = 0
    layout = main_window.widgets.topMenu.layout()  # Get the layout containing the buttons
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget and widget.objectName().startswith("btn_emu_"):
            count += 1  # Increment the count for each valid btn_emu_ button

    return count