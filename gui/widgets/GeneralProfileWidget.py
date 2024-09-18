import os

from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from config.settings import BASE_DIR
from db.db_setup import get_session
from db.models import General
from gui.generated.general_profile import Ui_General_Profile
from utils.dialog_utils import show_confirmation_dialog


class GeneralProfileWidget(QWidget):
    scan_console = Signal(str)
    def __init__(self, parent=None,flow_layout=None,data=None):
        super(GeneralProfileWidget, self).__init__(parent)
        self.ui = Ui_General_Profile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout
        self.data = data
        # Set widget object name
        self.setObjectName(f"general_profile_{self.data.id}")
        self.image_path = os.path.join(BASE_DIR, 'assets', self.data.image_resolution.value, 'generals')

        # Setup General Preview Details View
        self.switch_view()

        # Setup General LineEdit
        self.ui.edit_general.setText(self.data.name)
        self.ui.edit_general.setStyleSheet("""QLineEdit, QLineEdit:hover, QLineEdit:focus {border: none;}""")
        self.ui.edit_general.setObjectName(f"edit_general_{self.data.id}")
        self.ui.edit_general.setProperty('general_id', self.data.id)
        self.ui.edit_general.setProperty('previous_text', self.data.name)

        # Setup General Delete
        self.ui.delete_general_btn.setObjectName(f"delete_general_{self.data.id}")
        self.ui.delete_general_btn.clicked.connect(self.delete_general_profile)

    def delete_general_profile(self):
        """
        Remove the current general profile widget from the layout and the UI, and delete the record from the database.
        """

        # Confirm with the user
        if show_confirmation_dialog(self, "confirm", f"Are you sure you want to remove {self.ui.edit_general.text()}?"):
            session = get_session()

            try:
                # Query the database to find the general by its ID
                general = session.query(General).filter(General.id == self.ui.edit_general.property('general_id')).first()
                # print(self.ui.edit_general.property('general_id'))
                if general:
                    # Delete the general's record from the database
                    session.delete(general)
                    session.commit()  # Commit the transaction to apply changes
                    self.scan_console.emit(
                        f"General '{self.ui.edit_general.text()}' has been removed.")

                    # Check if the image file exists and delete it
                    general_details_img = os.path.join(str(self.image_path), self.data.details_image_name)
                    general_list_img = os.path.join(str(self.image_path),
                                                    self.data.list_image_name) if self.data.list_image_name else None

                    # Delete the details view image if it exists
                    if os.path.exists(general_details_img):
                        os.remove(general_details_img)

                    # Delete the list view image if the file path is valid and the image exists
                    if general_list_img and os.path.exists(general_list_img):
                        os.remove(general_list_img)
                else:
                    self.scan_console.emit(
                        f"Error: General '{self.ui.edit_general.text()}' not found in the database.")

            except Exception as e:
                session.rollback()  # Rollback in case of error
                self.scan_console.emit(f"Error deleting general: {e}")

            finally:
                session.close()

            # Remove the widget from the UI
            if self.flow_layout:
                self.flow_layout.removeWidget(self)
                self.deleteLater()

    def switch_view(self,checked=False):
        if not checked:
            pixmap = QPixmap(os.path.join(str(self.image_path),self.data.details_image_name))
            half_height = int(pixmap.height() / 2)
            pixmap = pixmap.scaledToHeight(half_height)
            self.ui.general_icon_label.setPixmap(pixmap)
        else:
            if self.data.list_image_name:
                pixmap = QPixmap(os.path.join(str(self.image_path),self.data.list_image_name))
                half_height = int(pixmap.height() / 1.5)
                pixmap = pixmap.scaledToHeight(half_height)
                self.ui.general_icon_label.setPixmap(pixmap)
            else:
                self.ui.general_icon_label.clear()

