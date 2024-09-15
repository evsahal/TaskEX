from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QFrame

from core.custom_widgets.FlowLayout import FlowLayout
from core.custom_widgets.QCheckComboBox import QCheckComboBox
from db.db_setup import get_session
from db.models import General
from gui.widgets.GeneralProfileWidget import GeneralProfileWidget


def init_scan_general_ui(main_window):

    # Set up scan type
    # Create a vertical layout for the frame
    frame_layout = QVBoxLayout()

    # Create an instance of the custom QCheckComboBox
    cb = QCheckComboBox(placeholderText="Scan Type")
    cb.setMinimumWidth(180)
    cb.setMinimumHeight(45)
    # model = cb.model()
    cb.addItem("Epic Historic")
    cb.setItemCheckState(0, Qt.Unchecked)
    cb.addItem("Legendary Historic")
    cb.setItemCheckState(1, Qt.Unchecked)
    # cb.show()
    # cb.raise_()

    # Add the MultiSelectComboBox to the frame layout
    frame_layout.addWidget(cb)
    frame_layout.setContentsMargins(0, frame_layout.contentsMargins().top(), 0, frame_layout.contentsMargins().bottom())

    # Set the layout to the sg_scan_type frame
    getattr(main_window.widgets, f"sg_scan_type").setFrameShape(QFrame.NoFrame)
    getattr(main_window.widgets, f"sg_scan_type").setLayout(frame_layout)

    # Set up scan filter
    # Create a vertical layout for the frame
    frame_layout = QVBoxLayout()

    # Create an instance of the custom QCheckComboBox
    cb = QCheckComboBox(placeholderText="Scan Filter")
    cb.setMinimumWidth(130)
    cb.setMinimumHeight(45)
    # model = cb.model()
    cb.addItem("Favorite")
    cb.setItemCheckState(0, Qt.Unchecked)
    cb.addItem("Idle")
    cb.setItemCheckState(1, Qt.Unchecked)
    # cb.show()
    # cb.raise_()

    # Add the MultiSelectComboBox to the frame layout
    frame_layout.addWidget(cb)
    frame_layout.setContentsMargins(0, frame_layout.contentsMargins().top(), 0, frame_layout.contentsMargins().bottom())

    # Set the layout to the sg_scan_type frame
    getattr(main_window.widgets, f"sg_scan_filter").setFrameShape(QFrame.NoFrame)
    getattr(main_window.widgets, f"sg_scan_filter").setLayout(frame_layout)

    # Set up the Layout for generals
    generals_list_frame = getattr(main_window.widgets, "generals_list_frame")

    # Use the existing generals_list_frame as the container
    flow_layout = FlowLayout(generals_list_frame)
    flow_layout.setObjectName("generals_list_flow_layout")
    setattr(main_window.widgets, flow_layout.objectName(), flow_layout)

    # Set the flow layout to the container frame (generals_list_frame)
    generals_list_frame.setLayout(flow_layout)

    # Create and add multiple frames in a loop
    # for i in range(40):  # Adjust the number of frames as needed
    #     frame = QFrame()
    #     frame.setFixedSize(200, 200)  # Set the size (width, height)
    #     frame.setStyleSheet(f"background-color: rgb({i * 5}, 0, 0);")
    #     flow_layout.addWidget(frame)

    # Load Existing Generals
    session = get_session()

    # Query all records from the generals table
    generals = session.query(General).all()
    session.close()

    # Get the project root directory dynamically
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    # print(PROJECT_ROOT)

    # Pass the data to add the widgets
    for general in generals:
        widget = GeneralProfileWidget(flow_layout=getattr(main_window.widgets, f"generals_list_flow_layout"),data= general,root_path=PROJECT_ROOT)
        # Connect the signals
        widget.ui.edit_general.scan_console.connect(lambda message: update_scan_console(main_window, message))
        widget.scan_console.connect(lambda message: update_scan_console(main_window, message))

        # Set the size of the widget to its size hint
        widget.setFixedSize(widget.sizeHint())
        flow_layout.addWidget(widget)


def update_scan_console(main_window,message):
    main_window.widgets.scan_general_console.appendPlainText(message)