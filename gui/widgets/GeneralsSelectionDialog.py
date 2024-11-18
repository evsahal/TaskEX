from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QDialog

from core.custom_widgets.QCheckComboBox import QCheckComboBox
from gui.generated.generals_selection import Ui_GeneralsSelectionDialog


class GeneralsSelectionDialog(QDialog, Ui_GeneralsSelectionDialog):
    def __init__(self, parent, index):
        super(GeneralsSelectionDialog, self).__init__(parent)
        # print(f"index recieved is {index}")
        try:
            self.setupUi(self)
            # Set window flags to disable the close button
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

            self.setWindowTitle("Generals Selection")
            # self.setFixedSize(600, 670)
            # SCAN Filter
            vert_layout = QVBoxLayout(self.general_filter_widget)
            label = QLabel("Filter")
            vert_layout.addWidget(label)
            self.combo_box = QCheckComboBox(placeholderText="None")
            self.combo_box.setObjectName("general_filter_dd")
            model = self.combo_box.model()
            self.combo_box.addItem("Favorite")
            model.item(0).setCheckable(True)
            self.combo_box.addItem("Idle")
            model.item(1).setCheckable(True)
            self.combo_box.setMinimumWidth(140)
            self.combo_box.currentIndexChanged.connect(self.test)
            vert_layout.addWidget(self.combo_box)
            self.general_filter_widget.setLayout(vert_layout)

        except Exception as e:
            print(e)