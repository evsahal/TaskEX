from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from gui.generated.generals_selection import Ui_GeneralsSelectionDialog


class GeneralsSelectionDialog(QDialog, Ui_GeneralsSelectionDialog):
    def __init__(self, parent):
        super(GeneralsSelectionDialog, self).__init__(parent)
        try:
            self.setupUi(self)

        except Exception as e:
            print(e)