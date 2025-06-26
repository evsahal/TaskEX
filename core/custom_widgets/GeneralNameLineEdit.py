import re
from PySide6.QtCore import Signal, QEvent, QTimer, Qt
from PySide6.QtWidgets import QLineEdit

from db.db_setup import get_session
from db.models import General


class GeneralNameLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    scan_console = Signal(str)

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
        # print(self.property('previous_text'))
        try:
            # Check if the name is same as before
            if self.text().strip() == self.property('previous_text'):
                event.ignore()
                return

            # Check if the string is empty or contains only whitespace
            if not self.text() or self.text().isspace():
                self.scan_console.emit("Name cannot be blank; please provide a valid name.")
                self.setText(self.property('previous_text'))
                event.ignore()
                return

            # Verify the name contains only alphabets, numbers, and hyphens
            pattern = "^[A-Za-z0-9- ]+$"
            if not re.match(pattern, self.text().strip()):
                self.scan_console.emit("Invalid Name; ensure the name contains only alphabets, numbers, and hyphens.")
                self.setText(self.property('previous_text'))
                event.ignore()
                return

            # Verify the name doesnt exist
            if self.name_exists_in_db(self.text().strip()):
                self.scan_console.emit("General with the same name already exists.")
                self.setText(self.property('previous_text'))
                event.ignore()
                return

            # Update the new name
            self.update_general_name_in_db(self.text().strip())

            # Update the new name
            self.setProperty('previous_text', self.text().strip())

        except Exception as e:
            print(e)

        super().focusOutEvent(event)

    def keyPressEvent(self, event):
        # Check if the Enter or Return key was pressed
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            # Remove focus from the QLineEdit
            self.clearFocus()
        else:
            super().keyPressEvent(event)

    def name_exists_in_db(self, name):
        """Check if the name exists in the database."""
        with get_session() as session:
            try:
                # Query the General table to check if the name already exists
                general_exists = session.query(General).filter(General.name == name).first()
                return general_exists is not None
            except Exception as e:
                print(f"Error checking database: {e}")
                return False

    def update_general_name_in_db(self, new_name):
        """Update the general's name in the database."""
        with get_session() as session:
            try:
                # Query the general by ID and update the name
                general = session.query(General).filter(General.id == self.property('general_id')).first()
                if general:
                    general.name = new_name
                    session.commit()
                    self.scan_console.emit(f"General name updated to '{new_name}'.")
                else:
                    self.scan_console.emit(f"Error: General with ID {self.property('general_id')} not found.")
            except Exception as e:
                session.rollback()  # Roll back if something goes wrong
                self.scan_console.emit(f"Error updating name: {e}")