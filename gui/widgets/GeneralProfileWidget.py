from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from gui.generated.general_profile import Ui_General_Profile


class GeneralProfileWidget(QWidget):
    def __init__(self, parent=None):
        super(GeneralProfileWidget, self).__init__(parent)
        self.ui = Ui_General_Profile()
        self.ui.setupUi(self)

        # Setup General Preview
        pixmap = QPixmap(r"E:\Projects\PyCharmProjects\TaskEX\assets\540p\Generals\elektra.png")
        half_height = int(pixmap.height() / 2)
        pixmap = pixmap.scaledToHeight(half_height)
        self.ui.general_icon_label.setPixmap(pixmap)

        # Setup General LineEdit
        self.ui.edit_general.setText("Elektra")
        self.ui.edit_general.setStyleSheet("""QLineEdit, QLineEdit:hover, QLineEdit:focus {border: none;}""")




# class GeneralProfile(QWidget, Ui_Scan_Generals_Form):
#     def __init__(self, general_property, parent=None):
#         super(GeneralProfile, self).__init__(parent)
#         self.setupUi(self)
#         # print(general_property["img_540p"])
#         pixmap = QPixmap(general_property["img_540p"])
#         half_height = pixmap.height() / 2
#         pixmap = pixmap.scaledToHeight(half_height)
#         self.label_general_icon.setPixmap(pixmap)
#         edit_general_obj_name = f"edit_general_{general_property['name'].lower().replace(' ', '').replace('-', '')}"
#         self.edit_general.setObjectName(edit_general_obj_name)
#         self.edit_general.setText(general_property["name"])
#         self.edit_general.setProperty('general_ID', general_property['id'])
#         self.edit_general.setProperty('previousText', general_property['name'])
#         self.edit_general.setProperty('imageFile', general_property['img_540p'])
#         self.edit_general.setStyleSheet("""QLineEdit, QLineEdit:hover, QLineEdit:focus {border: none;}""")
#         self.edit_general.updateDeleteObj.connect(self.updateDeleteObject)
#         self.edit_general.updateScanConsole.connect(self.updateConsole)
#         self.delete_general.setObjectName(f"delete_general_{general_property['name'].lower().replace(' ', '_')}")