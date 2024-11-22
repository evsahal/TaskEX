from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from requests import session

from db.db_setup import get_session
from db.models import GeneralPreset, General, PresetGeneralAssignment
from gui.generated.generals_selection import Ui_GeneralsSelectionDialog


class GeneralsSelectionDialog(QDialog, Ui_GeneralsSelectionDialog):
    def __init__(self, parent):
        super(GeneralsSelectionDialog, self).__init__(parent)
        self.setupUi(self)

        self.preset_id = None
        self.all_generals = None

        self.load_presets()
        self.connect_preset_buttons()
        # Fetch generals from the database
        self.load_all_generals()

        self.populate_generals_widgets()

    def load_all_generals(self):
        session = get_session()
        self.all_generals = session.query(General).filter(General.scale.isnot(None)).all()

    def populate_generals_widgets(self):
        """
        Populate the list widgets for both main and assistant generals.
        """
        # Clear existing items
        self.all_generals_main.clear()
        self.selected_generals_main.clear()
        self.all_generals_assistant.clear()
        self.selected_generals_assistant.clear()

        session = get_session()

        # Query for all selected generals (both main and assistant) for the given preset_id
        selected_generals = session.query(General.name, PresetGeneralAssignment.is_main_general).join(
            PresetGeneralAssignment).filter(
            PresetGeneralAssignment.preset_id == self.preset_id
        ).all()

        # Separate the selected generals into main and assistant
        selected_generals_main_names = [general.name for general in selected_generals if general.is_main_general]
        selected_generals_assistant_names = [general.name for general in selected_generals if
                                             not general.is_main_general]

        # Iterate through all generals and populate the widgets
        for general in self.all_generals:
            if general.name in selected_generals_main_names:
                self.selected_generals_main.addItem(general.name)
            else:
                self.all_generals_main.addItem(general.name)

            if general.name in selected_generals_assistant_names:
                self.selected_generals_assistant.addItem(general.name)
            else:
                self.all_generals_assistant.addItem(general.name)

        session.close()

    def connect_preset_buttons(self):
        # Initialize event connections
        self.edit_btn.clicked.connect(self.enable_edit_mode)
        self.delete_btn.clicked.connect(self.delete_preset)
        self.add_btn.clicked.connect(self.add_new_preset)
        self.preset_combobox.currentIndexChanged.connect(self.on_preset_changed)
        self.exit_btn.clicked.connect(lambda: self.close())



    def load_presets(self):
        """
        Load all presets from the database and populate the combo box.
        """

        session = get_session()

        # Query for all GeneralPresets
        presets = session.query(GeneralPreset).all()

        # Populate the combo box with preset names
        for preset in presets:
            self.preset_combobox.addItem(preset.name)

        # After populating, select the default option based on self.preset_id
        if self.preset_id is None:
            # If preset_id is None, select the first item (index 0)
            self.preset_combobox.setCurrentIndex(0)
            # Set self.preset_id to the ID of the first preset
            self.preset_id = presets[0].id
        else:
            # If preset_id is not None, find the preset by ID and select it
            for index, preset in enumerate(presets):
                if preset.id == self.preset_id:
                    self.preset_combobox.setCurrentIndex(index)
                    break


        session.close()

    def on_preset_changed(self):
        """
        Handle the event when the preset is changed.
        Update the UI with settings based on the selected preset.
        """
        # Get the selected preset name
        selected_preset_name = self.preset_combobox.currentText()

        session = get_session()

        # Fetch the preset object based on the selected name
        selected_preset = session.query(GeneralPreset).filter_by(name=selected_preset_name).first()

        if selected_preset:
            self.preset_id = selected_preset.id
            # Set category_combobox value
            self.category_combobox.setCurrentText(selected_preset.general_category.value)

            # Set view_combobox value
            self.view_combobox.setCurrentText(selected_preset.general_view.value)

            # Set filter_combobox value (custom combobox with checkboxes)
            filter_values = selected_preset.general_filter.split(",") if selected_preset.general_filter else []
            for index in range(self.filter_combobox.count()):
                item_text = self.filter_combobox.itemText(index)
                if item_text.lower() in filter_values:
                    self.filter_combobox.setItemCheckState(index, Qt.Checked)
                else:
                    self.filter_combobox.setItemCheckState(index, Qt.Unchecked)
            # Ensure the placeholder text is updated with the selected items by repainting the widget
            self.filter_combobox.repaint()

            # Set swipe_attempts_spinbox value
            self.swipe_attempts_spinbox.setValue(selected_preset.swipe_attempts)

            # Update the general list widgets
            self.populate_generals_widgets()

        session.close()

    def add_new_preset(self):
        """
        Enter add mode: Hides the combo box and buttons, and shows a line edit with Save/Cancel buttons.
        """
        # Access preset widget
        preset_widget = self.manage_preset_frame

        # Create line edit
        preset_line_edit = QLineEdit()
        preset_line_edit.setFixedHeight(40)
        preset_line_edit.setFixedWidth(180)
        preset_line_edit.setPlaceholderText("Enter new preset")
        preset_line_edit.setObjectName("preset_name_lineedit")

        # Create Save and Cancel buttons
        save_button = QPushButton()
        save_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
        save_button.setFixedSize(40, 40)
        save_button.setObjectName("preset_name_save_btn")

        cancel_button = QPushButton()
        cancel_button.setIcon(QIcon(":/icons/images/icons/cil-x.png"))
        cancel_button.setFixedSize(40, 40)
        cancel_button.setObjectName("preset_name_cancel_btn")

        # Connect Save/Cancel button actions
        save_button.clicked.connect(lambda: self.save_new_preset_name(preset_line_edit))
        cancel_button.clicked.connect(self.cancel_edit_mode)

        # Access or create layout
        if preset_widget.layout() is None:
            layout = QHBoxLayout(preset_widget)
            preset_widget.setLayout(layout)
        else:
            layout = preset_widget.layout()

        # Hide combo box and control buttons
        self.preset_combobox.hide()
        self.edit_btn.hide()
        self.delete_btn.hide()
        self.add_btn.hide()

        # Add line edit and buttons
        layout.addWidget(preset_line_edit)
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)

        # Store widgets
        setattr(self, preset_line_edit.objectName(), preset_line_edit)
        setattr(self, save_button.objectName(), save_button)
        setattr(self, cancel_button.objectName(), cancel_button)

    def save_new_preset_name(self, preset_line_edit):
        """
        Save the new preset entered by the user.
        """
        new_name = preset_line_edit.text().strip()

        if not new_name:  # Check if the name is empty
            QMessageBox.warning(self, "Error", "Preset name cannot be empty.")
            return

        session = get_session()

        # Check if the preset name already exists in the database
        existing_preset = session.query(GeneralPreset).filter_by(name=new_name).first()
        if existing_preset:
            QMessageBox.warning(self, "Error", "A preset with this name already exists.")
            session.close()
            return

        # Create a new preset entry in the database
        new_preset = GeneralPreset(name=new_name)
        session.add(new_preset)
        session.commit()

        # Add the new preset to the combo box and select it
        self.preset_combobox.addItem(new_name)
        self.preset_combobox.setCurrentIndex(self.preset_combobox.count() - 1)

        # Set the current preset ID to the newly created preset's ID
        self.preset_id = new_preset.id

        session.close()

        # Clean up and show the original UI
        self.remove_preset_edit_widgets()
        self.preset_combobox.show()
        self.edit_btn.show()
        self.delete_btn.show()
        self.add_btn.show()

    def enable_edit_mode(self):
        """
        Enable edit mode: Replaces the combo box with a line edit and shows Save/Cancel buttons.
        """
        # Access preset widget
        preset_widget = self.manage_preset_frame

        # Create line edit
        preset_line_edit = QLineEdit()
        preset_line_edit.setFixedHeight(40)
        preset_line_edit.setFixedWidth(180)
        preset_line_edit.setText(self.preset_combobox.currentText())
        preset_line_edit.setObjectName("preset_name_lineedit")

        # Create Save and Cancel buttons
        save_button = QPushButton()
        save_button.setIcon(QIcon(":/icons/images/icons/cil-save.png"))
        save_button.setFixedSize(40, 40)
        save_button.setObjectName("preset_name_save_btn")

        cancel_button = QPushButton()
        cancel_button.setIcon(QIcon(":/icons/images/icons/cil-x.png"))
        cancel_button.setFixedSize(40, 40)
        cancel_button.setObjectName("preset_name_cancel_btn")

        # Connect Save/Cancel button actions
        save_button.clicked.connect(lambda: self.save_preset_name(preset_line_edit))
        cancel_button.clicked.connect(self.cancel_edit_mode)

        # Access or create layout
        if preset_widget.layout() is None:
            layout = QHBoxLayout(preset_widget)
            preset_widget.setLayout(layout)
        else:
            layout = preset_widget.layout()

        # Hide combo box and control buttons
        self.preset_combobox.hide()
        self.edit_btn.hide()
        self.delete_btn.hide()
        self.add_btn.hide()

        # Add line edit and buttons
        layout.addWidget(preset_line_edit)
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)

        # Store widgets in the main_window
        setattr(self, preset_line_edit.objectName(), preset_line_edit)
        setattr(self, save_button.objectName(), save_button)
        setattr(self, cancel_button.objectName(), cancel_button)

    def save_preset_name(self, preset_line_edit):
        """
        Save the edited preset name.
        """
        new_name = preset_line_edit.text().strip()

        if not new_name:  # Check if the name is empty
            QMessageBox.warning(self, "Error", "Preset name cannot be empty.")
            return

        # Get the current preset from the combo box
        current_index = self.preset_combobox.currentIndex()
        current_name = self.preset_combobox.itemText(current_index)

        # Skip validation if the name hasn't changed
        if new_name == current_name:
            self.remove_preset_edit_widgets()
            self.preset_combobox.show()
            self.edit_btn.show()
            self.delete_btn.show()
            self.add_btn.show()
            return

        session = get_session()

        # Check if a preset with the new name already exists in the database
        existing_preset = session.query(GeneralPreset).filter_by(name=new_name).first()
        if existing_preset:
            QMessageBox.warning(self, "Error", "A preset with this name already exists.")
            session.close()
            return

        # Fetch the current preset from the database
        selected_preset = session.query(GeneralPreset).filter_by(name=current_name).first()

        # Update the preset name in the database
        selected_preset.name = new_name
        session.commit()

        # Update combo box with the new name
        self.preset_combobox.setItemText(current_index, new_name)

        # Update the current preset ID
        self.preset_id = selected_preset.id

        session.close()

        # Clean up edit mode
        self.remove_preset_edit_widgets()

        # Show combo box and control buttons again
        self.preset_combobox.show()
        self.edit_btn.show()
        self.delete_btn.show()
        self.add_btn.show()

    def cancel_edit_mode(self):
        """
        Cancel edit mode and revert to the previous state.
        """
        self.remove_preset_edit_widgets()

        # Show combo box and control buttons
        self.preset_combobox.show()
        self.edit_btn.show()
        self.delete_btn.show()
        self.add_btn.show()

    def remove_preset_edit_widgets(self):
        """
        Remove line edit and Save/Cancel buttons from the UI.
        """
        preset_line_edit = getattr(self, f"preset_name_lineedit", None)
        save_button = getattr(self, f"preset_name_save_btn", None)
        cancel_button = getattr(self, f"preset_name_cancel_btn", None)

        if preset_line_edit:
            preset_line_edit.deleteLater()
            delattr(self, f"preset_name_lineedit")

        if save_button:
            save_button.deleteLater()
            delattr(self, f"preset_name_save_btn")

        if cancel_button:
            cancel_button.deleteLater()
            delattr(self, f"preset_name_cancel_btn")

    def delete_preset(self):
        """
        Delete the currently selected preset from the combo box and the database.
        """
        current_index = self.preset_combobox.currentIndex()

        # Ensure a preset is selected
        if current_index == -1:
            QMessageBox.warning(self, "Error", "No preset selected to delete.")
            return

        # Ensure there's more than one preset in the combo box
        if self.preset_combobox.count() == 1:
            QMessageBox.warning(self, "Error", "At least one preset must remain. Cannot delete the last preset.")
            return

        # Get the current preset name
        preset_name = self.preset_combobox.itemText(current_index)

        # Show confirmation dialog
        confirm = QMessageBox.question(
            self,
            "Delete Preset",
            f"Are you sure you want to delete the preset '{preset_name}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirm != QMessageBox.Yes:
            return  # User chose not to delete

        session = get_session()

        try:
            # Fetch the preset from the database
            preset = session.query(GeneralPreset).filter_by(name=preset_name).first()

            if not preset:
                QMessageBox.warning(self, "Error", "Selected preset not found in the database.")
                return

            # Delete the preset (related rows in PresetGeneralAssignment are removed automatically)
            session.delete(preset)
            session.commit()

            # Remove the preset from the combo box
            self.preset_combobox.removeItem(current_index)

            # Update the preset_id with the newly selected preset
            new_selected_name = self.preset_combobox.currentText()  # Get the name of the newly selected preset
            new_selected_preset = session.query(GeneralPreset).filter_by(name=new_selected_name).first()

            if new_selected_preset:
                self.preset_id = new_selected_preset.id


        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Error", f"An error occurred while deleting the preset: {str(e)}")

        finally:
            session.close()