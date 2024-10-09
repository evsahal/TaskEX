from math import trunc

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, \
    QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from requests import session
from sqlalchemy.orm import joinedload

from db.db_setup import get_session
from db.models import BossMonster, MonsterCategory, MonsterLogic, MonsterLevel
from gui.generated.monster_edit_dialog import Ui_Monster_Edit_Dialog
from utils.helper_utils import image_chooser


class MonsterEditDialog(QDialog, Ui_Monster_Edit_Dialog):
    monster_updated = Signal(int)
    def __init__(self, monster_id=None, parent=None):
        super(MonsterEditDialog, self).__init__(parent)
        self.setupUi(self)

        self.monster_id = monster_id  # To track if we are editing an existing monster
        self.level_rows = []  # To track the rows added dynamically

        # Initialize the scroll area and its content layout
        self.init_level_scroll_area()

        # Connect the buttons
        self.save_changes_btn.clicked.connect(self.save_monster_config)
        self.cancel_btn.clicked.connect(self.cancel_dialog)
        self.add_level_btn.clicked.connect(self.handle_add_new_level)
        self.browse_preview_btn.clicked.connect(lambda :image_chooser(self.browse_preview_btn,self.preview_image_line_edit))
        self.browse_540p_btn.clicked.connect(lambda :image_chooser(self.browse_540p_btn,self.p540_image_line_edit))
        self.map_scan_checkbox.stateChanged.connect(self.toggle_map_scan_fields)

        # Logic Combo Box change event to handle switching between logics
        self.logic_combo_box.currentTextChanged.connect(self.handle_logic_change)


        # Load initial data
        self.previous_logic = None
        session = get_session()
        categories = session.query(MonsterCategory).all()
        logics = session.query(MonsterLogic).all()
        session.close()

        # Populate category combo box
        self.category_combo_box.clear()  # Clear any existing items
        for category in categories:
            self.category_combo_box.addItem(category.name, category.id)  # Add category name and ID

        # Populate logic combo box
        self.logic_combo_box.clear()  # Clear any existing items
        for logic in logics:
            self.logic_combo_box.addItem(logic.logic, logic.id)  # Add logic name and ID


        # Load monster data if editing an existing one
        if self.monster_id is not None:
            self.load_monster_data()

    def handle_logic_change(self):
        """Handle changes in logic combo box."""
        current_logic = self.logic_combo_box.currentText()

        # Check if the current selection is "Single Level Boss" and if there are multiple levels
        if current_logic == 'Single-Level Boss' and len(self.level_rows) > 1:
            reply = QMessageBox.question(self, "Change to Single Level Boss",
                                         "There are more than 1 level. Switching to Single Level Boss Logic will remove additional levels. Do you want to proceed?",
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                # Clear extra levels and continue
                self.clear_extra_levels()
            else:
                # Revert to the previous logic
                self.logic_combo_box.blockSignals(True)  # Temporarily block signals to avoid recursive calls
                self.logic_combo_box.setCurrentText(self.previous_logic)
                self.logic_combo_box.blockSignals(False)
                return  # Don't proceed further

        # Update the previous logic after handling the change
        self.previous_logic = current_logic

    def clear_extra_levels(self):
        """Clear all but the first level."""
        while len(self.level_rows) > 1:
            row_layout, *_ = self.level_rows.pop()
            self.delete_row(row_layout)  # Delete the extra rows

    def handle_add_new_level(self):
        """Handle adding a new level."""
        if self.logic_combo_box.currentText() == 'Single-Level Boss' and len(self.level_rows) >= 1:
            QMessageBox.warning(self, "Level Limit Reached",
                                "You cannot add more levels when the logic is 'Single-Level Boss'.")
            return

        # Proceed to add a level
        if self.smart_mode_check_box.isChecked():
            self.add_new_level_with_pre_data()
        else:
            self.add_new_level()

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

    def add_new_level_with_pre_data(self):
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

    def add_new_level(self, level_number='', name='', power=''):
        """Add a new row for level input with delete icon."""
        row_layout = QHBoxLayout()

        # Create input widgets
        level_input = QLineEdit(str(level_number))
        level_input.setPlaceholderText("Lv")
        level_input.setMinimumHeight(40)

        name_input = QLineEdit(name)
        name_input.setPlaceholderText("Name")
        name_input.setMinimumHeight(40)

        power_input = QLineEdit(str(power))
        power_input.setPlaceholderText("Power")
        power_input.setMinimumHeight(40)

        # Create the delete button
        delete_button = QPushButton()
        delete_button.setIcon(QIcon(":/icons/images/icons/icon_delete_3.png"))
        delete_button.setMinimumHeight(40)
        delete_button.setMinimumWidth(40)
        delete_button.setProperty("action", "delete")  # Set action to 'delete'
        delete_button.clicked.connect(lambda: self.delete_row(row_layout))

        # Add widgets to row layout
        row_layout.addWidget(level_input)
        row_layout.addWidget(name_input)
        row_layout.addWidget(power_input)
        row_layout.addWidget(delete_button)

        # Adjust stretch factors for proper alignment
        row_layout.setStretch(0, 1)  # Level input
        row_layout.setStretch(1, 10)  # Name input
        row_layout.setStretch(2, 3)  # Power input
        row_layout.setStretch(3, 2)  # Delete button

        # Add row to scroll layout (this is the layout inside the scroll area)
        self.scroll_layout.addLayout(row_layout)

        # Store the row for tracking and access later
        self.level_rows.append((row_layout, level_input, name_input, power_input, delete_button))

    def delete_row(self, row_layout):
        """Remove a row from the scroll area."""
        for i in reversed(range(row_layout.count())):
            widget_to_remove = row_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.deleteLater()

        # Remove the row from the tracking list
        self.level_rows = [row for row in self.level_rows if row[0] != row_layout]

    def load_monster_data(self):
        """Load the monster's existing data when editing."""
        session = get_session()
        monster_data = self.get_monster_data(session, self.monster_id)
        session.close()
        if not monster_data:
            return None
        self.preview_name_line_edit.setText(monster_data.preview_name)

        # Access category data
        if monster_data.monster_category:
            # print("Category: ", monster_data.monster_category.name)
            self.category_combo_box.setCurrentText(monster_data.monster_category.name)

        # Access logic data
        if monster_data.monster_logic:
            # print("Logic: ", monster_data.monster_logic.logic)
            self.logic_combo_box.setCurrentText(monster_data.monster_logic.logic)

        # map scan check box
        # print(f"Map Scan: {monster_data.enable_map_scan}")
        self.map_scan_checkbox.setChecked(monster_data.enable_map_scan)

        # Access preview image data
        if monster_data.monster_image:
            # print("Image preview: ", monster_data.monster_image.preview_image)
            self.preview_image_line_edit.setText(monster_data.monster_image.preview_image)

        # Access 540p image data
        if monster_data.monster_image.img_540p:
            # print("Image preview: ", monster_data.monster_image.img_540p)
            self.p540_image_line_edit.setText(monster_data.monster_image.img_540p)

        # Access threshold data
        if monster_data.monster_image.img_threshold:
            self.threshold_spin_box.setValue(monster_data.monster_image.img_threshold)

        # Access click pos data
        if monster_data.monster_image.click_pos:
            # print(monster_data.monster_image.click_pos.split(","))
            # print(monster_data.monster_image.click_pos.split(",")[0])
            self.click_x_spin_box.setValue(int(monster_data.monster_image.click_pos.split(",")[0]))
            self.click_y_spin_box.setValue(int(monster_data.monster_image.click_pos.split(",")[1]))

        # Access level data
        for level in monster_data.levels:
            # print(f"Level {level.level}: {level.name}, Power: {level.power}")
            self.add_new_level(level.level, level.name, level.power)

    def get_monster_data(self,session, boss_monster_id):
        """Fetch all related data for a given boss_monster_id and return as ORM objects."""

        return  session.query(BossMonster).options(
            joinedload(BossMonster.monster_category),
            joinedload(BossMonster.monster_image),
            joinedload(BossMonster.monster_logic),
            joinedload(BossMonster.levels)
        ).filter(BossMonster.id == boss_monster_id).one_or_none()

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

    def save_monster_config(self):
        """Save the monster configuration."""
        if not self.validate_inputs():
            QMessageBox.warning(self, "Input Validation", "Please ensure all required fields are filled out correctly.")
            return

        session = get_session()

        if self.monster_id is None:
            monster = BossMonster()
        else:
            monster = session.query(BossMonster).filter(BossMonster.id == self.monster_id).one()

        # Save basic monster info
        monster.preview_name = self.preview_name_line_edit.text()
        monster.monster_category_id = self.category_combo_box.currentData()
        monster.monster_logic_id = self.logic_combo_box.currentData()

        # Save monster image info
        monster.monster_image.preview_image = self.preview_image_line_edit.text()
        monster.monster_image.image_540p = self.p540_image_line_edit.text()
        monster.monster_image.img_threshold = self.threshold_spin_box.value()
        # Combine click_x and click_y into click_pos
        click_x = self.click_x_spin_box.value()  # Get the click x coordinate
        click_y = self.click_y_spin_box.value()  # Get the click y coordinate
        monster.monster_image.click_pos = f"{click_x},{click_y}"


        # Save additional level information
        self.save_monster_levels(monster, session)

        # Commit the transaction
        try:
            session.add(monster)
            session.commit()
            QMessageBox.information(self, "Save Successful", "Monster configuration has been saved successfully!")
            self.monster_updated.emit(self.monster_id)
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Save Error", f"Failed to save monster configuration. Error: {str(e)}")
        finally:
            session.close()

        # Close the dialog after saving
        self.accept()

    def save_monster_levels(self, monster, session):
        """Save the levels related to the monster, updating existing ones, adding new ones, and deleting removed ones."""

        # Get current levels from the database for this monster, mapped by their unique IDs
        existing_levels = {level.id: level for level in monster.levels}

        # Track the level IDs from the UI to detect deleted rows
        ui_level_ids = []

        for level_row in self.level_rows:
            level_id = getattr(level_row[1], 'level_id', None)  # Use a custom attribute for level ID in the UI
            level_number = level_row[1].text().strip()
            name = level_row[2].text().strip()
            power = level_row[3].text().strip()

            if level_id:  # If the level already exists (it has an ID)
                ui_level_ids.append(level_id)

                if level_id in existing_levels:
                    # Update the existing level
                    monster_level = existing_levels[level_id]
                    monster_level.level_number = level_number
                    monster_level.name = name
                    monster_level.power = power
            else:
                # Add new level if it doesn't exist (no ID yet)
                new_level = MonsterLevel(level=level_number, name=name, power=power)
                monster.levels.append(new_level)
                session.add(new_level)

        # Find levels to delete (existing ones not in the current UI)
        levels_to_delete = [level for level_id, level in existing_levels.items() if level_id not in ui_level_ids]

        for level in levels_to_delete:
            monster.levels.remove(level)
            session.delete(level)  # Delete the level from the database

    def validate_inputs(self):
        """Validate the inputs before saving."""

        # Always validate the preview name and category/logic combo boxes
        if not self.preview_name_line_edit.text().strip():
            return False

        if self.category_combo_box.currentIndex() == -1:
            return False

        if self.logic_combo_box.currentIndex() == -1:
            return False

        # Check the state of the map scan checkbox
        if self.map_scan_checkbox.isChecked():  # If map scan is enabled
            # Validate the fields related to map scan
            if not self.p540_image_line_edit.text().strip():
                return False

            if not self.preview_image_line_edit.text().strip():
                return False


        return True

    def cancel_dialog(self):
        """Close the dialog without saving."""
        self.reject()
