import os
import random
import tempfile
from datetime import datetime
from tempfile import template

import cv2
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QImage
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, \
    QMessageBox, QWidget, QFrame
from sqlalchemy.orm import joinedload

from config.settings import BASE_DIR
from core.controllers.emulator_controller import check_port_already_in_use, monster_template_scan, \
    generate_template_image
from core.custom_widgets.SelectionTool import SelectionTool
from core.instance_manager import is_emulator_port_available
from db.db_setup import get_session
from db.models import BossMonster, MonsterCategory, MonsterLogic, MonsterLevel, MonsterImage
from gui.generated.monster_edit_dialog import Ui_Monster_Edit_Dialog
from utils.helper_utils import image_chooser, copy_image_to_preview, copy_image_to_template
from utils.image_picker import ImagePicker


class MonsterEditDialog(QDialog, Ui_Monster_Edit_Dialog):
    # Signal emitted when a monster is updated
    monster_updated = Signal(int)
    # Signal emitted to setup the template selection
    frame_ready = Signal(QImage)
    # Signal to receive template and threshold
    template_ready = Signal(object, float)
    reset_template_btn = Signal()

    def __init__(self, monster_id=None,monster_to_edit=None, parent=None):
        super(MonsterEditDialog, self).__init__(parent)
        self.setupUi(self)

        self.monster_id = monster_id  # None for new monsters, ID for editing
        self.monster = None
        self.monster_to_edit = monster_to_edit
        self.previous_logic = None
        self.level_rows = []  # Keep track of dynamically added levels
        self.main_window = parent

        # Set up scroll area for monster levels
        self.init_level_scroll_area()


        # Connect signals
        self.save_changes_btn.clicked.connect(self.save_changes_pressed)
        self.cancel_btn.clicked.connect(self.cancel_dialog)
        self.add_level_btn.clicked.connect(self.handle_add_new_level)
        # self.browse_preview_btn.clicked.connect(lambda: image_chooser(self.browse_preview_btn, self.preview_image_line_edit))
        # self.browse_540p_btn.clicked.connect(lambda: image_chooser(self.browse_540p_btn, self.p540_image_line_edit))
        self.logic_combo_box.currentTextChanged.connect(self.handle_logic_change)
        self.map_scan_checkbox.stateChanged.connect(self.toggle_map_scan_fields)
        self.capture_image_btn.clicked.connect(self.capture_template_ss)
        self.lock_btn.clicked.connect(self.toggle_lock_button)
        self.find_template_btn.clicked.connect(self.generate_template_image)
        self.frame_ready.connect(self.handle_frame_ready)
        self.template_ready.connect(self.handle_template_ready)
        self.reset_template_btn.connect(self.reset_template_btn_state)

        # Setup image picker
        self.preview_image_picker = ImagePicker(self.browse_preview_btn, self.preview_image_line_edit)
        self.template_image_picker = ImagePicker(self.browse_540p_btn, self.p540_image_line_edit)

        # Setup Emulator Connection
        self.lock_btn.setIcon(QIcon(":/icons/images/icons/cil-lock-unlocked.png"))

        # Populate fields with initial data
        self.populate_field_data()

        # Keep track of the selection tool for state management
        self.selection_tool = None

    def handle_template_ready(self, template, threshold):
        """Handle the received template and threshold."""
        # print(f"[INFO] Template received with threshold: {threshold}")

        # Update the QDoubleSpinBox with the received threshold
        self.threshold_spin_box.setValue(threshold)

        # Generate a unique filename using the current timestamp and a random number
        filename = f"template_{datetime.now().strftime("%Y%m%d%H%M%S")}.png"

        # Get the real system temp directory and define the template path
        temp_dir = tempfile.gettempdir()
        template_path = os.path.join(temp_dir, filename)

        # Save the template image to the temp directory
        cv2.imwrite(template_path, template)

        # Update the image picker
        self.template_image_picker.load_file(template_path)

        # if the template line edit is empty, then set a new name there
        if not self.p540_image_line_edit.text().strip():
            # Get the text from preview_name_line_edit
            preview_name = self.preview_name_line_edit.text().strip()

            # If preview_name is not empty, set it as the text for p540_image_line_edit
            if preview_name:
                # Replace spaces with underscores and add '_540p.png' at the end
                p540_image_name = f"{preview_name.replace(' ', '_').lower()}_540p.png"
                # Set the new name in p540_image_line_edit
                self.p540_image_line_edit.setText(p540_image_name)

    def reset_template_btn_state(self):
        self.find_template_btn.setIcon(QIcon.fromTheme("system-search"))
        self.find_template_btn.blockSignals(False)

    def handle_frame_ready(self, img):
        """
        Slot to receive the emitted image, remove the scroll area, and display
        the selection tool inside the template_selection_frame.
        """
        try:
            # Get the template_selection_frame
            template_frame = self.template_selection_frame
            if not template_frame:
                raise ValueError("[ERROR] Template selection frame not found.")

            # Get or create the layout for the template frame
            template_layout = template_frame.layout()
            if not template_layout:
                template_layout = QVBoxLayout(template_frame)
                template_frame.setLayout(template_layout)

            # Remove all widgets from the template frame (including the scroll area if present)
            while template_layout.count() > 0:
                item = template_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    print(f"[DEBUG] Removing widget: {widget.objectName()} ({widget.__class__.__name__})")
                    widget.deleteLater()

            # Create the selection tool with the captured image
            self.selection_tool = SelectionTool(img, full_preview=False, parent=template_frame)
            self.selection_tool.setObjectName("selection_tool")

            # Add the selection tool directly to the template frame layout
            template_layout.addWidget(self.selection_tool)

            print("[DEBUG] Selection tool added to the template selection frame.")

        except Exception as e:
            print(f"[ERROR] Error in handle_frame_ready: {e}")

    def capture_template_ss(self):
        """Capture the template image through emulator."""
        port = self.port_lineEdit.text().strip()

        is_valid, error_message = self.validate_port(port)

        if not is_valid:
            QMessageBox.critical(self, "Error", error_message)
            return

        # Start the thread to capture the image
        monster_template_scan(self, port, "capture_template_ss")

    def validate_port(self,port):

        if not port.isdigit():
            # print("Wrong Port, stop exection")
            return False, "Invalid Port Number."

        if not is_emulator_port_available(int(port)):
            return False, "Enter a valid Port Number."

        #Check if the port is in use by emulator controls
        if check_port_already_in_use(self.main_window,port):
            # print("Already in use, stop execution")
            return False, "Port is already in use"

        return True, None

    def toggle_lock_button(self, checked):
        """Handle the lock button state."""
        if checked:
            # Ensure a template is selected before locking
            if not self.selection_tool or not self.selection_tool.is_selection_made():
                QMessageBox.warning(self, "Warning", "Please select a template area before locking.")
                self.lock_btn.setChecked(False)  # Revert the button state
                return

            # Lock the selection tool to make it read-only
            self.selection_tool.set_read_only(True)
            self.lock_btn.setIcon(QIcon(":/icons/images/icons/cil-lock-locked.png"))
            self.port_lineEdit.setReadOnly(True)  # Disable port input
            self.capture_image_btn.setEnabled(False)  # Disable capture button
        else:
            # Unlock the selection tool
            if self.selection_tool:
                self.selection_tool.set_read_only(False)
            self.lock_btn.setIcon(QIcon(":/icons/images/icons/cil-lock-unlocked.png"))
            self.port_lineEdit.setReadOnly(False)  # Enable port input
            self.capture_image_btn.setEnabled(True)  # Enable capture button

    def generate_template_image(self):
        if not self.lock_btn.isChecked():
            QMessageBox.warning(self, "Error", "Please lock the selection area before generating the template.")
            return

        generate_template_image(self, self.port_lineEdit.text(), "generate_template_image")

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
            monster_data = self.get_monster_data(session)
            self.load_monster_data(monster_data)
        elif self.monster_to_edit:
            self.load_monster_data(self.monster_to_edit)

        session.close()

    def load_monster_data(self, monster_data):
        """Load the existing data for the selected boss monster."""

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
            # Load the image picker with existing file path value
            preview_img =os.path.join(BASE_DIR, 'assets', 'preview' , monster_data.monster_image.preview_image)
            if self.monster_id and os.path.isfile(preview_img):
                self.preview_image_picker.load_file(str(preview_img))
            elif getattr(self.monster, 'preview_img_path', None) and os.path.isfile(self.monster.preview_img_path):
                self.preview_image_picker.load_file(self.monster.preview_img_path)
            if self.map_scan_checkbox.isChecked():
                # Load the image picker with existing file path value
                template_img = os.path.join(BASE_DIR, 'assets', '540p', 'monsters', monster_data.monster_image.img_540p)
                if self.monster_id and os.path.isfile(template_img):
                    self.template_image_picker.load_file(str(template_img))
                elif getattr(self.monster, 'p540_img_path', None) and os.path.isfile(self.monster.p540_img_path):
                    self.template_image_picker.load_file(self.monster.p540_img_path)
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
        self.port_lineEdit.setEnabled(toggle)
        self.capture_image_btn.setEnabled(toggle)
        self.lock_btn.setEnabled(toggle)


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
        if not self.monster_id and not self.monster_to_edit:
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
            # QMessageBox.warning(self, "Validation Error", "Please fill in all required fields.")
            return

        session = get_session()
        # print(self.monster_to_edit)
        if not self.monster_id and not self.monster_to_edit:
            # print("New Monster")
            # Create new monster
            self.monster = BossMonster()
            self.monster.monster_image = MonsterImage()
        elif self.monster_to_edit:
            # print("Edit New Monster")
            self.monster = self.monster_to_edit
        else:
            # print("Edit Monster")
            # Edit existing monster
            self.monster = session.query(BossMonster).filter(BossMonster.id == self.monster_id).one()

        # Store basic info
        self.monster.preview_name = self.preview_name_line_edit.text()
        self.monster.monster_category_id = self.category_combo_box.currentData()
        self.monster.monster_logic_id = self.logic_combo_box.currentData()
        self.monster.enable_map_scan = self.map_scan_checkbox.isChecked()

        # Store image data
        self.monster.monster_image.preview_image = self.preview_image_line_edit.text()
        if self.monster.enable_map_scan:
            self.monster.monster_image.img_540p = self.p540_image_line_edit.text()
            self.monster.monster_image.img_threshold = self.threshold_spin_box.value()
            self.monster.monster_image.click_pos = f"{self.click_x_spin_box.value()},{self.click_y_spin_box.value()}"
        else:
            self.monster.monster_image.img_540p = None
            self.monster.monster_image.img_threshold = None
            self.monster.monster_image.click_pos = None

        # Store monster levels
        self.update_monster_levels()

        # Return the new monster object without saving
        if not self.monster_id:
            # Close  the dialog
            self.accept()
            self.monster.preview_img_path = self.preview_image_line_edit.property("file_path")
            self.monster.p540_img_path = self.p540_image_line_edit.property("file_path")
            return self.monster
        # Commit changes for existing monsters
        try:
            session.add(self.monster)
            # Move the file to the preview folder if file picker is used:
            file_path = self.preview_image_line_edit.property("file_path")
            if file_path:
                copy_image_to_preview(file_path,self.monster.monster_image.preview_image)
            # Move the file to the 540p template if file picker is used:
            file_path = self.p540_image_line_edit.property("file_path")
            if file_path:
                copy_image_to_template(file_path, self.monster.monster_image.img_540p)

            # Commit changes in db
            session.commit()
            self.monster_updated.emit(self.monster_id)
            QMessageBox.information(self, "Success", "Monster updated successfully!")
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Error", f"Failed to save the monster: {e}")
        finally:
            session.close()
            self.accept()

    def update_monster_levels(self):
        """
        Handle updating the monster.levels object based on the UI input.
        For existing monsters, update the DB records. For new monsters, reset the levels list.
        """

        # Scenario 1: For existing monsters (already in the DB, with a valid monster_id)
        if self.monster_id:
            # Get the current levels from the database and map them by their unique ID
            existing_levels = {level.id: level for level in self.monster.levels} if self.monster.levels else {}

            ui_level_ids = []  # To track levels that are still present in the UI

            for level_row in self.level_rows:
                # Retrieve data from the UI inputs (level number, name, power)
                level_number = level_row[1].text().strip()
                name = level_row[2].text().strip()
                power = level_row[3].text().strip()

                # If the row represents an existing level (has level_id), update it
                if hasattr(level_row[1], 'level_id'):
                    level_id = level_row[1].level_id
                    if level_id in existing_levels:
                        # Update the existing level
                        monster_level = existing_levels[level_id]
                        monster_level.level = level_number
                        monster_level.name = name
                        monster_level.power = power
                        ui_level_ids.append(level_id)  # Track the updated level

                else:
                    # Add a new level for newly created rows (those without level_id)
                    new_level = MonsterLevel(level=level_number, name=name, power=power)
                    self.monster.levels.append(new_level)  # Append the new level to the monster object

            # Identify levels that were removed in the UI and delete them
            levels_to_delete = [level for level_id, level in existing_levels.items() if level_id not in ui_level_ids]
            for level in levels_to_delete:
                self.monster.levels.remove(level)

        # Scenario 2: For new monsters (monster_id is None)
        else:
            # Reset the levels list for new monsters
            self.monster.levels = []

            # Re-populate the levels list from the UI
            for level_row in self.level_rows:
                # Extract data from the UI inputs (level number, name, power)
                level_number = level_row[1].text().strip()
                name = level_row[2].text().strip()
                power = level_row[3].text().strip()

                # Add each level to the monster's levels list
                new_level = MonsterLevel(level=level_number, name=name, power=power)
                self.monster.levels.append(new_level)

    def validate_inputs(self):
        """Validate the form inputs before saving."""

        # 1. Validate the preview name
        if not self.preview_name_line_edit.text().strip():
            QMessageBox.warning(self, "Validation Error", "Preview name cannot be empty.")
            return False

        # 2. Validate the preview image field
        if not self.preview_image_line_edit.text().strip():
            QMessageBox.warning(self, "Validation Error", "Preview image cannot be empty.")
            return False

        # 3. Validate category and logic combo boxes
        if self.category_combo_box.currentIndex() == -1:
            QMessageBox.warning(self, "Validation Error", "Please select a category.")
            return False

        if self.logic_combo_box.currentIndex() == -1:
            QMessageBox.warning(self, "Validation Error", "Please select a logic.")
            return False

        # 4. Validate map scan-related fields if map_scan_checkbox is checked
        if self.map_scan_checkbox.isChecked():
            if not self.p540_image_line_edit.text().strip():
                QMessageBox.warning(self, "Validation Error", "Template image 540p cannot be empty.")
                return False

        # 5. Validate there is at least one level
        if len(self.level_rows) == 0:
            QMessageBox.warning(self, "Validation Error", "There must be at least one level.")
            return False

        # 6. Validate all levels have values for level number, name, and power
        level_numbers = set()  # To keep track of unique level numbers
        for level_row in self.level_rows:
            level_number = level_row[1].text().strip()
            name = level_row[2].text().strip()
            power = level_row[3].text().strip()

            if not level_number:
                QMessageBox.warning(self, "Validation Error", "Level number cannot be empty.")
                return False
            if not name:
                QMessageBox.warning(self, "Validation Error", "Level name cannot be empty.")
                return False
            if not power:
                QMessageBox.warning(self, "Validation Error", "Level power cannot be empty.")
                return False

            # Check if the level number is unique
            if level_number in level_numbers:
                QMessageBox.warning(self, "Validation Error", f"Level number {level_number} is duplicated.")
                return False
            level_numbers.add(level_number)  # Add level number to the set for uniqueness check

        # If all validations pass
        return True

    def get_monster(self):
        """Return the monster object created in the dialog."""
        return self.monster

    def get_preview_image_path(self):
        return  self.preview_image_line_edit.property("file_path")

    def cancel_dialog(self):
        """Close the dialog without saving."""
        self.reject()

