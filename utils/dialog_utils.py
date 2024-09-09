from PySide6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


def show_confirmation_dialog(main_window, title="Confirm", message="Are you sure?"):
    """
    Shows a generic confirmation dialog.

    Args:
        main_window: The main window object.
        title (str): The title of the dialog window.
        message (str): The confirmation message to be displayed.

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    reply = QMessageBox.question(main_window, title,
                                 message,
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
    return reply == QMessageBox.Yes


def show_error_dialog(main_window, title="Error", message="An error occurred"):
    """
    Shows a custom error dialog.

    Args:
        main_window: The main window object.
        title (str): The title of the error dialog.
        message (str): The error message to be displayed.
    """
    # Create a custom dialog
    error_dialog = QDialog(main_window)
    error_dialog.setWindowTitle(title)

    # Set the size of the dialog
    # error_dialog.resize(300, 150)

    # Create layout and add widgets
    layout = QVBoxLayout()

    # Create a label to display the error message
    label = QLabel(message)

    label.setContentsMargins(20, 20, 20, 0)  # Add margins to the label (left, top, right, bottom)
    layout.addWidget(label)

    # Create an "OK" button and put it in an additional horizontal layout aligned to the right
    button_layout = QHBoxLayout()  # Horizontal layout to hold the button
    button_layout.addStretch()  # Adds space before the button to push it to the right
    ok_button = QPushButton("OK")
    ok_button.setMinimumHeight(40)
    ok_button.setMinimumWidth(100)
    ok_button.clicked.connect(error_dialog.accept)
    button_layout.addWidget(ok_button)

    # Add the button layout (with the button aligned to the right) to the main layout
    layout.addLayout(button_layout)

    # Apply custom styles
    error_dialog.setStyleSheet("""
        QDialog {
            background-color: rgb(40, 44, 52);
            color: rgb(221, 221, 221);
            font-size: 14px;
        }
        QLabel {
            font-size: 16px;
            margin-bottom: 20px;
        }
        QPushButton {
            border: 2px solid rgb(52, 59, 72);
            border-radius: 5px;	
            background-color: rgb(52, 59, 72);
        }
        QPushButton:hover {
            background-color: rgb(57, 65, 80);
            border: 2px solid rgb(61, 70, 86);
        }
        QPushButton:pressed {	
            background-color: rgb(35, 40, 49);
            border: 2px solid rgb(43, 50, 61);
        }

    """)

    # Set the layout to the dialog
    error_dialog.setLayout(layout)

    # Execute the dialog
    error_dialog.exec_()
