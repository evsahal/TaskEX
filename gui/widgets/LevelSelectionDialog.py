from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QScrollArea, QWidget, QGridLayout
)
from PySide6.QtCore import Qt


class LevelSelectionDialog(QDialog):
    def __init__(self, selected_ids, level_data, preview_name, parent=None):
        """
        Dialog for selecting levels with group checkboxes.

        :param selected_ids: Previously selected level IDs.
        :param level_data: List of MonsterLevel objects containing level details.
        :param preview_name: Boss preview name for dialog title.
        """
        super().__init__(parent)
        self.setWindowTitle(preview_name)
        self.resize(750, 570)

        # Store selected level IDs
        self.selected_ids = set(selected_ids)
        self.level_data = level_data

        # Main layout
        main_layout = QVBoxLayout(self)

        # Scrollable area for levels
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        self.level_layout = QVBoxLayout(content_widget)

        # Group levels dynamically
        self.checkboxes = {}  # Level ID -> Checkbox
        self.group_checkboxes = {}  # Group Range -> Group Checkbox
        self.create_level_groups()

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

        # Buttons
        button_layout = QHBoxLayout()
        select_button = QPushButton("Select")
        select_button.setMinimumHeight(40)
        select_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.setMinimumHeight(40)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(select_button)
        button_layout.addWidget(cancel_button)
        main_layout.addLayout(button_layout)

    def create_level_groups(self):
        """
        Groups levels into batches of 10 and adds checkboxes.
        """
        levels_per_group = 10
        total_levels = len(self.level_data)

        for group_start in range(0, total_levels, levels_per_group):
            group_end = min(group_start + levels_per_group, total_levels)
            group_label = f"Skip Levels {self.level_data[group_start].level} - {self.level_data[group_end - 1].level}"
            group_box = QCheckBox(group_label)

            # Connect group checkbox with a proper function to avoid lambda issues
            self.connect_group_checkbox(group_box, group_start, group_end)
            self.level_layout.addWidget(group_box)

            # Track group checkboxes
            self.group_checkboxes[(group_start, group_end)] = group_box

            # Add checkboxes for each level in the group
            grid_layout = QGridLayout()
            for i, level in enumerate(self.level_data[group_start:group_end]):
                checkbox = QCheckBox(f"Level {level.level} ({level.power})")
                checkbox.setChecked(level.id in self.selected_ids)
                checkbox.stateChanged.connect(self.update_group_checkbox_state)
                grid_layout.addWidget(checkbox, i // 5, i % 5)  # 5 checkboxes per row

                # Track checkboxes by level ID
                self.checkboxes[level.id] = checkbox

            self.level_layout.addLayout(grid_layout)

    def connect_group_checkbox(self, group_box, group_start, group_end):
        """
        Connect the group checkbox to toggle the checkboxes in its range.
        """
        group_box.stateChanged.connect(lambda state: self.toggle_group(state, group_start, group_end))

    def toggle_group(self, state, group_start, group_end):
        """
        Toggle all checkboxes in a group when 'Select All' is checked/unchecked.
        """
        levels = self.level_data[group_start:group_end]

        # Check the state and update the individual checkboxes
        if state == 1:  # Qt.Checked (all checkboxes should be checked)
            for level in levels:
                checkbox = self.checkboxes[level.id]
                checkbox.blockSignals(True)
                checkbox.setChecked(True)
                checkbox.blockSignals(False)

        elif state == 0:  # Qt.Unchecked (all checkboxes should be unchecked)
            for level in levels:
                checkbox = self.checkboxes[level.id]
                checkbox.blockSignals(True)
                checkbox.setChecked(False)
                checkbox.blockSignals(False)

        elif state == 2:  # Qt.PartiallyChecked (should behave as partial check)
            for level in levels:
                checkbox = self.checkboxes[level.id]
                checkbox.blockSignals(True)
                checkbox.setChecked(True)
                checkbox.blockSignals(False)


        # After modifying individual checkboxes, update the state of the group checkbox
        self.update_group_checkbox_state()


    def update_group_checkbox_state(self):
        """
        Update the state of 'Select All' group checkboxes dynamically.
        """
        for (group_start, group_end), group_box in self.group_checkboxes.items():
            levels = self.level_data[group_start:group_end]
            all_checked = all(self.checkboxes[level.id].isChecked() for level in levels)
            any_checked = any(self.checkboxes[level.id].isChecked() for level in levels)

            group_box.blockSignals(True)
            if all_checked:
                group_box.setCheckState(Qt.Checked)
            elif any_checked:
                group_box.setCheckState(Qt.PartiallyChecked)
            else:
                group_box.setCheckState(Qt.Unchecked)
            group_box.blockSignals(False)

        self.update_selected_ids()

    def update_selected_ids(self):
        """
        Update the set of selected level IDs.
        """
        self.selected_ids = {level_id for level_id, checkbox in self.checkboxes.items() if checkbox.isChecked()}
