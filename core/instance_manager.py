from zoneinfo import available_timezones

import psutil
from PySide6 import QtCore
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QPushButton, QToolTip, QApplication, QWidget, QVBoxLayout, \
    QLineEdit, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QSize

from core.controllers.emulator_controller import handle_run_button, sync_lineedits


def add_instance_controls(main_window,index):
    """
    Function to add instance controls with additional widgets: QLineEdit, Play button, and Delete button.
    This function appends these widgets to the extraCenterArea's content widget (scrollAreaWidgetContents_2).
    """

    # Get the scroll area and its content widget
    scroll_area = main_window.widgets.extraCenterArea  # This is the QScrollArea
    content_widget = scroll_area.findChild(QWidget, "extraCenterAreaWidgetContents")  # Find the content widget by object name

    # Ensure the content widget has a layout
    if content_widget.layout() is None:
        content_layout = QVBoxLayout()
        content_widget.setLayout(content_layout)
    else:
        content_layout = content_widget.layout()

    # Set the alignment of the layout to the top
    content_layout.setAlignment(Qt.Alignment.AlignTop)

    # 2. Create a QLineEdit for emulator name
    emu_line_edit = QLineEdit()
    emu_line_edit.setObjectName(f"im_emu_name_{index}")
    emu_line_edit.setPlaceholderText(f"Emulator {index}")
    emu_line_edit.setFixedHeight(39)
    emu_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    setattr(main_window.widgets, emu_line_edit.objectName(), emu_line_edit)
    # print(emu_line_edit.objectName())
    # Sync instance manager emulator name and run tab emulator name
    sync_lineedits(emu_line_edit, getattr(main_window.widgets, f"emu_name_{index}"),getattr(main_window.widgets, f"btn_emu_{index}"))

    # Set default emulator name
    emu_line_edit.setText(f"Emulator {index}")

    # 2. Create a QLineEdit for port number
    port_line_edit = QLineEdit()
    port_line_edit.setObjectName(f"im_emu_port_{index}")
    port_line_edit.setPlaceholderText("Port No.")
    port_line_edit.setFixedHeight(39)
    port_line_edit.setFixedWidth(80)
    port_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    setattr(main_window.widgets, port_line_edit.objectName(), port_line_edit)

    # Sync instance manager emulator port and run tab emulator port
    sync_lineedits(port_line_edit, getattr(main_window.widgets, f"emu_port_{index}"))

    # 3. Create a "Play" button with a run icon
    play_button = QPushButton()
    play_button.setObjectName(f"im_run_btn_{index}")
    play_button.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))  # Replace with actual path to run icon
    play_button.setToolTip("Run")
    play_button.setFixedSize(39, 39)  # Set fixed size for the play button
    play_button.setStyleSheet("""QPushButton{	border-radius: 5px;	border: 2px solid rgb(33, 37, 43);}
    QPushButton:hover { background-color: rgb(57, 65, 80); }
    QPushButton:pressed {	background-color: rgb(35, 40, 49); 	border: 2px solid rgb(43, 50, 61); }
    """)
    setattr(main_window.widgets, play_button.objectName(), play_button)

    play_button.clicked.connect(lambda: handle_run_button(main_window, index))

    # Create a widget container to hold these elements horizontally
    widget_container = QWidget()
    widget_container.setObjectName(f"im_widget_{index}")
    layout = QHBoxLayout(widget_container)
    setattr(main_window.widgets, widget_container.objectName(), widget_container)

    layout.addWidget(emu_line_edit)
    layout.addWidget(port_line_edit)
    layout.addWidget(play_button)
    layout.setContentsMargins(0, 0, 0, 0)  # No margins for a compact look
    layout.setSpacing(5)  # Optional: Set spacing between widgets for better layout

    # Add the widget container to the content layout of the scroll area
    content_layout.addWidget(widget_container)

    # Update the content widget size and the scroll area
    content_widget.adjustSize()
    scroll_area.update()

def setup_port_display_table(main_window):
    # Reference to the table
    table = main_window.widgets.port_display_table

    table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

    # Set column headers
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["Emulator Name", "Port No.", ""])

    # Create a reload icon item for the 'Actions' header
    reload_icon = QIcon(":/icons/images/icons/cil-reload.png")
    reload_header_item = QTableWidgetItem()
    reload_header_item.setIcon(reload_icon)
    table.setHorizontalHeaderItem(2, reload_header_item)

    # Connect the header click to the reload function
    table.horizontalHeader().sectionClicked.connect(lambda index: reload_ports(main_window) if index == 2 else None)

    # Resize columns
    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)

    # Adjust alignment for the other columns if needed
    table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
    table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignCenter)

def reload_ports(main_window):
    # Implement the logic to refresh/reload the open ports for the emulators
    # print("Reloading ports...")
    table = main_window.widgets.port_display_table
    table.setRowCount(0)  # Clear existing rows
    get_available_ports(main_window)  # Repopulate table with updated data

def add_row_to_port_display_table(main_window, emulator_type, port_number):
    table = main_window.widgets.port_display_table
    row_count = table.rowCount()
    table.insertRow(row_count)

    # Set Emulator Name (leave as is, no centering)
    table.setItem(row_count, 0, QTableWidgetItem(emulator_type))

    # Set Port Number and center-align it
    port_item = QTableWidgetItem(str(port_number))
    port_item.setTextAlignment(Qt.AlignCenter)
    table.setItem(row_count, 1, port_item)

    # Add Copy button in Actions column and center-align it
    copy_button = QPushButton()
    # copy_button.setIcon(QIcon(":/icons/images/icons/cil-task.png"))  # Replace with the actual path to your copy icon
    copy_button.setToolTip("Copy")

    copy_button.setIcon(QIcon.fromTheme("edit-copy"))
    copy_button.setStyleSheet("border: none;background-color: transparent;")
    # Create a QWidget to hold the button and set a layout to center it
    button_container = QWidget()
    button_layout = QVBoxLayout(button_container)
    button_layout.addWidget(copy_button)
    button_layout.setAlignment(Qt.AlignCenter)  # Align the button to the center
    button_layout.setContentsMargins(0, 0, 0, 0)  # Remove any margins

    table.setCellWidget(row_count, 2, button_container)

    # Connect the copy button to the clipboard function
    copy_button.clicked.connect(lambda: copy_port_number_to_clipboard(port_number))

def copy_port_number_to_clipboard(port_number):
    clipboard = QApplication.clipboard()
    clipboard.setText(str(port_number))
    QToolTip.showText(QCursor.pos(), "Copied!")

def get_available_ports(main_window):
    # Search for all the available ports for Bluestacks and Memu
    available_ports = find_emulator_ports()
    for emulator_type, port_number in available_ports:
        # print(f"Emulator Type: {emulator_type}, Port Number: {port_number}")
        add_row_to_port_display_table(main_window, emulator_type, port_number)

def find_emulator_ports():
    emulator_ports = []

    # Define known emulator process names
    emulator_process_names = ['MEmu', 'HD-Player']
    emulator_player_names ={'HD-Player.exe':'Bluestacks','MEmuHyper.exe':'MEmu'}

    # Iterate over all network connections
    for conn in psutil.net_connections(kind='inet'):
        pid = conn.pid
        if pid is not None:
            try:
                process = psutil.Process(pid)
                process_name = process.name()

                # Check if the process is an emulator
                if any(emulator_name.lower() in process_name.lower() for emulator_name in emulator_process_names):
                    # Check the connection conditions
                    local_port = conn.laddr.port
                    remote_address = conn.raddr.ip if conn.raddr else '0.0.0.0'
                    if local_port < 26000 and local_port != 21501 and remote_address == '0.0.0.0':
                        emulator_ports.append((emulator_player_names[process_name], local_port))

            except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
                continue

    return emulator_ports