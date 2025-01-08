from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMessageBox

from db.db_setup import get_session
from db.models import GeneralPreset, JoinRallyPresetConfiguration, JoinRallyPresetOption
from gui.generated.preset_configuration import Ui_PresetConfigDialog
from gui.widgets.GeneralsSelectionDialog import GeneralsSelectionDialog


class PresetConfigDialog(QDialog, Ui_PresetConfigDialog):
    def __init__(self, parent,index):
        super(PresetConfigDialog, self).__init__(parent)
        self.profile_id = getattr(parent.widgets, f"emu_profile_{index}").currentData()
        self.general_preset_id = None  # To store the currently selected preset ID
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("Preset Configuration")
        self.setFixedSize(600, 730)
        self.setWindowModality(Qt.ApplicationModal)
        self.general_presets_btn.clicked.connect(self.open_manage_general_presets_dialog)
        self.cancel_preset_config_btn.clicked.connect(lambda: self.close())
        self.general_presets_btn.setIcon(QIcon(":/icons/images/icons/cil-settings.png"))

        # Connect combo box value change to update preset ID
        self.general_preset_combobox.currentIndexChanged.connect(self.update_preset_id)

        # Connect the save button to save the preset config
        self.save_preset_config_btn.clicked.connect(self.save_preset_config)

        # Populate the general_preset_combobox with preset names
        self.load_general_presets()

        # Load profile-specific preset options
        self.load_profile_preset_options()

    def load_general_presets(self):
        """
        Load general preset names from the database and populate the combo box.
        """
        session = get_session()
        try:
            # Temporarily disconnect the signal to prevent unwanted updates
            self.general_preset_combobox.blockSignals(True)

            # Query all general presets
            general_presets = session.query(GeneralPreset).all()

            # Clear the combo box before adding items
            self.general_preset_combobox.clear()

            # Populate combo box with preset names
            for preset in general_presets:
                self.general_preset_combobox.addItem(preset.name,preset.id)

            # Set the selected preset based on self.general_preset_id
            if self.general_preset_id is None:
                # If no preset_id is set, select the first option by default
                if general_presets:
                    self.general_preset_id = general_presets[0].id
                    self.general_preset_combobox.setCurrentIndex(0)
            else:
                # If preset_id is set, check if it exists in the new list
                matching_preset_index = next(
                    (index for index, preset in enumerate(general_presets) if preset.id == self.general_preset_id),
                    None
                )
                if matching_preset_index is not None:
                    # If found, select the matching preset
                    self.general_preset_combobox.setCurrentIndex(matching_preset_index)
                elif general_presets:
                    # If not found, fall back to the first option
                    self.general_preset_id = general_presets[0].id
                    self.general_preset_combobox.setCurrentIndex(0)
                else:
                    # If no presets exist, set preset_id to None
                    self.general_preset_id = None
        finally:
            # Reconnect the signal after loading
            self.general_preset_combobox.blockSignals(False)
            # Close the session to avoid connection issues
            session.close()

    def load_profile_preset_options(self):
        """
        Load the preset options and general preset ID based on the selected profile.
        """
        session = get_session()
        try:
            # Fetch the preset configuration for the selected profile
            preset_config = session.query(JoinRallyPresetConfiguration).filter_by(profile_id=self.profile_id).first()


            # Set the general preset ID and load the value to the combobox
            self.general_preset_id = preset_config.general_preset_id

            # Access the combobox
            general_preset_combobox = getattr(self, f"general_preset_combobox")

            # Find the index of the item with the data matching general_preset_id
            index = general_preset_combobox.findData(preset_config.general_preset_id)

            # If the index is valid, set it as the current index
            if index != -1:
                general_preset_combobox.setCurrentIndex(index)
            else:
                # Handle case where the ID is not found, e.g., set to the first item or show a warning
                general_preset_combobox.setCurrentIndex(0)


            # Fetch all preset options associated with this configuration
            preset_options = session.query(JoinRallyPresetOption).filter_by(
                preset_configuration_id=preset_config.id).all()

            # Populate the UI for each preset option
            for option in preset_options:
                # Access widgets dynamically by preset number
                use_generals_checkbox = getattr(self, f"preset_{option.preset_number}_option_1")
                skip_no_general_checkbox = getattr(self, f"preset_{option.preset_number}_option_2")
                reset_to_one_troop_checkbox = getattr(self,f"preset_{option.preset_number}_option_3")

                # Update the checkbox states based on the database values
                use_generals_checkbox.setChecked(option.use_selected_generals)
                skip_no_general_checkbox.setChecked(option.skip_no_general)
                reset_to_one_troop_checkbox.setChecked(option.reset_to_one_troop)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while loading presets: {e}")
        finally:
            # Ensure the session is closed
            session.close()


    def update_preset_id(self):
        """
        Update the preset ID when the combo box value changes.
        """
        self.general_preset_id = self.general_preset_combobox.currentData()

    def open_manage_general_presets_dialog(self):
        """
        Open the GeneralsSelectionDialog and pass the selected preset ID.
        """
        if self.general_preset_id is not None:
            general_selection_dialog = GeneralsSelectionDialog(self, self.general_preset_id)
            general_selection_dialog.exec()  # Use exec() for modal dialog

            # After the dialog closes, reload presets
            self.load_general_presets()
        else:
            QMessageBox.warning(self, "No Preset Selected", "Please select a valid preset before proceeding.")

    def save_preset_config(self):

        session = get_session()
        try:
            # Get the currently selected general preset ID from the combobox
            general_preset_id = self.general_preset_combobox.currentData()

            # Fetch the current preset configuration from the database
            preset_config = session.query(JoinRallyPresetConfiguration).filter_by(profile_id=self.profile_id).first()

            if not preset_config:
                # print("Preset configuration not found!")
                return

            # Update the general preset ID
            preset_config.general_preset_id = general_preset_id

            # Loop through all 8 presets to update their options
            for i in range(1, 9):
                # Dynamically get the preset frame and options
                frame_name = f"preset_frame_{i}"
                option_1_name = f"preset_{i}_option_1"
                option_2_name = f"preset_{i}_option_2"
                option_3_name = f"preset_{i}_option_3"

                # Ensure the frame exists (safe lookup)
                preset_frame = getattr(self, frame_name, None)
                if not preset_frame:
                    # print(f"Frame {frame_name} not found!")
                    continue

                # Retrieve options dynamically
                option_1 = getattr(self, option_1_name).isChecked()
                option_2 = getattr(self, option_2_name).isChecked()
                option_3 = getattr(self, option_3_name).isChecked()

                # Find the corresponding preset option in the database
                preset_option = (
                    session.query(JoinRallyPresetOption)
                    .filter_by(preset_configuration_id=preset_config.id, preset_number=i)
                    .first()
                )

                if preset_option:
                    # Update the options
                    preset_option.use_selected_generals = option_1
                    preset_option.skip_no_general = option_2
                    preset_option.reset_to_one_troop = option_3

            # Commit the changes to the database
            session.commit()
        except Exception as e:
            print(e)

        finally:
            # Close the session
            session.close()
            # Close the dialog
            self.close()
