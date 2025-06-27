import json
import re
from time import sleep

from PySide6.QtCore import Qt, QItemSelectionModel, QThreadPool, QTime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QAbstractItemView, \
    QComboBox, QLineEdit, QLabel, QVBoxLayout, QMessageBox, QFrame, QCheckBox, QSpinBox, QTimeEdit
from sqlalchemy import select

from core.custom_widgets.QCheckComboBox import QCheckComboBox
from db.db_setup import get_session
from db.models import Profile, Instance, GeneralPreset, JoinRallyPresetConfiguration, JoinRallyPresetOption, ProfileData
from features.utils.profile_load_worker import ProfileLoadWorker


def init_run_tab(main_window, index, instance):
    # Setup scheduler table
    setup_scheduler_table(main_window, index)

    # Initialize preset control buttons
    initialize_preset_buttons(main_window, index)

    # Initialize manage profile control buttons
    initialize_manage_profiles(main_window,index)

    # Populate the profile combobox
    populate_profile_combo(getattr(main_window.widgets, f"emu_profile_{index}"))

    # Populate the manage profile combobox
    populate_profile_combo(getattr(main_window.widgets, f"profile_combobox_{index}"))

    # Load the emulator data(name,port and profile)
    if instance:
        load_instance_data(main_window,instance,index)
        setup_instance_edit_handlers(main_window, index)


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
    # set the instance id as property for profile combobox
    profile_combobox.setProperty('instance_id', instance.id)
    for i in range(profile_combobox.count()):
        # Get the user data (profile_id) of the current item
        item_data = profile_combobox.itemData(i)
        if item_data == instance.profile_id:
            # Set the combobox index to the matching item
            profile_combobox.setCurrentIndex(i)

    # Set the emulator name
    emulator_name_ledit = getattr(main_window.widgets, f"emu_name_{index}")
    # set the instance id as property for emulator name line edit
    emulator_name_ledit.setProperty('instance_id', instance.id)
    # print(f"Instance Name: {instance.emulator_name}")
    emulator_name_ledit.setText(instance.emulator_name if instance.emulator_name else f"Emulator {index}")

    # Set emulator port
    emulator_port_ledit = getattr(main_window.widgets, f"emu_port_{index}")
    # set the instance id as property for emulator port line edit
    emulator_port_ledit.setProperty('instance_id', instance.id)
    emulator_port_ledit.setText(str(instance.emulator_port) if instance.emulator_port else "")

def setup_instance_edit_handlers(main_window, index):
    """
    Sets up event handlers for instance widgets to update the database on change.

    Args:
        main_window: The main window containing the widgets.
        index: The index of the instance being edited.
    """
    # Connect profile combobox changes
    profile_combobox = getattr(main_window.widgets, f"emu_profile_{index}")
    profile_combobox.currentIndexChanged.connect(
        lambda: update_instance_profile(main_window, index)
    )

    # Connect emulator name line edit changes
    emulator_name_ledit = getattr(main_window.widgets, f"emu_name_{index}")
    emulator_name_ledit.editingFinished.connect(
        lambda: update_instance_emulator_name(main_window, index)
    )

    # Connect emulator port line edit changes
    emulator_port_ledit = getattr(main_window.widgets, f"emu_port_{index}")
    emulator_port_ledit.editingFinished.connect(
        lambda: update_instance_emulator_port(main_window, index)
    )

def update_instance_profile(main_window, index):
    """
    Updates the profile_id of the instance in the database.

    Args:
        main_window: The main window containing the widgets.
        index: The index of the instance being edited.
    """
    # print(f"Profile changed {index}")
    profile_combobox = getattr(main_window.widgets, f"emu_profile_{index}")
    instance_id = profile_combobox.property("instance_id")
    selected_profile_id = profile_combobox.currentData()

    if instance_id is not None:
        session = get_session()
        try:
            instance = session.query(Instance).get(instance_id)
            if instance:
                instance.profile_id = selected_profile_id
                session.commit()
                load_profile_controls(main_window, index, selected_profile_id)
        finally:
            session.close()

def update_instance_emulator_name(main_window, index):
    """
    Updates the emulator_name of the instance in the database.

    Args:
        main_window: The main window containing the widgets.
        index: The index of the instance being edited.
    """
    emulator_name_ledit = getattr(main_window.widgets, f"emu_name_{index}")
    instance_id = emulator_name_ledit.property("instance_id")
    new_name = emulator_name_ledit.text()

    # Default name if the line edit is empty
    default_name = f"Emulator {index}"
    if not new_name:
        new_name = default_name
        emulator_name_ledit.setText(new_name)


    if instance_id is not None:
        session = get_session()
        try:
            instance = session.query(Instance).get(instance_id)
            if instance:
                instance.emulator_name = new_name
                session.commit()
        finally:
            session.close()

def update_instance_emulator_port(main_window, index):
    """
    Updates the emulator_port of the instance in the database.

    Args:
        main_window: The main window containing the widgets.
        index: The index of the instance being edited.
    """
    emulator_port_ledit = getattr(main_window.widgets, f"emu_port_{index}")
    instance_id = emulator_port_ledit.property("instance_id")
    new_port = emulator_port_ledit.text()

    if instance_id is not None:
        session = get_session()
        try:
            instance = session.query(Instance).get(instance_id)
            if instance:
                instance.emulator_port = int(new_port) if new_port.isdigit() else None
                session.commit()
        finally:
            session.close()


### PRESET WIDGETS FUNCTIONALITIES ###
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
    cancel_button.clicked.connect(lambda: cancel_preset_edit_mode(main_window, index, preset_combo))

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


def cancel_preset_edit_mode(main_window, index, preset_combo):
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
    cancel_button.clicked.connect(lambda: cancel_preset_edit_mode(main_window, index, preset_combo))

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


### MANAGE PROFILE WIDGETS FUNCTIONALITIES ###
def initialize_manage_profiles(main_window, index):
    """
    Initialize the manage profile UI and logic for the given index.
    :param main_window: The main window containing the widgets.
    :param index: The index to uniquely identify the profile section.
    """
    # Access widgets
    profile_combobox = getattr(main_window.widgets, f"profile_combobox_{index}")
    edit_profile_btn = getattr(main_window.widgets, f"edit_profile_btn_{index}")
    save_profile_btn = getattr(main_window.widgets, f"save_profile_btn_{index}")
    add_profile_btn = getattr(main_window.widgets, f"add_profile_btn_{index}")
    manage_profile_frame = getattr(main_window.widgets, f"manage_profile_frame_{index}")

    # Connect buttons to their respective actions
    edit_profile_btn.clicked.connect(lambda: enable_profile_edit_mode(main_window, index))
    save_profile_btn.clicked.connect(lambda: confirm_save_controls(main_window, index))
    add_profile_btn.clicked.connect(lambda: enable_add_mode(main_window, index))

    # Enable/disable buttons based on profile selection
    profile_combobox.currentIndexChanged.connect(
        lambda: toggle_main_frame_buttons(profile_combobox, edit_profile_btn, save_profile_btn)
    )
    toggle_main_frame_buttons(profile_combobox, edit_profile_btn, save_profile_btn)

def toggle_main_frame_buttons(profile_combobox, edit_btn, save_btn):
    """
    Enable or disable buttons in the main frame based on profile selection.
    """
    has_selection = profile_combobox.currentIndex() >= 0
    edit_btn.setEnabled(has_selection)
    save_btn.setEnabled(has_selection)

def enable_profile_edit_mode(main_window, index):
    # Access the main frame and its child widgets
    main_frame = getattr(main_window.widgets, f"manage_profile_frame_{index}")
    profile_combo = getattr(main_window.widgets, f"profile_combobox_{index}")
    edit_btn = getattr(main_window.widgets, f"edit_profile_btn_{index}")
    save_btn = getattr(main_window.widgets, f"save_profile_btn_{index}")
    add_btn = getattr(main_window.widgets, f"add_profile_btn_{index}")

    # Create a line edit and set the current profile name as text
    profile_line_edit = QLineEdit()
    profile_line_edit.setFixedHeight(40)
    profile_line_edit.setText(profile_combo.currentText())
    profile_line_edit.setObjectName(f"profile_lineedit_{index}")

    # Create save and cancel buttons
    save_button = QPushButton()
    save_button.setFixedSize(45, 45)
    save_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
    save_button.setObjectName(f"profile_save_btn_{index}")

    cancel_button = QPushButton()
    cancel_button.setFixedSize(45, 45)
    cancel_button.setIcon(QIcon(":/icons/images/icons/cil-x.png"))
    cancel_button.setObjectName(f"profile_cancel_btn_{index}")


    # Create delete button
    delete_button = QPushButton()
    delete_button.setFixedSize(45, 45)
    delete_button.setIcon(QIcon(":/icons/images/icons/icon_delete_2.png"))
    delete_button.setObjectName(f"profile_delete_btn_{index}")

    # Define actions for buttons
    save_button.clicked.connect(lambda: save_profile_name(main_window, index, profile_line_edit))
    cancel_button.clicked.connect(lambda: cancel_edit_mode(main_window, index))
    delete_button.clicked.connect(lambda: delete_profile(main_window, index))

    # Access or create the layout in the main frame
    if main_frame.layout() is None:
        layout = QVBoxLayout(main_frame)
        main_frame.setLayout(layout)
    else:
        layout = main_frame.layout()

    # Hide the main frame widgets
    profile_combo.hide()
    edit_btn.hide()
    save_btn.hide()
    add_btn.hide()

    # Add new widgets to the layout
    layout.addWidget(profile_line_edit)
    layout.addWidget(save_button)
    layout.addWidget(cancel_button)
    layout.addWidget(delete_button)

    # Store new widgets in the main_window
    setattr(main_window, profile_line_edit.objectName(), profile_line_edit)
    setattr(main_window, save_button.objectName(), save_button)
    setattr(main_window, cancel_button.objectName(), cancel_button)
    setattr(main_window, delete_button.objectName(), delete_button)

def save_profile_name(main_window, index, profile_line_edit):
    # Access the current profile combo box and details
    profile_combo = getattr(main_window.widgets, f"profile_combobox_{index}")
    current_index = profile_combo.currentIndex()
    profile_id = profile_combo.itemData(current_index)  # Get the profile ID
    new_name = profile_line_edit.text().strip()  # Get the new name and trim whitespace

    # Validate the new name
    if not new_name:
        QMessageBox.critical(main_window, "Error", "Profile name cannot be empty!")
        return

    # Check if the new name already exists in the database
    session = get_session()
    existing_profile = session.query(Profile).filter(Profile.name == new_name).first()
    if existing_profile and existing_profile.id != profile_id:
        QMessageBox.critical(main_window, "Error", "A profile with this name already exists!")
        session.close()
        return

    # Update the profile name in the database
    profile = session.query(Profile).filter_by(id=profile_id).first()
    if profile:
        profile.name = new_name
        session.commit()
    session.close()

    # Update all instance combo boxes with the new profile name
    from core.menu_button import get_active_instance_indexes
    instance_indexes = get_active_instance_indexes(main_window)
    for instance_index in instance_indexes:
        # Access the combo boxes
        profile_combobox = getattr(main_window.widgets, f"profile_combobox_{instance_index}")
        emu_profile_combo = getattr(main_window.widgets, f"emu_profile_{instance_index}")

        # Update the name in the profile combo box
        for i in range(profile_combobox.count()):
            if profile_combobox.itemData(i) == profile_id:
                profile_combobox.setItemText(i, new_name)

        # Update the name in the emulator profile combo box
        for i in range(emu_profile_combo.count()):
            if emu_profile_combo.itemData(i) == profile_id:
                emu_profile_combo.setItemText(i, new_name)

    # Show success message
    QMessageBox.information(main_window, "Success", "Profile name updated successfully!")

    # Restore the main frame
    cancel_edit_mode(main_window, index)

def cancel_edit_mode(main_window, index):
    # Access the main frame and its child widgets
    main_frame = getattr(main_window.widgets, f"manage_profile_frame_{index}")
    profile_combo = getattr(main_window.widgets, f"profile_combobox_{index}")
    edit_btn = getattr(main_window.widgets, f"edit_profile_btn_{index}")
    save_btn = getattr(main_window.widgets, f"save_profile_btn_{index}")
    add_btn = getattr(main_window.widgets, f"add_profile_btn_{index}")

    # Show the main frame widgets
    profile_combo.show()
    edit_btn.show()
    save_btn.show()
    add_btn.show()

    # Remove dynamic widgets from the layout
    layout = main_frame.layout()
    for widget_name in [f"profile_lineedit_{index}", f"profile_save_btn_{index}", f"profile_cancel_btn_{index}", f"profile_delete_btn_{index}"]:
        widget = getattr(main_window, widget_name, None)
        if widget:
            layout.removeWidget(widget)
            widget.hide()
            widget.deleteLater()
            delattr(main_window, widget_name)

def delete_profile(main_window, index):
    """
    Deletes the current profile from the database and updates the UI.
    """
    # Access the profile combo box
    profile_combo = getattr(main_window.widgets, f"profile_combobox_{index}")
    profile_name = profile_combo.currentText()
    current_index = profile_combo.currentIndex()

    # Check if there is only one profile remaining
    if profile_combo.count() <= 1:
        QMessageBox.critical(main_window, "Error", "At least one profile must be present!")
        return

    # Show confirmation dialog
    confirmation = QMessageBox.question(
        main_window,
        "Confirm Deletion",
        f"Are you sure you want to delete the profile '{profile_name}'?",
        QMessageBox.Yes | QMessageBox.No
    )
    if confirmation != QMessageBox.Yes:
        return

    # Get the current profile ID
    profile_id = profile_combo.itemData(current_index)
    session = get_session()

    # Query and delete the profile from the database using the ID
    profile = session.query(Profile).filter_by(id=profile_id).first()
    if profile:
        session.delete(profile)
        session.commit()
    session.close()


    # Update the combo boxes
    from core.menu_button import get_active_instance_indexes
    instance_indexes = get_active_instance_indexes(main_window)
    for instance_index in instance_indexes:
        # Access the combo boxes
        profile_combobox = getattr(main_window.widgets, f"profile_combobox_{instance_index}")
        emu_profile_combo = getattr(main_window.widgets, f"emu_profile_{instance_index}")

        # Remove the profile from the combo box
        profile_combobox.removeItem(current_index)

        # Update Emulator profile combobox
        if emu_profile_combo.currentData() == profile_id:
            if current_index != 0:
                emu_profile_combo.setCurrentIndex(0)
            else:
                emu_profile_combo.setCurrentIndex(1)
        # Remove the profile from the emulator profile combo box
        emu_profile_combo.removeItem(current_index)


    # Show success dialog
    QMessageBox.information(main_window, "Profile", f"Profile '{profile_name}' deleted successfully!")

    # Restore the main frame
    cancel_edit_mode(main_window, index)

def enable_add_mode(main_window, index):
    # Access the main frame and its child widgets
    main_frame = getattr(main_window.widgets, f"manage_profile_frame_{index}")
    profile_combo = getattr(main_window.widgets, f"profile_combobox_{index}")
    edit_btn = getattr(main_window.widgets, f"edit_profile_btn_{index}")
    save_btn = getattr(main_window.widgets, f"save_profile_btn_{index}")
    add_btn = getattr(main_window.widgets, f"add_profile_btn_{index}")

    # Create a line edit for entering a new profile name
    profile_line_edit = QLineEdit()
    profile_line_edit.setFixedHeight(40)
    profile_line_edit.setPlaceholderText("Enter New Profile")
    profile_line_edit.setObjectName(f"profile_lineedit_{index}")

    # Create save and cancel buttons
    save_button = QPushButton()
    save_button.setFixedSize(45, 45)
    save_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
    save_button.setObjectName(f"profile_save_btn_{index}")

    cancel_button = QPushButton()
    cancel_button.setFixedSize(45, 45)
    cancel_button.setIcon(QIcon(":/icons/images/icons/cil-x.png"))
    cancel_button.setObjectName(f"profile_cancel_btn_{index}")

    # Define actions for buttons
    save_button.clicked.connect(lambda: add_new_profile(main_window, index, profile_line_edit))
    cancel_button.clicked.connect(lambda: cancel_edit_mode(main_window, index))

    # Access or create the layout in the main frame
    if main_frame.layout() is None:
        layout = QVBoxLayout(main_frame)
        main_frame.setLayout(layout)
    else:
        layout = main_frame.layout()

    # Hide the main frame widgets
    profile_combo.hide()
    edit_btn.hide()
    save_btn.hide()
    add_btn.hide()

    # Add new widgets to the layout
    layout.addWidget(profile_line_edit)
    layout.addWidget(save_button)
    layout.addWidget(cancel_button)

    # Store new widgets in the main_window
    setattr(main_window, profile_line_edit.objectName(), profile_line_edit)
    setattr(main_window, save_button.objectName(), save_button)
    setattr(main_window, cancel_button.objectName(), cancel_button)

def add_new_profile(main_window, index, profile_line_edit):
    """
    Add a new profile to the database and update UI elements.

    Args:
        main_window: The main window containing widgets.
        index: The index of the current tab.
        profile_line_edit: QLineEdit containing the new profile name.
        session: SQLAlchemy session for database operations.
    """

    # Get the new profile name from the line edit
    new_profile_name = profile_line_edit.text().strip()

    # Validate the profile name
    if not new_profile_name:
        QMessageBox.critical(main_window, "Error", "Profile name cannot be empty.")
        return
    session = get_session()
    # Check if the profile name already exists in the database
    if session.query(Profile).filter_by(name=new_profile_name).first():
        QMessageBox.critical(main_window, "Error", f"The profile '{new_profile_name}' already exists.")
        return

    # Add the new profile to the database
    try:
        new_profile = Profile(name=new_profile_name)
        session.add(new_profile)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        QMessageBox.critical(main_window, "Error", f"Error saving profile to database")
        return

    # Update the combo boxes
    from core.menu_button import get_active_instance_indexes
    instance_indexes = get_active_instance_indexes(main_window)
    for instance_index in instance_indexes:
        # Access the combo boxes
        profile_combo = getattr(main_window.widgets, f"profile_combobox_{instance_index}")
        emu_profile_combo = getattr(main_window.widgets, f"emu_profile_{instance_index}")

        profile_combo.addItem(new_profile.name,new_profile.id)
        if instance_index == index:
            profile_combo.setCurrentText(new_profile_name)

        # Temporarily disconnect the signal to avoid triggering events
        try:
            emu_profile_combo.blockSignals(True)
            emu_profile_combo.addItem(new_profile.name,new_profile.id)
        finally:
            emu_profile_combo.blockSignals(False)
            session.close()

    # Restore the main frame
    cancel_edit_mode(main_window, index)
    QMessageBox.information(main_window, "Information", f"Profile '{new_profile.name}' has been successfully added.")

    # Create the default entries for preset configurations and preset options
    session = get_session()
    profile_id = getattr(main_window.widgets, f"profile_combobox_{index}").currentData()

    # Fetch the first general preset ID
    general_preset = session.execute(
        select(GeneralPreset.id).order_by(GeneralPreset.id.asc()).limit(1)
    ).scalar()

    # Insert a new entry into `jr_preset_configurations`
    new_preset_configuration = JoinRallyPresetConfiguration(
        profile_id=profile_id,
        general_preset_id=general_preset
    )
    session.add(new_preset_configuration)
    # Flush to get the new `jr_preset_configuration_id`
    session.flush()

    # Create 8 entries in `jr_preset_options`
    preset_options = []
    for preset_number in range(1, 9):
        preset_options.append(
            JoinRallyPresetOption(
                preset_configuration_id=new_preset_configuration.id,
                preset_number=preset_number,
                # preset_selected=(preset_number == 1),  # True for the first preset, False for others
                use_selected_generals=False,
                skip_no_general=False,
                reset_to_one_troop=False
            )
        )

    # Bulk insert the preset options
    session.bulk_save_objects(preset_options)
    session.commit()
    session.close()

def confirm_save_controls(main_window, index):
    """
    Confirm saving controls to the selected profile.
    """
    profile_combobox = getattr(main_window.widgets, f"profile_combobox_{index}")
    selected_profile = profile_combobox.currentText()

    if not selected_profile:
        QMessageBox.warning(main_window, "Error", "No profile selected.")
        return

    reply = QMessageBox.question(
        main_window,
        "Save Controls",
        f"Are you sure you want to save the controls to the profile '{selected_profile}'?",
        QMessageBox.Yes | QMessageBox.No
    )

    if reply == QMessageBox.Yes:
        save_profile_controls(main_window,index)
        QMessageBox.information(main_window, "Success", f"Controls saved to profile '{selected_profile}'.")


def save_profile_controls(main_window, index):
    """
    Save widget data from a dynamically generated page into a profile dictionary.

    :param main_window: The main window containing widgets
    :param index: The index of the emulator page
    :return: Dictionary of widget data categorized by widget type
    """
    # Initialize the dictionary to store widget data
    widgets_dict = {}

    # Get the page containing the widgets
    page_emu = getattr(main_window.widgets, f"page_emu_{index}", None)
    if not page_emu:
        raise ValueError(f"Page for index {index} not found!")

    # Loop through all child widgets of the page
    for widget in page_emu.findChildren(QWidget):
        object_name = widget.objectName()

        # Check if the object name ends with '___' followed by digits
        if re.search(r'___\d+$', object_name):
            # Clean the object name by removing the trailing digits after '___'
            generated_obj_name = re.sub(r'___\d+$', '___', object_name)

            # Get widget data (type and value)
            widget_data = return_widget_data(widget, generated_obj_name)

            # Skip unsupported widgets
            if not widget_data:
                continue

            # Add data to the appropriate key in the dictionary
            widgets_dict.setdefault(widget.__class__.__name__, []).append(widget_data)

    # Save it to the db
    profile_id = getattr(main_window.widgets,f'profile_combobox_{index}').currentData() # Get the profile id
    session = get_session()
    try:
        # Check if there's already a ProfileData entry for this profile
        profile_data = session.query(ProfileData).filter_by(profile_id=profile_id).first()

        if profile_data:
            # Update existing entry
            profile_data.settings = json.dumps(widgets_dict)
        else:
            # Create new entry
            profile_data = ProfileData(profile_id=profile_id, settings=json.dumps(widgets_dict))
            session.add(profile_data)
        # Commit changes
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

    # print(widgets_dict)

def return_widget_data(widget, object_name):
    """
    Return the widget type and its data for saving into the profile.

    :param widget: The widget instance
    :param object_name: The cleaned object name
    :return: Tuple of widget type (str) and widget data (dict)
    """
    widget_data = None

    if isinstance(widget, QCheckBox):
        widget_data = {"object_name": object_name, "value": widget.isChecked()}
    elif isinstance(widget, QLineEdit):
        widget_data = {"object_name": object_name, "value": widget.text()}
    elif isinstance(widget, QSpinBox):
        widget_data = {"object_name": object_name, "value": widget.value()}
    elif isinstance(widget, QTimeEdit):
        widget_data = {"object_name": object_name, "value": widget.time().toString()}
    elif isinstance(widget, QCheckComboBox):
        if not widget.isEnabled():
            widget_data = {"object_name": object_name, "value": []}
        else:
            selected_values = []
            for i in range(widget.count()):
                if widget.itemCheckState(i) == Qt.Checked:
                    selected_values.append(widget.itemData(i))
            widget_data = {"object_name": object_name, "value": selected_values}
    elif isinstance(widget, QComboBox):
        widget_data = {"object_name": object_name, "value": widget.currentData()}
    elif isinstance(widget, QPushButton):
        widget_data = {"object_name": object_name, 'type': widget.property('type')}
        if widget.property('type') == 'checkable':
            widget_data["value"] = widget.isChecked()
        elif widget.property('type') == 'value':
            widget_data["value"] = widget.property('value')
            # print(widget.__class__.__name__)
            # print(widget.property('value'))
            # # print(widget_data)
            # print(f"Object Name: {widget.objectName()}")
    else:
        # Optionally log unsupported widget types for debugging
        print(f"Unsupported widget type: {widget.__class__.__name__} (run_tab_controller)")


    return widget_data

def load_profile_controls(main_window, index,profile_id):
    """
    Load profile controls using QThreadPool for efficiency.

    :param main_window: The main application window containing widgets.
    :param index: The index of the profile page to load controls for.
    :param profile_id: profile id to load the controls
    """
    # Create the worker
    worker = ProfileLoadWorker(profile_id)
    # Store the ref in main_window to keep the worker alive
    main_window.worker_refs[index] = worker
    # Connect signals to slots
    worker.signals.profile_loaded.connect(lambda settings: on_profile_loaded(settings, main_window, index))
    worker.signals.error.connect(lambda error: print(f"Error: {error}"))

    # Run the worker using QThreadPool
    QThreadPool.globalInstance().start(worker)


def on_profile_loaded(settings, main_window, index):
    """
    Update the main window with the loaded profile settings.

    :param settings: Dictionary of profile settings.
    :param main_window: The main application window containing widgets.
    :param index: The index of the profile page to load controls for.
    """
    # print(index, settings)

    page_emu = getattr(main_window.widgets, f"page_emu_{index}", None)
    if not page_emu:
        print(f"Page for index {index} not found!")
        return

    # Update widgets with loaded settings
    for widget_type, widgets_data in settings.items():
        for widget_data in widgets_data:
            object_name = widget_data.get("object_name")
            value = widget_data.get("value")

            # Find the widget by its object name
            widget = getattr(main_window.widgets,f"{object_name}{index}",None)
            if not widget:
                continue

            # print(widget.objectName())
            # print(f"{widget.objectName()} :: {widget.__class__.__name__}")

            # Update the widget
            if isinstance(widget, QCheckBox):
                widget.setChecked(value)
                # print(widget.objectName(),value)
            elif isinstance(widget, QLineEdit):
                widget.setText(value)
            elif isinstance(widget, QSpinBox):
                widget.setValue(value)
            elif isinstance(widget, QTimeEdit):
                time = QTime.fromString(value, "hh:mm:ss")
                if time.isValid():
                    widget.setTime(time)
            elif isinstance(widget, QCheckComboBox):
                # Check if the value is an empty list, meaning all options should be unchecked
                if not value:  # Empty list
                    for i in range(widget.count()):
                        widget.setItemCheckState(i, Qt.Unchecked)
                else:  # Loop through the options and check if the item's data matches the saved value
                    for i in range(widget.count()):
                        item_data = widget.itemData(i)  # Get itemData for each option
                        if item_data in value:
                            widget.setItemCheckState(i, Qt.Checked)  # Check the option
                        else:
                            widget.setItemCheckState(i, Qt.Unchecked)  # Uncheck the option
            elif isinstance(widget, QComboBox):
                # Loop through all items in the QComboBox
                for i in range(widget.count()):
                    # Get the item data for the current index
                    item_data = widget.itemData(i)
                    # Check if the stored value matches the item's data
                    if item_data == value:
                        # Set the current index to the matching item
                        widget.setCurrentIndex(i)
                        break
            elif isinstance(widget, QPushButton):
                button_type = widget.property('type')  # Get the type of the button
                if button_type == 'checkable':
                    # Set the button's checked state
                    widget.setChecked(value)
                elif button_type == 'value':
                    # Set the button's 'value' property
                    widget.setProperty('value', value)
    # Destroy the worker
    main_window.worker_refs[index] = None





### SCHEDULER TABLE ###
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