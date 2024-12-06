from PySide6.QtCore import Qt, QItemSelectionModel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QAbstractItemView, \
    QComboBox, QLineEdit, QLabel, QVBoxLayout

from db.db_setup import get_session
from db.models import Profile


def init_run_tab(main_window, index, instance):
    # Setup scheduler table
    setup_scheduler_table(main_window, index)

    # Initialize preset control buttons
    initialize_preset_buttons(main_window, index)

    # Populate the profile combobox
    populate_profile_combo(getattr(main_window.widgets, f"emu_profile_{index}"))

    # Load the emulator data(name,port and profile)
    if instance:
        load_instance_data(main_window,instance,index)


def populate_profile_combo(combobox):
    session = get_session()
    try:
        # Query all profiles from the database
        profiles = session.query(Profile).all()

        # Add profiles to the combobox
        for profile in profiles:
            combobox.addItem(profile.name, profile.id)

    finally:
        # Close the session to avoid connection leaks
        session.close()

def load_instance_data(main_window,instance,index ):

    # Select the profile
    profile_combobox = getattr(main_window.widgets, f"emu_profile_{index}")
    for i in range(profile_combobox.count()):
        # Get the user data (profile_id) of the current item
        item_data = profile_combobox.itemData(i)
        if item_data == instance.profile_id:
            # Set the combobox index to the matching item
            profile_combobox.setCurrentIndex(i)

    # Set the emulator name
    emulator_name_ledit = getattr(main_window.widgets, f"emu_name_{index}")
    # print(f"Instance Name: {instance.emulator_name}")
    emulator_name_ledit.setText(instance.emulator_name if instance.emulator_name else f"Emulator {index}")

    # Set emulator port
    emulator_port_ledit = getattr(main_window.widgets, f"emu_port_{index}")
    emulator_port_ledit.setText(str(instance.emulator_port) if instance.emulator_port else "")




def setup_scheduler_table(main_window, index):
    # Accessing the scheduler table
    scheduler_table = getattr(main_window.widgets, f"scheduler_table_{index}")

    # Set the selection mode to Single Selection for selecting individual cells
    scheduler_table.setSelectionMode(QAbstractItemView.SingleSelection)
    # scheduler_table.setSelectionBehavior(QAbstractItemView.SelectItems)  # Allow selecting individual cells
    scheduler_table.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Enable drag and drop for internal reordering
    scheduler_table.setDragEnabled(True)
    scheduler_table.setAcceptDrops(True)
    scheduler_table.setDragDropMode(QAbstractItemView.InternalMove)  # Allows row reordering
    scheduler_table.setDefaultDropAction(Qt.MoveAction)

    scheduler_table.itemSelectionChanged.connect(lambda: selected_scheduler_task(main_window, index))

    # Hide the vertical header (row numbers)
    scheduler_table.verticalHeader().setVisible(False)

    # Stretch the first column
    scheduler_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    # Align the last column (Actions) to the right, with a fixed size or interactive resizing
    scheduler_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

    # Set the height of the horizontal header
    scheduler_table.horizontalHeader().setFixedHeight(45)

    # Add the footer row with "Add Task" and "Save Tasks" buttons
    add_footer(main_window, index)


def initialize_preset_buttons(main_window, index):
    # Access preset control buttons and combo box
    preset_edit_btn = getattr(main_window.widgets, f"preset_edit_btn_{index}")
    preset_delete_btn = getattr(main_window.widgets, f"preset_delete_btn_{index}")
    preset_add_btn = getattr(main_window.widgets, f"preset_add_btn_{index}")

    # Initialize event connections
    preset_edit_btn.clicked.connect(lambda: enable_edit_mode(main_window, index))
    preset_delete_btn.clicked.connect(lambda: delete_preset(main_window, index))
    preset_add_btn.clicked.connect(lambda: enable_new_preset_mode(main_window, index))


def enable_edit_mode(main_window, index):
    # Access the combo box and preset widget
    preset_widget = getattr(main_window.widgets, f"preset_widget_{index}")
    preset_combo = getattr(main_window.widgets, f"preset_combo_{index}")
    preset_edit_btn = getattr(main_window.widgets, f"preset_edit_btn_{index}")
    preset_delete_btn = getattr(main_window.widgets, f"preset_delete_btn_{index}")
    preset_add_btn = getattr(main_window.widgets, f"preset_add_btn_{index}")

    # Create a line edit and set the current preset name as text
    preset_line_edit = QLineEdit()
    preset_line_edit.setFixedHeight(45)
    preset_line_edit.setText(preset_combo.currentText())
    preset_line_edit.setObjectName(f"preset_name_lineedit_{index}")

    # Create save and cancel buttons
    save_button = QPushButton()
    save_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
    save_button.setFixedSize(45, 45)
    save_button.setObjectName(f"preset_name_save_btn_{index}")

    cancel_button = QPushButton()
    cancel_button.setIcon(QIcon(":/icons/images/icons/cil-x.png"))
    cancel_button.setFixedSize(45, 45)
    cancel_button.setObjectName(f"preset_name_cancel_btn_{index}")

    # Define save and cancel button actions
    save_button.clicked.connect(lambda: save_preset_name(main_window, index, preset_line_edit))
    cancel_button.clicked.connect(lambda: cancel_edit_mode(main_window, index, preset_combo, preset_line_edit))

    # Access or create the layout in the preset widget
    if preset_widget.layout() is None:
        layout = QHBoxLayout(preset_widget)
        preset_widget.setLayout(layout)
    else:
        layout = preset_widget.layout()

    # Hide the combo box and preset control buttons temporarily
    preset_combo.hide()
    preset_edit_btn.hide()
    preset_delete_btn.hide()
    preset_add_btn.hide()

    # Add the line edit, save, and cancel buttons to the layout
    layout.addWidget(preset_line_edit)
    layout.addWidget(save_button)
    layout.addWidget(cancel_button)

    # Store them in the main_window as attributes with unique names
    setattr(main_window, preset_line_edit.objectName(), preset_line_edit)
    setattr(main_window, save_button.objectName(), save_button)
    setattr(main_window, cancel_button.objectName(), cancel_button)


def save_preset_name(main_window, index, preset_line_edit):
    preset_combo = getattr(main_window.widgets, f"preset_combo_{index}")
    new_name = preset_line_edit.text()
    # Update combo box with the new name
    current_index = preset_combo.currentIndex()
    preset_combo.setItemText(current_index, new_name)

    # Remove the line edit and save/cancel buttons
    remove_preset_edit_widgets(main_window, index)

    # Show the combo box and preset control buttons again
    preset_combo.show()
    getattr(main_window.widgets, f"preset_edit_btn_{index}").show()
    getattr(main_window.widgets, f"preset_delete_btn_{index}").show()
    getattr(main_window.widgets, f"preset_add_btn_{index}").show()


def cancel_edit_mode(main_window, index, preset_combo, preset_line_edit):
    # Remove the line edit and save/cancel buttons
    remove_preset_edit_widgets(main_window, index)

    # Show the combo box and preset control buttons again
    preset_combo.show()
    getattr(main_window.widgets, f"preset_edit_btn_{index}").show()
    getattr(main_window.widgets, f"preset_delete_btn_{index}").show()
    getattr(main_window.widgets, f"preset_add_btn_{index}").show()


def remove_preset_edit_widgets(main_window, index):
    # Remove the line edit and save/cancel buttons based on index
    preset_line_edit = getattr(main_window, f"preset_name_lineedit_{index}", None)
    save_button = getattr(main_window, f"preset_name_save_btn_{index}", None)
    cancel_button = getattr(main_window, f"preset_name_cancel_btn_{index}", None)

    if preset_line_edit:
        preset_line_edit.deleteLater()
        delattr(main_window, f"preset_name_lineedit_{index}")

    if save_button:
        save_button.deleteLater()
        delattr(main_window, f"preset_name_save_btn_{index}")

    if cancel_button:
        cancel_button.deleteLater()
        delattr(main_window, f"preset_name_cancel_btn_{index}")


def delete_preset(main_window, index):
    preset_combo = getattr(main_window.widgets, f"preset_combo_{index}")
    current_index = preset_combo.currentIndex()
    if current_index >= 0:
        # Remove the selected preset from the combo box
        preset_combo.removeItem(current_index)


def enable_new_preset_mode(main_window, index):
    # Access the combo box and preset widget
    preset_widget = getattr(main_window.widgets, f"preset_widget_{index}")
    preset_combo = getattr(main_window.widgets, f"preset_combo_{index}")
    preset_edit_btn = getattr(main_window.widgets, f"preset_edit_btn_{index}")
    preset_delete_btn = getattr(main_window.widgets, f"preset_delete_btn_{index}")
    preset_add_btn = getattr(main_window.widgets, f"preset_add_btn_{index}")

    # Create a line edit for entering a new preset name
    preset_line_edit = QLineEdit()
    preset_line_edit.setFixedHeight(45)
    preset_line_edit.setPlaceholderText("Enter New Preset")
    preset_line_edit.setObjectName(f"preset_name_lineedit_{index}")

    # Create save and cancel buttons
    save_button = QPushButton()
    save_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
    save_button.setFixedSize(45, 45)
    save_button.setObjectName(f"preset_name_save_btn_{index}")

    cancel_button = QPushButton()
    cancel_button.setIcon(QIcon(":/icons/images/icons/cil-x.png"))
    cancel_button.setFixedSize(45, 45)
    cancel_button.setObjectName(f"preset_name_cancel_btn_{index}")

    # Define save and cancel button actions for adding a new preset
    save_button.clicked.connect(lambda: add_new_preset_name(main_window, index, preset_line_edit))
    cancel_button.clicked.connect(lambda: cancel_edit_mode(main_window, index, preset_combo, preset_line_edit))

    # Access or create the layout in the preset widget
    if preset_widget.layout() is None:
        layout = QHBoxLayout(preset_widget)
        preset_widget.setLayout(layout)
    else:
        layout = preset_widget.layout()

    # Hide the combo box and preset control buttons temporarily
    preset_combo.hide()
    preset_edit_btn.hide()
    preset_delete_btn.hide()
    preset_add_btn.hide()

    # Add the line edit, save, and cancel buttons to the layout
    layout.addWidget(preset_line_edit)
    layout.addWidget(save_button)
    layout.addWidget(cancel_button)

    # Store these widgets as attributes of the main_window so they can be accessed later
    setattr(main_window, preset_line_edit.objectName(), preset_line_edit)
    setattr(main_window, save_button.objectName(), save_button)
    setattr(main_window, cancel_button.objectName(), cancel_button)


def add_new_preset_name(main_window, index, preset_line_edit):
    preset_combo = getattr(main_window.widgets, f"preset_combo_{index}")
    new_name = preset_line_edit.text()

    if new_name:  # Ensure the name is not empty
        # Add the new name to the combo box
        preset_combo.addItem(new_name)
        preset_combo.setCurrentText(new_name)

    # Remove the line edit and save/cancel buttons
    remove_preset_edit_widgets(main_window, index)

    # Show the combo box and preset control buttons again
    preset_combo.show()
    getattr(main_window.widgets, f"preset_edit_btn_{index}").show()
    getattr(main_window.widgets, f"preset_delete_btn_{index}").show()
    getattr(main_window.widgets, f"preset_add_btn_{index}").show()


def add_footer(main_window, index):
    # Accessing the scheduler table
    scheduler_table = getattr(main_window.widgets, f"scheduler_table_{index}")
    footer_row = scheduler_table.rowCount()
    scheduler_table.insertRow(footer_row)

    scheduler_table.setRowHeight(footer_row, 40)

    # Create the "Add Task" button
    add_task_button = QPushButton("Add New Task")
    add_task_button.setMinimumHeight(45)
    add_task_button.clicked.connect(lambda: add_new_task(main_window, index))

    # Create the "Save Tasks" button
    save_task_button = QPushButton()
    save_task_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
    save_task_button.setFixedSize(40, 45)
    save_task_button.setObjectName(f"scheduler_preset_save_btn_{index}")

    # Add buttons to the footer row
    scheduler_table.setCellWidget(footer_row, 0, add_task_button)
    scheduler_table.setCellWidget(footer_row, 1, save_task_button)

    # Make the action column visible
    scheduler_table.horizontalHeader().setStretchLastSection(False)


def add_new_task(main_window, index):
    scheduler_table = getattr(main_window.widgets, f"scheduler_table_{index}")
    row_position = scheduler_table.rowCount() - 1
    scheduler_table.insertRow(row_position)

    # Task name column (selectable)
    task_item = QTableWidgetItem(f"New Task {row_position}")
    task_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make only the task name column selectable
    scheduler_table.setItem(row_position, 0, task_item)

    # Action column (non-selectable)
    delete_button = QPushButton()
    delete_button.setIcon(QIcon(":/icons/images/icons/icon_delete_3.png"))
    delete_button.setFixedSize(40, 40)
    delete_button.clicked.connect(lambda: remove_task_row(scheduler_table, delete_button))

    scheduler_table.setCellWidget(row_position, 1, delete_button)
    non_selectable_item = QTableWidgetItem()  # Placeholder item to disable selection
    non_selectable_item.setFlags(Qt.ItemIsEnabled)  # Make non-selectable
    scheduler_table.setItem(row_position, 1, non_selectable_item)

    # Clear any previous selections
    scheduler_table.clearSelection()

    # Select the task item after adding
    scheduler_table.setCurrentCell(row_position, 0, QItemSelectionModel.Select)


def remove_task_row(scheduler_table, delete_button):
    # Get the current row of the delete button
    row_position = scheduler_table.indexAt(delete_button.pos()).row()
    footer_row = scheduler_table.rowCount() - 1

    if row_position != footer_row and row_position >= 0:
        scheduler_table.removeRow(row_position)
        # Clear any previous selections
        scheduler_table.clearSelection()

def selected_scheduler_task(main_window, index):
    scheduler_table = getattr(main_window.widgets, f"scheduler_table_{index}")
    selected_items = scheduler_table.selectedItems()
    if selected_items and selected_items[0].column() == 0:  # Only proceed if column 0 (Task Name) is selected
        task_text = selected_items[0].text()
        print(f"Selected Task: {task_text}")
    else:
        scheduler_table.clearSelection()  # Clear selection if an invalid cell is selected