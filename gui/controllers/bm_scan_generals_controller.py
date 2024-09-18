import re
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QFrame, QLabel, QHBoxLayout, QWidget

from core.custom_widgets.FlowLayout import FlowLayout
from core.custom_widgets.QCheckComboBox import QCheckComboBox
from core.custom_widgets.QToggle import QToggle
from db.db_setup import get_session
from db.models import General
from gui.widgets.GeneralProfileWidget import GeneralProfileWidget


def init_scan_general_ui(main_window):

    # Set up scan type
    # Create a vertical layout for the frame
    frame_layout = QVBoxLayout()

    # Create an instance of the custom QCheckComboBox
    cb = QCheckComboBox(placeholderText="Scan Type")
    cb.setObjectName("scan_generals_type")
    setattr(main_window.widgets, cb.objectName(), cb)
    cb.setMinimumWidth(180)
    cb.setMinimumHeight(45)
    # model = cb.model()
    cb.addItem("Epic Historic")
    cb.setItemCheckState(0, Qt.Unchecked)
    cb.addItem("Legendary Historic")
    cb.setItemCheckState(1, Qt.Unchecked)

    # Add the MultiSelectComboBox to the frame layout
    frame_layout.addWidget(cb)
    frame_layout.setContentsMargins(0, frame_layout.contentsMargins().top(), 0, frame_layout.contentsMargins().bottom())

    # Set the layout to the sg_scan_type frame
    main_window.widgets.sg_scan_type.setFrameShape(QFrame.NoFrame)
    main_window.widgets.sg_scan_type.setLayout(frame_layout)

    # Set up scan filter
    # Create a vertical layout for the frame
    frame_layout = QVBoxLayout()

    # Create an instance of the custom QCheckComboBox
    cb = QCheckComboBox(placeholderText="Scan Filter")
    cb.setObjectName("scan_generals_filter")
    setattr(main_window.widgets, cb.objectName(), cb)
    cb.setMinimumWidth(130)
    cb.setMinimumHeight(45)
    # model = cb.model()
    cb.addItem("Favorite")
    cb.setItemCheckState(0, Qt.Unchecked)
    cb.addItem("Idle")
    cb.setItemCheckState(1, Qt.Unchecked)


    # Add the MultiSelectComboBox to the frame layout
    frame_layout.addWidget(cb)
    frame_layout.setContentsMargins(0, frame_layout.contentsMargins().top(), 0, frame_layout.contentsMargins().bottom())

    # Set the layout to the sg_scan_type frame
    main_window.widgets.sg_scan_filter.setFrameShape(QFrame.NoFrame)
    main_window.widgets.sg_scan_filter.setLayout(frame_layout)


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


def add_general_to_frame(main_window,general):
    flow_layout = main_window.widgets.generals_list_flow_layout
    widget = GeneralProfileWidget(flow_layout=flow_layout, data=general)
    # Connect the signals
    widget.ui.edit_general.scan_console.connect(lambda message: update_scan_console(main_window, message))
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

def update_scan_console(main_window,message):
    main_window.widgets.scan_general_console.appendPlainText(message)