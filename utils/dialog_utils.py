from PySide6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


def show_confirmation_dialog(main_window, title="Confirm", message="Are you sure?"):
    """
    Shows a custom confirmation dialog with custom size and styles.

    Args:
        main_window: The main window object.
        title (str): The title of the confirmation dialog.
        message (str): The confirmation message to be displayed.

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    # Create a custom dialog
    confirmation_dialog = QDialog(main_window)
    confirmation_dialog.setWindowTitle(title)

    # Create the main vertical layout
    layout = QVBoxLayout()

    # Create a label to display the confirmation message with word wrapping and margins
    label = QLabel(message)
    # label.setWordWrap(True)  # Enable word wrapping for long messages
    label.setContentsMargins(20, 20, 20, 0)  # Add margins to the label (left, top, right, bottom)
    layout.addWidget(label)

    # Create a layout for the "Yes" and "No" buttons
    button_layout = QHBoxLayout()  # Horizontal layout to hold the buttons
    button_layout.addStretch()  # Adds space before the buttons to push them to the right

    # Create the "Yes" button
    yes_button = QPushButton("Yes")
    yes_button.setMinimumHeight(40)
    yes_button.setMinimumWidth(100)
    yes_button.clicked.connect(confirmation_dialog.accept)  # Close dialog and return True
    button_layout.addWidget(yes_button)

    # Create the "No" button
    no_button = QPushButton("No")
    no_button.setMinimumHeight(40)
    no_button.setMinimumWidth(100)
    no_button.clicked.connect(confirmation_dialog.reject)  # Close dialog and return False
    button_layout.addWidget(no_button)

    # Add the button layout (aligned to the right) to the main layout
    layout.addLayout(button_layout)

    # Apply custom styles (same as the error dialog)
    confirmation_dialog.setStyleSheet("""
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
    confirmation_dialog.setLayout(layout)

    # Execute the dialog and return the result (True if "Yes" is clicked, False if "No" is clicked)
    result = confirmation_dialog.exec_()

    return result == QDialog.Accepted

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
