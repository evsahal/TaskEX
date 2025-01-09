from PySide6.QtWidgets import QDialog, QMessageBox

from gui.generated.march_speed_selection import Ui_MarchSpeedSelectionJRDialog

class MarchSpeedSelectionJRDialog(QDialog, Ui_MarchSpeedSelectionJRDialog):
    def __init__(self, parent, button, index):
        super(MarchSpeedSelectionJRDialog, self).__init__(parent)
        self.button = button  # Reference to the button with settings
        self.index = index
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

        # Load the settings from the button's config_values
        settings = self.button.property('config_values')
        self.use_free_boost.setChecked(settings["use_free_boost"])
        self.use_free_boost_gems.setChecked(settings["use_free_boost_gems"])
        self.boost_hours.setValue(settings["boost_hours"])
        self.boost_repeat_times.setValue(settings["boost_repeat_times"])

        # Connect update button to save changes
        self.update_settings_btn.clicked.connect(self.update_settings)

        # Connect exit button
        self.exit_btn.clicked.connect(self.close)

    def update_settings(self):
        # Update the button's config_values with the current dialog values
        self.button.setProperty('config_values',{
            "use_free_boost": self.use_free_boost.isChecked(),
            "use_free_boost_gems": self.use_free_boost_gems.isChecked(),
            "boost_hours": self.boost_hours.value(),
            "boost_repeat_times": self.boost_repeat_times.value(),
        })

        # Show confirmation message
        QMessageBox.information(self, "Settings Updated", "March speed settings have been updated.")
        self.close()
