import re
from PySide6.QtCore import Signal, QEvent, QTimer
from PySide6.QtWidgets import QLineEdit

class GeneralNameLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    updateDeleteObj = Signal(str)
    updateScanConsole = Signal(str)

    def mouseDoubleClickEvent(self, event):
        if self.isReadOnly():
            QTimer.singleShot(0, self.moveCursorToEnd)
        self.setReadOnly(False)
        super().mouseDoubleClickEvent(event)

    def moveCursorToEnd(self):
        self.end(False)

    def focusOutEvent(self, event):
        self.setReadOnly(True)
        self.deselect()
        try:
            # Check if the name is same as before
            if self.text().strip() == self.property('previousText'):
                event.ignore()
                return

            # Check if the string is empty or contains only whitespace
            if not self.text() or self.text().isspace():
                self.updateScanConsole.emit("Name cannot be blank; please provide a valid name.")
                self.setText(self.property('previousText'))
                event.ignore()
                return

            # Verify the name contains only alphabets, numbers, and hyphens
            pattern = "^[A-Za-z0-9- ]+$"
            if not re.match(pattern, self.text().strip()):
                self.updateScanConsole.emit("Invalid Name; ensure the name contains only alphabets, numbers, and hyphens.")
                self.setText(self.property('previousText'))
                event.ignore()
                return

            # Emit signal to update the delete button object name
            self.updateDeleteObj.emit(self.text().strip())
            self.setProperty('previousText', self.text().strip())

        except Exception as e:
            print(e)

        super().focusOutEvent(event)
