import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from config.settings import BASE_DIR
from gui.generated.monster_profile import Ui_Monster_Profile
from utils.constants_util import logic_colors
from utils.dialog_utils import show_confirmation_dialog


class MonsterProfileWidget(QWidget):
    def __init__(self, parent=None,flow_layout=None,data=None):
        super(MonsterProfileWidget, self).__init__(parent)
        self.ui = Ui_Monster_Profile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout
        self.data = data

        # Set widget object name
        self.setObjectName(f"monster_profile_{self.data.id}")
        self.preview_path = os.path.join(BASE_DIR, 'assets', 'preview')

        # Setup Monster Preview
        monster_preview = os.path.join(str(self.preview_path), self.data.monster_image.preview_image)
        if not os.path.isfile(monster_preview):
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
            # TODO Connect to db and remove
            if self.flow_layout:
                self.flow_layout.removeWidget(self)
                self.deleteLater()