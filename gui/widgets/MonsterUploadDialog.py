from PySide6.QtWidgets import QMessageBox, QDialog

from core.custom_widgets.FlowLayout import FlowLayout
from db.db_setup import get_session
from gui.generated.monster_upload_dialog import Ui_Monster_Upload_Dialog
from gui.widgets.MonsterEditDialog import MonsterEditDialog
from gui.widgets.MonsterProfileWidget import MonsterProfileWidget


class MonsterUploadDialog(QDialog, Ui_Monster_Upload_Dialog):
    def __init__(self, parent=None):
        super(MonsterUploadDialog, self).__init__(parent)
        self.setupUi(self)

        # List to store newly added monsters
        self.boss_monster_list = []

        # Connect the 'Add Monster' button to open MonsterEditDialog
        self.add_monster_btn.clicked.connect(self.open_monster_edit_dialog)

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
            monster_edit_dialog = MonsterEditDialog( parent=self)

        result = monster_edit_dialog.exec_()

        # If the user clicked "Save" in the dialog
        if result == QDialog.Accepted:
            # Get the monster object returned from the dialog
            new_monster = monster_edit_dialog.get_monster()

            # If the monster is being edited, update the list and UI
            if monster_to_edit:
                self.update_existing_monster(monster_to_edit, new_monster)
            else:
                self.add_new_monster_to_list(new_monster)

    def add_new_monster_to_list(self, new_monster):
        """
        Add a new monster to the list and display it in the UI.
        """
        # Create a MonsterProfileWidget to represent the monster visually
        widget = MonsterProfileWidget(flow_layout=self.flow_layout, data=new_monster)

        # Connect the 'edit' button from the MonsterProfileWidget to allow editing
        widget.ui.configure_monster_btn.clicked.connect(lambda: self.open_monster_edit_dialog(new_monster))

        # Add the widget to the flow layout for visual representation
        widget.setFixedSize(widget.sizeHint())
        self.flow_layout.addWidget(widget)

        # Add the new monster to the list of unsaved monsters
        self.boss_monster_list.append(new_monster)

    def update_existing_monster(self, old_monster, updated_monster):
        """
        Update the existing monster in the list and refresh its display in the UI.
        """
        # Update the existing monster in the list
        for i, monster in enumerate(self.boss_monster_list):
            if monster == old_monster:
                self.boss_monster_list[i] = updated_monster
                break

        # Refresh the corresponding MonsterProfileWidget in the UI
        for i in range(self.flow_layout.count()):
            widget = self.flow_layout.itemAt(i).widget()
            if widget.data == old_monster:
                # Update the widget's data and refresh the displayed info
                widget.data = updated_monster
                widget.ui.monster_name_label.setText(updated_monster.preview_name)
                break

    def save_new_monsters(self):
        """
        Save all newly added monsters to the database.
        """
        if not self.boss_monster_list:
            QMessageBox.information(self, "No New Monsters", "There are no new monsters to save.")
            return

        session = get_session()
        try:
            for monster in self.boss_monster_list:
                session.add(monster)
            session.commit()
            QMessageBox.information(self, "Save Successful", "All new monsters have been saved to the database.")
            self.boss_monster_list.clear()  # Clear the list after saving
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Save Error", f"Failed to save monsters. Error: {str(e)}")
        finally:
            session.close()

    def remove_monster(self, monster):
        """
        Remove the monster from the list and UI.
        :param monster: Monster object to be removed
        """
        # Remove from the list of unsaved monsters
        self.boss_monster_list = [m for m in self.boss_monster_list if m != monster]

        # Find and remove the corresponding widget from the UI
        for i in range(self.flow_layout.count()):
            widget = self.flow_layout.itemAt(i).widget()
            if widget.data == monster:
                widget.deleteLater()
                break
