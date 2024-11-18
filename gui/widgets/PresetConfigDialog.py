from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from gui.generated.preset_configuration import Ui_PresetConfigDialog


class PresetConfigDialog(QDialog, Ui_PresetConfigDialog):
    def __init__(self, parent):
        super(PresetConfigDialog, self).__init__(parent)
        try:
            self.setupUi(self)
            self.setWindowTitle("Preset Configuration")
            self.setFixedSize(600, 670)
            self.setWindowModality(Qt.ApplicationModal)
            self.cancel_preset_config.clicked.connect(lambda: self.close())
            # self.show()

        except Exception as e:
            print(e)