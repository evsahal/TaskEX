import os
from PySide6.QtWidgets import QPushButton, QFileDialog, QLineEdit
from PySide6.QtGui import QIcon

class ImagePicker:
    """Class to manage image selection and removal with a toggle button."""

    def __init__(self, button: QPushButton, line_edit: QLineEdit):
        self.button = button
        self.line_edit = line_edit

        # Initial button setup
        self.default_icon = QIcon.fromTheme("folder-open")
        self.remove_icon = QIcon.fromTheme("window-close")

        self._setup_button()

    def _setup_button(self):
        """Set the button to file picker mode initially."""
        self.button.setIcon(self.default_icon)
        self.button.setStyleSheet("")  # Reset any styles
        self.button.clicked.connect(self._handle_button_click)

    def _handle_button_click(self):
        """Handle button clicks for selecting or removing the file."""
        if self.line_edit.property("file_path"):
            self._remove_file()
        else:
            self._select_file()

    def _select_file(self):
        """Open a file dialog to select an image and set the file path."""
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Open in read-only mode

        file_name, _ = QFileDialog.getOpenFileName(
            self.button,
            "Select Image File",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
            options=options,
        )

        if file_name:
            self.line_edit.setText(os.path.basename(file_name))
            self.line_edit.setProperty("file_path", file_name)
            self._switch_to_remove_mode()

    def _remove_file(self):
        """Clear the file path and switch the button back to file picker mode."""
        self.line_edit.clear()
        self.line_edit.setProperty("file_path", None)
        self._switch_to_picker_mode()

    def _switch_to_remove_mode(self):
        """Switch the button to show a remove icon and make it red."""
        self.button.setIcon(self.remove_icon)
        self.button.setStyleSheet("background-color: red; color: white;")

    def _switch_to_picker_mode(self):
        """Switch the button back to the file picker mode."""
        self.button.setIcon(self.default_icon)
        self.button.setStyleSheet("")

    def load_file(self, file_path: str):
        """Manually set the file path and switch the button to remove mode."""
        # self.line_edit.setText(os.path.basename(file_path))
        self.line_edit.setProperty("file_path", file_path)
        self._switch_to_remove_mode()
