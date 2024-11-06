import os

from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from db.db_setup import get_session
from db.models import BossMonster, MonsterLevel, MonsterImage
from gui.generated.monster_profile import Ui_Monster_Profile
from utils.constants_util import logic_colors
from utils.dialog_utils import show_confirmation_dialog


class MonsterProfileWidget(QWidget):
    monster_deleted = Signal(object)
    def __init__(self, parent=None,flow_layout=None,data=None,file_path = None):
        super(MonsterProfileWidget, self).__init__(parent)
        self.ui = Ui_Monster_Profile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout
        self.data = data

        # Set widget object name
        self.setObjectName(f"monster_profile_{self.data.id}")
        self.preview_path = os.path.join( 'assets', 'preview')

        # Setup Monster Preview
        monster_preview = os.path.join(str(self.preview_path), self.data.monster_image.preview_image)
        # Determine which preview image to use
        if file_path and os.path.exists(file_path):
            # Use the provided custom file path if it exists
            monster_preview = file_path
        elif not os.path.isfile(monster_preview):
            # Use the default preview image
            monster_preview = os.path.join(str(self.preview_path), "default_preview.png")
        pixmap = QPixmap(monster_preview)
        # half_height = int(pixmap.height() / 2)
        # print(half_height) #92
        pixmap = pixmap.scaledToHeight(92)
        self.ui.monster_icon_label.setPixmap(pixmap)

        # Setup Monster Label
        self.ui.monster_name_label.setText(self.data.preview_name)
        # setattr(main_window.widgets, play_button.objectName(), play_button)


        # print(self.data.monster_logic_id)
        # Get the corresponding color for the logic ID
        logic_color = logic_colors.get(self.data.monster_logic_id, '#000000')  # Default to black if not found

        # Setup the Monster Bottom Frame Color
        self.ui.bottom_color_frame.setStyleSheet(f"""
            background-color: rgb(29, 33, 38);
            border-bottom: 2px solid {logic_color};
        """)

        # Setup Monster Delete
        if self.data.system:
            self.ui.delete_monster_btn.setEnabled(False)
        self.ui.delete_monster_btn.clicked.connect(self.delete_monster_profile)

        # Checkbox
        self.ui.checkBox.setVisible(False)
        self.ui.checkBox.setProperty("boss_id", self.data.id)
        # get_value = self.ui.checkbox.property("boss_id")

    def delete_monster_profile(self):
        """
        Remove the current monster profile widget from the layout and the UI.
        """
        if show_confirmation_dialog(self, "confirm", f"Are you sure you want to remove {self.ui.monster_name_label.text()}?"):
            session = get_session()
            # If it's present in the db
            if self.data.id:
                try:
                    # Remove the monster and its related data from the DB
                    monster_to_delete = session.query(BossMonster).filter(BossMonster.id == self.data.id).one_or_none()
                    if monster_to_delete:
                        # Delete the related levels
                        session.query(MonsterLevel).filter(MonsterLevel.boss_monster_id == monster_to_delete.id).delete()

                        # Delete the related images
                        session.query(MonsterImage).filter(MonsterImage.id == monster_to_delete.monster_image_id).delete()

                        # Finally, delete the boss monster itself
                        session.delete(monster_to_delete)

                        # Commit the transaction to remove the monster from the database
                        session.commit()
                except Exception as e:
                    session.rollback()
                    print(e)
                finally:
                    session.close()

            # Remove it from the UI
            if self.flow_layout:
                self.flow_layout.removeWidget(self)
                self.deleteLater()

            # Emit the signal, passing the monster object (self.data) if the id is None
            self.monster_deleted.emit(self.data)