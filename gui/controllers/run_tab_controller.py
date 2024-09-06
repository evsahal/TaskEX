from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QAbstractItemView


def setup_scheduler_table(self, index):
    # Accessing the scheduler table
    scheduler_table = getattr(self.widgets, f"scheduler_table_{index}")



    # Hide the vertical header (row numbers)
    scheduler_table.verticalHeader().setVisible(False)

    # Set the selection behavior to select only cells, not entire rows
    scheduler_table.setSelectionBehavior(QAbstractItemView.SelectItems)

    # Stretch the first column
    scheduler_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    # Align the last column (Actions) to the right, with a fixed size or interactive resizing
    scheduler_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

    # Set the height of the horizontal header
    scheduler_table.horizontalHeader().setFixedHeight(40)

    # Add the footer row with "Add Task" button
    add_footer(scheduler_table)


def add_footer(scheduler_table):
    # Insert a footer row (at the bottom)
    footer_row = scheduler_table.rowCount()
    scheduler_table.insertRow(footer_row)

    # Set the height of the footer row
    scheduler_table.setRowHeight(footer_row, 40)

    # Create the "Add Task" button and set it in the footer row
    add_task_button = QPushButton("Add Task")
    add_task_button.setMinimumHeight(40)
    add_task_button.clicked.connect(lambda: add_new_task(scheduler_table))

    # Create a QWidget to hold the button and span across two columns
    button_widget = QWidget()
    layout = QHBoxLayout(button_widget)
    layout.addWidget(add_task_button)
    # Remove margins around the button
    layout.setContentsMargins(0, 0, 0, 0)
    button_widget.setLayout(layout)

    # Span the button across both columns (0 and 1)
    scheduler_table.setCellWidget(footer_row, 0, button_widget)
    # Span across both columns
    scheduler_table.setSpan(footer_row, 0, 1, 2)

    # Disable selection for the entire footer row
    for col in range(scheduler_table.columnCount()):
        item = QTableWidgetItem()
        # Disable selection, but keep the item enabled
        item.setFlags(Qt.ItemIsEnabled)
        scheduler_table.setItem(footer_row, col, item)


def add_new_task(scheduler_table):
    # Insert a new row above the footer
    row_position = scheduler_table.rowCount() - 1  # Insert before the footer row
    scheduler_table.insertRow(row_position)

    # Set the height of the new row to 40
    scheduler_table.setRowHeight(row_position, 40)

    # Add Task Name to the first column
    task_item = QTableWidgetItem("New Task")
    task_item.setFlags(task_item.flags() | Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Ensure it's selectable
    scheduler_table.setItem(row_position, 0, task_item)

    # Create a delete button for the second column (Actions)
    delete_button = QPushButton()
    delete_button.setIcon(QIcon(":/icons/images/icons/icon_delete_3.png"))
    delete_button.setStyleSheet("background-color:transparent;")

    # Connect the button to remove the row
    delete_button.clicked.connect(lambda: scheduler_table.removeRow(row_position))

    # Set the delete button in the second column
    scheduler_table.setCellWidget(row_position, 1, delete_button)

    # Disable selection for the "Actions" column (second column)
    non_selectable_item = QTableWidgetItem()
    # Disable selection for the actions column
    non_selectable_item.setFlags(Qt.ItemIsEnabled)
    scheduler_table.setItem(row_position, 1, non_selectable_item)
