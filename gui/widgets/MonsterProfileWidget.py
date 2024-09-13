from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from gui.generated.monster_profile import Ui_Monster_Profile
from utils.dialog_utils import show_confirmation_dialog


class MonsterProfileWidget(QWidget):
    def __init__(self, parent=None,flow_layout=None):
        super(MonsterProfileWidget, self).__init__(parent)
        self.ui = Ui_Monster_Profile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout

        # Setup General Preview
        pixmap = QPixmap(r"E:\Projects\PyCharmProjects\TaskEX\assets\preview\pan_mounted_preview_50x50.png")
        # half_height = int(pixmap.height() / 2)
        # print(half_height) #92
        pixmap = pixmap.scaledToHeight(92)
        self.ui.monster_icon_label.setPixmap(pixmap)

        # Setup General LineEdit
        self.ui.monster_name_label.setText("Ymir")
        self.ui.monster_name_label.setObjectName(f"edit_monster_") # add index here
        # setattr(main_window.widgets, play_button.objectName(), play_button)

        # Setup General Delete
        self.ui.delete_monster_btn.setObjectName(f"delete_monster_") # add index here and connect to slot
        self.ui.delete_monster_btn.clicked.connect(self.delete_monster_profile)

        # Checkbox
        self.ui.checkBox.setVisible(False)

    def delete_monster_profile(self):
        """
        Remove the current monster profile widget from the layout and the UI.
        """
        if show_confirmation_dialog(self, "confirm", f"Are you sure you want to remove {self.ui.monster_name_label.text()}?"):

            if self.flow_layout:
                self.flow_layout.removeWidget(self)
                self.deleteLater()