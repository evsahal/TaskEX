import os
import shutil
import tempfile
import zipfile

import yaml
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QDialog, QFileDialog

from config.settings import BASE_DIR
from core.custom_widgets.FlowLayout import FlowLayout
from core.services.bm_monsters_service import create_monster_from_zip_data
from db.db_setup import get_session
from gui.generated.monster_upload_dialog import Ui_Monster_Upload_Dialog
from gui.widgets.MonsterEditDialog import MonsterEditDialog
from gui.widgets.MonsterProfileWidget import MonsterProfileWidget
from utils.constants_util import logic_colors
from utils.helper_utils import copy_image_to_preview, copy_image_to_template


class MonsterUploadDialog(QDialog, Ui_Monster_Upload_Dialog):
    def __init__(self,main_window, parent=None):
        super(MonsterUploadDialog, self).__init__(parent)
        self.setupUi(self)

        # Store the reference to MainWindow
        self.main_window = main_window

        # List to store newly added monsters
        self.boss_monster_list = []

        # Connect the buttons
        self.add_monster_btn.clicked.connect(self.open_monster_edit_dialog)
        self.import_monster_btn.clicked.connect(self.import_monsters_from_zip)
        self.upload_monsters_btn.clicked.connect(self.save_new_monsters)
        self.exit_btn.clicked.connect(self.close)

        # Initialize the layout for displaying the monster profiles
        self.flow_layout = FlowLayout(self.monsters_list_frame)
        self.monsters_list_frame.setLayout(self.flow_layout)

    def open_monster_edit_dialog(self, monster_to_edit=None):
        """
        Open MonsterEditDialog for adding or editing a monster.
        :param monster_to_edit: Optional. Pass an existing monster object if editing.
        """
        # Open the MonsterEditDialog for editing the passed monster or adding a new one
        if monster_to_edit is None:
            monster_edit_dialog = MonsterEditDialog(parent=self)
        else:
            monster_edit_dialog = MonsterEditDialog(parent=self,monster_to_edit=monster_to_edit)


        result = monster_edit_dialog.exec_()

        # If the user clicked "Save" in the dialog
        if result == QDialog.Accepted:
            # Get the monster object returned from the dialog
            new_monster = monster_edit_dialog.get_monster()
            # print(new_monster.file_path)

            # If the monster is being edited, update the list and UI
            if monster_to_edit:
                self.update_existing_monster(monster_to_edit, new_monster,monster_edit_dialog.get_preview_image_path())
            else:
                self.add_new_monster_to_list(new_monster,monster_edit_dialog.get_preview_image_path())

    def add_new_monster_to_list(self, new_monster,file_path):
        """
        Add a new monster to the list and display it in the UI.
        """
        # Create a MonsterProfileWidget to represent the monster visually
        widget = MonsterProfileWidget(flow_layout=self.flow_layout, data=new_monster,file_path=file_path)

        # Connect the 'edit' button from the MonsterProfileWidget to allow editing
        widget.ui.configure_monster_btn.clicked.connect(lambda: self.open_monster_edit_dialog(new_monster))

        # Add the widget to the flow layout for visual representation
        widget.setFixedSize(widget.sizeHint())
        self.flow_layout.addWidget(widget)

        # Add the new monster to the list of unsaved monsters
        self.boss_monster_list.append(new_monster)

    def update_existing_monster(self, old_monster, updated_monster,file_path):
        """
        Update the existing monster in the list and refresh its display in the UI.
        """
        # Update the existing monster in the list
        pos = -1
        for i, monster in enumerate(self.boss_monster_list):
            if monster == old_monster:
                self.boss_monster_list[i] = updated_monster
                pos = i
                break

        # Refresh the corresponding MonsterProfileWidget in the UI
        widget = self.flow_layout.itemAt(pos).widget()
        if widget.data == old_monster:
            # Update the widget's data and refresh the displayed info
            widget.data = updated_monster
            preview_path = os.path.join(BASE_DIR, 'assets', 'preview')
            # Setup Monster Preview
            widget.ui.monster_name_label.setText(updated_monster.preview_name)

            # Check if the file exists
            if file_path and os.path.exists(file_path):
                monster_preview = file_path  # Use the provided image path
            else:
                # Use the default preview image
                monster_preview = os.path.join(str(preview_path), "default_preview.png")


            pixmap = QPixmap(monster_preview)
            pixmap = pixmap.scaledToHeight(92)
            widget.ui.monster_icon_label.setPixmap(pixmap)

            # Update the frame
            # Get the corresponding color for the logic ID
            logic_color = logic_colors.get(updated_monster.monster_logic_id, '#000000')  # Default to black if not found

            # Setup the Monster Bottom Frame Color
            widget.ui.bottom_color_frame.setStyleSheet(f"""
                                    background-color: rgb(29, 33, 38);
                                    border-bottom: 2px solid {logic_color};
                                """)

    def save_new_monsters(self):
        """
        Save all newly added monsters to the database.
        """
        if not self.boss_monster_list:
            QMessageBox.information(self, "No New Monsters", "There are no new monsters to save.")
            return

        # TODO Validate the bosses

        # Add to the database
        session = get_session()
        try:
            for monster in self.boss_monster_list:
                session.add(monster)
                # Commit to assign IDs to new monsters
            session.commit()

            # After commit, add each monster to the main frame
            for monster in self.boss_monster_list:
                # Move the file to the preview folder if file_path is set
                if monster.preview_img_path and os.path.exists(monster.preview_img_path):
                    copy_image_to_preview(monster.preview_img_path, monster.monster_image.preview_image)
                if monster.p540_img_path and os.path.exists(monster.p540_img_path):
                    copy_image_to_template(monster.p540_img_path, monster.monster_image.img_540p)

                # Now we can call add_monster_to_main_frame because monster IDs are assigned
                self.add_monster_to_main_frame(monster)

            QMessageBox.information(self, "Save Successful", "All new monsters have been saved to the database.")
            # Disable the upload button after saving
            self.upload_monsters_btn.setEnabled(False)
            self.boss_monster_list.clear()  # Clear the list after saving

        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Save Error", f"Failed to save monsters. Error: {str(e)}")
        finally:
            session.close()

    def add_monster_to_main_frame(self, boss):
        flow_layout = self.main_window.widgets.monsters_list_flow_layout

        widget = MonsterProfileWidget(flow_layout=flow_layout, data=boss)
        setattr(self.main_window.widgets, widget.objectName(), widget)

        # Lazy import to avoid circular import
        def configure_monster_clicked():
            from gui.controllers.bm_monsters_controller import configure_monster
            configure_monster(self.main_window, widget.ui.checkBox.property("boss_id"))

        # Setup Configure/Edit Monster
        widget.ui.configure_monster_btn.clicked.connect(configure_monster_clicked)

        # Set the size of the widget to its size hint
        widget.setFixedSize(widget.sizeHint())
        flow_layout.addWidget(widget)

    def import_monsters_from_zip(self):
        """Open a file picker to import a zip file and process its content."""
        zip_file_path, _ = QFileDialog.getOpenFileName(self, "Select Monster Export Zip", "", "Zip Files (*.zip)")
        if not zip_file_path:
            return  # User canceled the operation

        # Extract to the system's temporary folder
        temp_extract_folder = tempfile.mkdtemp(prefix="monster_import_")

        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_extract_folder)

            # Validate the YAML file
            yaml_file_path = os.path.join(temp_extract_folder, "boss_monsters.yaml")
            if not os.path.exists(yaml_file_path):
                raise FileNotFoundError("Invalid zip file. YAML file not found.")

            with open(yaml_file_path, 'r') as yaml_file:
                monsters_data = yaml.safe_load(yaml_file)

            # Convert YAML data to BossMonster objects and add to the upload scroll area
            for monster_data in monsters_data:
                new_monster = create_monster_from_zip_data(monster_data,temp_extract_folder)
                print("Yaml images")
                print(new_monster.preview_img_path)
                print(new_monster.p540_img_path)
                print("End of yaml")
                self.add_new_monster_to_list(new_monster,new_monster.preview_img_path)

            QMessageBox.information(self, "Import Successful", "Monsters imported successfully!")

        except Exception as e:
            # Clean up the temp folder on error
            shutil.rmtree(temp_extract_folder)
            QMessageBox.critical(self, "Import Error! ", str(e))

