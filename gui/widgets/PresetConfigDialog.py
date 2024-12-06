from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMessageBox

from db.db_setup import get_session
from db.models import GeneralPreset
from gui.generated.preset_configuration import Ui_PresetConfigDialog
from gui.widgets.GeneralsSelectionDialog import GeneralsSelectionDialog


class PresetConfigDialog(QDialog, Ui_PresetConfigDialog):
    def __init__(self, parent):
        super(PresetConfigDialog, self).__init__(parent)
        self.preset_data = []  # To store all preset data
        self.preset_id = None  # To store the currently selected preset ID
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("Preset Configuration")
        self.setFixedSize(600, 730)
        self.setWindowModality(Qt.ApplicationModal)
        self.general_presets_btn.clicked.connect(self.open_manage_general_presets_dialog)
        self.cancel_preset_config.clicked.connect(lambda: self.close())
        self.general_presets_btn.setIcon(QIcon(":/icons/images/icons/cil-settings.png"))

        # Connect combo box value change to update preset ID
        self.general_preset_combobox.currentIndexChanged.connect(self.update_preset_id)

        # Populate the general_preset_combobox with preset names
        self.load_general_presets()

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

            # Store preset data in a class variable
            self.preset_data = general_presets

            # Clear the combo box before adding items
            self.general_preset_combobox.clear()

            # Populate combo box with preset names
            for preset in general_presets:
                self.general_preset_combobox.addItem(preset.name)

            # Set the selected preset based on self.preset_id
            if self.preset_id is None:
                # If no preset_id is set, select the first option by default
                if general_presets:
                    self.preset_id = general_presets[0].id
                    self.general_preset_combobox.setCurrentIndex(0)
            else:
                # If preset_id is set, check if it exists in the new list
                matching_preset_index = next(
                    (index for index, preset in enumerate(general_presets) if preset.id == self.preset_id),
                    None
                )
                if matching_preset_index is not None:
                    # If found, select the matching preset
                    self.general_preset_combobox.setCurrentIndex(matching_preset_index)
                elif general_presets:
                    # If not found, fall back to the first option
                    self.preset_id = general_presets[0].id
                    self.general_preset_combobox.setCurrentIndex(0)
                else:
                    # If no presets exist, set preset_id to None
                    self.preset_id = None
        finally:
            # Reconnect the signal after loading
            self.general_preset_combobox.blockSignals(False)
            # Close the session to avoid connection issues
            session.close()

    def update_preset_id(self):
        """
        Update the preset ID when the combo box value changes.
        """
        selected_name = self.general_preset_combobox.currentText()
        for preset in self.preset_data:
            if preset.name == selected_name:
                self.preset_id = preset.id
                print(f"CP - 0 {self.preset_id}")
                break

    def open_manage_general_presets_dialog(self):
        """
        Open the GeneralsSelectionDialog and pass the selected preset ID.
        """
        if self.preset_id is not None:
            general_selection_dialog = GeneralsSelectionDialog(self, self.preset_id)
            general_selection_dialog.exec()  # Use exec() for modal dialog

            # After the dialog closes, reload presets
            self.load_general_presets()
        else:
            QMessageBox.warning(self, "No Preset Selected", "Please select a valid preset before proceeding.")

