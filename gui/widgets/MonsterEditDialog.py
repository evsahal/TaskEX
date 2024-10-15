import os
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QMessageBox, QWidget
from sqlalchemy.orm import joinedload

from db.db_setup import get_session
from db.models import BossMonster, MonsterCategory, MonsterLogic, MonsterLevel, MonsterImage
from gui.generated.monster_edit_dialog import Ui_Monster_Edit_Dialog
from utils.helper_utils import image_chooser

class MonsterEditDialog(QDialog, Ui_Monster_Edit_Dialog):
    # Signal emitted when a monster is updated
    monster_updated = Signal(int)

    def __init__(self, monster_id=None, parent=None):
        super(MonsterEditDialog, self).__init__(parent)
        self.setupUi(self)

        self.monster_id = monster_id  # None for new monsters, ID for editing
        self.monster = None
        self.previous_logic = None
        self.level_rows = []  # Keep track of dynamically added levels

        # Set up scroll area for monster levels
        self.init_level_scroll_area()

        # Connect signals
        self.save_changes_btn.clicked.connect(self.save_changes_pressed)
        self.cancel_btn.clicked.connect(self.cancel_dialog)
        self.add_level_btn.clicked.connect(self.handle_add_new_level)
        self.browse_preview_btn.clicked.connect(lambda: image_chooser(self.browse_preview_btn, self.preview_image_line_edit))
        self.browse_540p_btn.clicked.connect(lambda: image_chooser(self.browse_540p_btn, self.p540_image_line_edit))
        self.logic_combo_box.currentTextChanged.connect(self.handle_logic_change)
        self.map_scan_checkbox.stateChanged.connect(self.toggle_map_scan_fields)

        # Populate fields with initial data
        self.populate_field_data()

    def populate_field_data(self):
        """Populate category and logic combo boxes, and load existing monster data if editing."""
        session = get_session()
        categories = session.query(MonsterCategory).all()
        logics = session.query(MonsterLogic).all()

        # Populate category combo box
        self.category_combo_box.clear()
        for category in categories:
            self.category_combo_box.addItem(category.name, category.id)

        # Populate logic combo box
        self.logic_combo_box.clear()
        for logic in logics:
            self.logic_combo_box.addItem(logic.logic, logic.id)

        # Load monster data if editing an existing one
        if self.monster_id is not None:
            self.load_monster_data(session)
        session.close()

    def load_monster_data(self, session):
        """Load the existing data for the selected boss monster."""
        monster_data = self.get_monster_data(session)
        if not monster_data:
            return

        # Populate fields with the monster's data
        self.monster = monster_data
        self.preview_name_line_edit.setText(monster_data.preview_name)

        # Populate the combo boxes
        self.category_combo_box.setCurrentIndex(self.category_combo_box.findData(monster_data.monster_category_id))
        self.logic_combo_box.setCurrentIndex(self.logic_combo_box.findData(monster_data.monster_logic_id))

        # Map scan checkbox
        self.map_scan_checkbox.setChecked(monster_data.enable_map_scan)

        # Load image data
        if monster_data.monster_image:
            self.preview_image_line_edit.setText(monster_data.monster_image.preview_image)
            if self.map_scan_checkbox.isChecked():
                self.p540_image_line_edit.setText(monster_data.monster_image.img_540p)
                self.threshold_spin_box.setValue(monster_data.monster_image.img_threshold)
                click_pos = monster_data.monster_image.click_pos.split(',')
                self.click_x_spin_box.setValue(int(click_pos[0]))
                self.click_y_spin_box.setValue(int(click_pos[1]))


        # Load monster levels
        for level in monster_data.levels:
            self.add_new_level(level_number=level.level, name=level.name, power=level.power)

    def get_monster_data(self, session):
        """Fetch all the related data for the given monster ID."""
        return session.query(BossMonster).options(
            joinedload(BossMonster.monster_category),
            joinedload(BossMonster.monster_image),
            joinedload(BossMonster.monster_logic),
            joinedload(BossMonster.levels)
        ).filter(BossMonster.id == self.monster_id).one_or_none()

    def handle_logic_change(self):
        """Handle changes in logic combo box."""
        current_logic = self.logic_combo_box.currentText()

        if current_logic == 'Single-Level Boss' and len(self.level_rows) > 1:
            reply = QMessageBox.question(self, "Change to Single Level Boss",
                                         "There are more than 1 level. Switching to Single Level Boss Logic will remove additional levels. Do you want to proceed?",
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.clear_extra_levels()
            else:
                self.logic_combo_box.blockSignals(True)
                self.logic_combo_box.setCurrentText(self.previous_logic)
                self.logic_combo_box.blockSignals(False)

        self.previous_logic = current_logic

    def toggle_map_scan_fields(self, state):
        """Enable or disable fields based on the map scan checkbox state."""
        # When checked, enable fields; when unchecked, disable them.
        # is_checked = state != Qt.Checked  # True if checked, False if unchecked
        toggle = False if state == 0 else True
        # print(toggle)
        # Enable or disable the related fields based on the checkbox state
        self.p540_image_line_edit.setEnabled(toggle)
        self.browse_540p_btn.setEnabled(toggle)
        self.threshold_spin_box.setEnabled(toggle)
        self.find_template_btn.setEnabled(toggle)
        self.click_x_spin_box.setEnabled(toggle)
        self.click_y_spin_box.setEnabled(toggle)
        self.simulate_click_btn.setEnabled(toggle)
        self.choose_emulator_combo_box.setEnabled(toggle)
        self.map_template_btn.setEnabled(toggle)

    def clear_extra_levels(self):
        """Clear all but the first level."""
        while len(self.level_rows) > 1:
            row_layout, *_ = self.level_rows.pop()
            self.delete_row(row_layout)

    def init_level_scroll_area(self):
        """Initialize the scroll area where levels will be dynamically added."""
        # Assuming level_scrollArea is defined in the .ui file and linked with the UI object
        self.level_scrollArea.setWidgetResizable(True)  # Make the scroll area resizable

        # Create a widget that will hold the scroll area content (levels)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)  # Vertical layout for levels inside the scroll

        # Set the widget for the QScrollArea to hold the scroll widget
        self.level_scrollArea.setWidget(self.scroll_widget)

        # Add the first row (if creating a new monster, otherwise rows will be preloaded)
        if self.monster_id is None:
            self.add_new_level()  # Add an initial level when creating a new monster

        # Adjust layout to remove extra space between rows
        self.scroll_layout.setSpacing(5)
        self.scroll_layout.setAlignment(Qt.AlignTop)  # Ensure alignment to the top

    def handle_add_new_level(self):
        """Handle adding a new level."""
        if self.logic_combo_box.currentText() == 'Single-Level Boss' and len(self.level_rows) >= 1:
            QMessageBox.warning(self, "Level Limit Reached",
                                "You cannot add more levels when the logic is 'Single-Level Boss'.")
            return

        # Proceed to add a level
        if self.smart_mode_check_box.isChecked():
            self.add_new_level_smart_mode()
        else:
            self.add_new_level()

    def add_new_level(self, level_number='', name='', power=''):
        """Add a new row for monster level input."""
        row_layout = QHBoxLayout()

        # Level input
        level_input = QLineEdit(str(level_number))
        level_input.setPlaceholderText("Level")
        level_input.setMinimumHeight(40)

        # Name input
        name_input = QLineEdit(name)
        name_input.setPlaceholderText("Name")
        name_input.setMinimumHeight(40)

        # Power input
        power_input = QLineEdit(str(power))
        power_input.setPlaceholderText("Power")
        power_input.setMinimumHeight(40)

        # Delete button
        delete_button = QPushButton()
        delete_button.setIcon(QIcon(":/icons/images/icons/icon_delete_3.png"))
        delete_button.setMinimumHeight(40)
        delete_button.setMinimumWidth(40)
        delete_button.setProperty("action", "delete")  # Set action to 'delete'
        delete_button.clicked.connect(lambda: self.delete_row(row_layout))

        # Add to layout
        row_layout.addWidget(level_input)
        row_layout.addWidget(name_input)
        row_layout.addWidget(power_input)
        row_layout.addWidget(delete_button)

        # Adjust stretch factors for proper alignment
        row_layout.setStretch(0, 1)  # Level input
        row_layout.setStretch(1, 10)  # Name input
        row_layout.setStretch(2, 3)  # Power input
        row_layout.setStretch(3, 2)  # Delete button

        # Add the row to the scroll layout
        self.scroll_layout.addLayout(row_layout)

        # Store the row data for later reference
        self.level_rows.append((row_layout, level_input, name_input, power_input))

    def add_new_level_smart_mode(self):
        boss_name = ''
        logic = self.logic_combo_box.currentText()

        # Check if there are existing levels and find the highest level
        # for row in self.level_rows:
        #     level_no = row[1].text()
        #     name = row[2].text()
        #     power = row[3].text()
        if self.level_rows:
            # Extract the levels from level_rows and find the maximum
            current_level = [level[1].text() for level in self.level_rows]
            next_level = int(max(current_level)) + 1  # Increment the highest level by 1
        else:
            next_level = 1  # If no levels exist, start from level 1

        if logic == 'Multi-Level Boss' or logic == 'Custom-Level Boss':
            boss_name = [level[2].text() for level in self.level_rows][0]

        self.add_new_level(str(next_level),boss_name)

    def delete_row(self, row_layout):
        """Delete the selected row from the level layout."""
        for i in reversed(range(row_layout.count())):
            widget_to_remove = row_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.deleteLater()

        self.level_rows = [row for row in self.level_rows if row[0] != row_layout]

    def save_changes_pressed(self):
        """Save the monster or update an existing one."""
        if not self.validate_inputs():
            QMessageBox.warning(self, "Validation Error", "Please fill in all required fields.")
            return

        session = get_session()

        if self.monster_id is None:
            # Create new monster
            self.monster = BossMonster()
            self.monster.monster_image = MonsterImage()
        else:
            # Edit existing monster
            self.monster = session.query(BossMonster).filter(BossMonster.id == self.monster_id).one()

        # Save basic info
        self.monster.preview_name = self.preview_name_line_edit.text()
        self.monster.monster_category_id = self.category_combo_box.currentData()
        self.monster.monster_logic_id = self.logic_combo_box.currentData()

        # Save image data
        self.monster.monster_image.preview_image = self.preview_image_line_edit.text()
        self.monster.monster_image.img_540p = self.p540_image_line_edit.text()
        self.monster.monster_image.img_threshold = self.threshold_spin_box.value()
        self.monster.monster_image.click_pos = f"{self.click_x_spin_box.value()},{self.click_y_spin_box.value()}"

        # Save monster levels
        self.save_monster_levels()

        if not self.monster_id:
            # Close  the dialog
            self.accept()
            # Return the new monster object without saving
            return self.monster
        # Commit changes for existing monsters
        try:
            session.add(self.monster)
            session.commit()
            self.monster_updated.emit(self.monster_id)
            QMessageBox.information(self, "Success", "Monster updated successfully!")
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Error", f"Failed to save the monster: {e}")
        finally:
            session.close()
            self.accept()



    def save_monster_levels(self):
        """Handle saving levels for the monster."""
        existing_levels = {level.id: level for level in self.monster.levels} if self.monster.levels else {}

        ui_level_ids = []
        for level_row in self.level_rows:
            level_number = level_row[1].text().strip()
            name = level_row[2].text().strip()
            power = level_row[3].text().strip()

            # Check if the level exists in the current levels
            if hasattr(level_row[1], 'level_id'):
                level_id = level_row[1].level_id
                if level_id in existing_levels:
                    # Update the existing level
                    monster_level = existing_levels[level_id]
                    monster_level.level = level_number
                    monster_level.name = name
                    monster_level.power = power
                    ui_level_ids.append(level_id)
            else:
                # Add new level if it's a new entry
                new_level = MonsterLevel(level=level_number, name=name, power=power)
                self.monster.levels.append(new_level)

        # Find levels to delete (existing levels that are not in the UI)
        levels_to_delete = [level for level_id, level in existing_levels.items() if level_id not in ui_level_ids]
        for level in levels_to_delete:
            self.monster.levels.remove(level)

    def validate_inputs(self):
        """Validate the form inputs before saving."""
        if not self.preview_name_line_edit.text().strip():
            return False
        if self.category_combo_box.currentIndex() == -1:
            return False
        if self.logic_combo_box.currentIndex() == -1:
            return False
        if self.map_scan_checkbox.isChecked() and not self.p540_image_line_edit.text().strip():
            return False
        return True

    def get_monster(self):
        """Return the monster object created in the dialog."""
        return self.monster


    def cancel_dialog(self):
        """Close the dialog without saving."""
        self.reject()

