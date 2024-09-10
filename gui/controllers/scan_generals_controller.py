from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout

from core.custom_widgets.QCheckComboBox import QCheckComboBox


def init_scan_general_ui(main_window):

    # Set up scan type
    scan_type_f = getattr(main_window.widgets, f"sg_scan_type")
    # scan_type_f.setContentsMargins(0, 0, 0, 0)
    # scan_type_f.setStyleSheet("border: 1px solid red;")

    # Create a vertical layout for the frame
    frame_layout = QVBoxLayout()

    # Create an instance of the custom QCheckComboBox
    cb = QCheckComboBox(placeholderText="Scan Type")
    cb.setMinimumWidth(180)
    cb.setMinimumHeight(45)
    model = cb.model()
    cb.addItem("Epic Historic")
    cb.setItemCheckState(0, Qt.Unchecked)
    cb.addItem("Legendary Historic")
    cb.setItemCheckState(1, Qt.Unchecked)
    cb.show()
    cb.raise_()

    # Add the MultiSelectComboBox to the frame layout
    frame_layout.addWidget(cb)

    # Set the layout to the sg_scan_type frame
    scan_type_f.setLayout(frame_layout)

    # Set up scan filter
    scan_filter_f = getattr(main_window.widgets, f"sg_scan_filter")
    # scan_filter_f.setContentsMargins(0, 0, 0, 0)
    # scan_filter_f.setStyleSheet("border: 1px solid red;")

    # Create a vertical layout for the frame
    frame_layout = QVBoxLayout()

    # Create an instance of the custom QCheckComboBox
    cb = QCheckComboBox(placeholderText="Scan Filter")
    cb.setMinimumWidth(130)
    cb.setMinimumHeight(45)
    model = cb.model()
    cb.addItem("Favorite")
    cb.setItemCheckState(0, Qt.Unchecked)
    cb.addItem("Idle")
    cb.setItemCheckState(1, Qt.Unchecked)
    cb.show()
    cb.raise_()

    # Add the MultiSelectComboBox to the frame layout
    frame_layout.addWidget(cb)

    # Set the layout to the sg_scan_type frame
    scan_filter_f.setLayout(frame_layout)