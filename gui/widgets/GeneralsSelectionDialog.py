from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QHBoxLayout

from gui.generated.generals_selection import Ui_GeneralsSelectionDialog


class GeneralsSelectionDialog(QDialog, Ui_GeneralsSelectionDialog):
    def __init__(self, parent):
        super(GeneralsSelectionDialog, self).__init__(parent)

        self.setupUi(self)
        self.connect_preset_buttons()

    def connect_preset_buttons(self):
        # Initialize event connections
        self.edit_btn.clicked.connect(self.enable_edit_mode)
        self.delete_btn.clicked.connect(self.delete_preset)
        self.add_btn.clicked.connect(self.add_new_preset)

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
        new_name = preset_line_edit.text()

        if new_name.strip():  # Add only if the name is not empty
            self.preset_combobox.addItem(new_name)
            self.preset_combobox.setCurrentIndex(self.preset_combobox.count() - 1)

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
        new_name = preset_line_edit.text()

        # Update combo box with the new name
        current_index = self.preset_combobox.currentIndex()
        self.preset_combobox.setItemText(current_index, new_name)

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
        Delete the currently selected preset from the combo box.
        """
        current_index = self.preset_combobox.currentIndex()

        if current_index != -1:
            self.preset_combobox.removeItem(current_index)