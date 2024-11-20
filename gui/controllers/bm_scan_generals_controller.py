import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QFrame, QLabel, QHBoxLayout, QWidget

from core.custom_widgets.FlowLayout import FlowLayout
from core.custom_widgets.QCheckComboBox import QCheckComboBox
from core.custom_widgets.QToggle import QToggle
from db.db_setup import get_session
from db.models import General
from gui.widgets.GeneralProfileWidget import GeneralProfileWidget
from gui.widgets.GeneralsSelectionDialog import GeneralsSelectionDialog


def init_scan_general_ui(main_window):

    # Connect Manage General Presets Button
    getattr(main_window.widgets, "general_preset_btn").clicked.connect(lambda: open_manage_general_presets_dialog(main_window))

    # Set up view toggle
    toggle_layout = QHBoxLayout(main_window.widgets.toggle_general_view_frame)
    main_window.widgets.toggle_general_view_frame.setContentsMargins(0, 0, 0, 0)

    # Create a new frame to contain the toggle label
    toggle_label_frame = QFrame()
    toggle_label_layout = QHBoxLayout(toggle_label_frame)
    toggle_label_layout.setContentsMargins(0, 0, 0, 5)  # Set bottom margin only

    # Create the toggle label inside the new frame
    toggle_label = QLabel("Details View ")
    toggle_label.setObjectName("toggle_label")
    setattr(main_window.widgets, toggle_label.objectName(), toggle_label)
    toggle_label_layout.addWidget(toggle_label)

    # Add the toggle label frame to the main layout
    toggle_layout.addWidget(toggle_label_frame)


    # Create an instance of QToggle
    toggle_general_view = QToggle()
    toggle_general_view.setObjectName("toggle_general_view")
    setattr(main_window.widgets, toggle_general_view.objectName(), toggle_general_view)
    toggle_general_view.toggled.connect(lambda checked: change_general_ui_view(main_window,checked))

    # Add the QToggle button to the frame's layout
    toggle_layout.addWidget(toggle_general_view)


    # Set up the Layout for generals
    generals_list_frame = main_window.widgets.generals_list_frame

    # Use the existing generals_list_frame as the container
    flow_layout = FlowLayout(generals_list_frame)
    flow_layout.setObjectName("generals_list_flow_layout")
    setattr(main_window.widgets, flow_layout.objectName(), flow_layout)

    # Set the flow layout to the container frame (generals_list_frame)
    generals_list_frame.setLayout(flow_layout)

    # Load Existing Generals
    session = get_session()

    # Query all records from the generals table
    generals = session.query(General).all()
    session.close()

    # Pass the data to add the widgets
    for general in generals:
        add_general_to_frame(main_window,general)

def open_manage_general_presets_dialog(main_window):
    general_selection_dialog = GeneralsSelectionDialog(main_window)
    session = get_session()
    all_generals = General.get_all_valid_general_names(session)
    for gen in all_generals:
        print(gen)
    general_selection_dialog.all_generals_main.addItems(all_generals)
    general_selection_dialog.show()


def add_general_to_frame(main_window,general):
    flow_layout = main_window.widgets.generals_list_flow_layout
    toggle = getattr(main_window.widgets, "toggle_general_view").isChecked()
    widget = GeneralProfileWidget(flow_layout=flow_layout,toggle= toggle, data=general)
    setattr(main_window.widgets, widget.objectName(), widget)
    # print(widget.objectName())
    # Connect the signals
    widget.ui.edit_general.scan_console.connect(lambda message: update_scan_console(main_window, message))
    widget.update_data.connect(lambda general_obj: update_scan_general_data(main_window,general_obj))
    widget.update_view.connect(lambda general_id,checked: update_scan_general_view(main_window,general_id,checked))
    widget.scan_console.connect(lambda message: update_scan_console(main_window, message))

    # Set the size of the widget to its size hint
    widget.setFixedSize(widget.sizeHint())

    flow_layout.addWidget(widget)

def change_general_ui_view(main_window,checked):
    label = main_window.widgets.toggle_label
    label.setText("List View " if label.text() == "Details View " else "Details View ")

    generals_list_frame = main_window.widgets.generals_list_frame

    # Regex pattern to match 'general_profile_{i}' where i is any number
    pattern = re.compile(r"^general_profile_\d+$")
    # Loop through all children and filter those with names 'general_profile'
    for child in generals_list_frame.findChildren(QWidget):
        if pattern.match(child.objectName()):
            if checked:
                child.switch_view(checked=True)
            else:
                child.switch_view()

def update_scan_general_view(main_window,general_id,checked):
    getattr(main_window.widgets, f"general_profile_{general_id}").switch_view(checked)


def update_scan_general_data(main_window,general):
    session = get_session()
    general = session.merge(general)
    getattr(main_window.widgets, f"general_profile_{general.id}").data = general
    session.close()

def update_scan_console(main_window,message):
    main_window.widgets.scan_general_console.appendPlainText(message)