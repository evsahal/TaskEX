import os
import shutil
from hashlib import md5

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QFrame, QFileDialog, QMessageBox

from db.db_setup import get_session
from db.models import BlackMarket, BlackMarketItem
from gui.generated.black_market_profile import Ui_BlackMarket_Profile

ASSETS_PATH = os.path.join("assets", "540p", "blackmarket")


class BlackMarketProfileWidget(QWidget):
    def __init__(self, parent=None, flow_layout=None, data=None):
        super(BlackMarketProfileWidget, self).__init__(parent)
        self.ui = Ui_BlackMarket_Profile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout
        self.data = data

        # Store templates and removed templates
        self.templates = []
        self.removed_templates = []

        # Style the purchase buttons
        self.ui.purchase_button_frame.setStyleSheet("""
        QPushButton { background-color: #777; }
        QPushButton:checked { background-color: #FF79C6; color: black; font-weight: 560; }
        """)

        # Connect buttons
        self.ui.add_template_btn.clicked.connect(self.insert_new_template)
        self.ui.save_btn.clicked.connect(self.save_profile)
        self.ui.delete_btn.clicked.connect(self.delete_profile)

        # Disable delete button for new profiles until saved
        self.ui.delete_btn.setEnabled(data is not None)

        if data:
            self.load_profile_data()

    def insert_new_template(self):
        """Open file picker and insert a new template button."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Template Image", "", "Images (*.png *.jpg *.jpeg)")
        if not file_path:
            return

        if not self.validate_image_size(file_path):
            QMessageBox.warning(self, "Invalid Image", "Template image must be around 80x80.")
            return

        template_button = self.create_template_button(file_path)
        layout = self.ui.scroll_area_frame.layout()
        layout.insertWidget(self.get_add_template_button_index(layout), template_button)

        self.templates.append({"file_path": file_path, "button": template_button})

    def validate_image_size(self, file_path):
        """Check if the image size is valid."""
        pixmap = QPixmap(file_path)
        return pixmap.width() <= 100 and pixmap.height() <= 100

    def create_template_button(self, file_path):
        """Create a button with the selected template image."""
        button_frame = QFrame()
        button_frame.setFixedSize(60, 60)

        button = QPushButton(button_frame)
        button.setFixedSize(60, 60)
        button.setIcon(QIcon(QPixmap(file_path).scaled(60, 60, Qt.KeepAspectRatioByExpanding)))
        button.setIconSize(button.size())
        button.setProperty("file_path", file_path)

        overlay = QFrame(button_frame)
        overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        overlay.setFixedSize(button.size())
        overlay.hide()

        delete_btn = QPushButton("X", overlay)
        delete_btn.setFixedSize(20, 20)
        delete_btn.setStyleSheet("""
            QPushButton { color: white; background: red; border-radius: 10px; font-weight: bold; }
        """)
        delete_btn.move(35, 5)
        delete_btn.clicked.connect(lambda: self.remove_template(file_path, button_frame))

        button_frame.enterEvent = lambda event: overlay.show()
        button_frame.leaveEvent = lambda event: overlay.hide()

        return button_frame

    def remove_template(self, file_path, template_button):
        """Remove the template with confirmation."""
        reply = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this template?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            layout = self.ui.scroll_area_frame.layout()
            layout.removeWidget(template_button)
            template_button.deleteLater()

            self.templates = [t for t in self.templates if t["file_path"] != file_path]
            self.removed_templates.append(file_path)

    def get_add_template_button_index(self, layout):
        """Find the index of the add_template_btn."""
        for i in range(layout.count()):
            if layout.itemAt(i).widget() == self.ui.add_template_btn:
                return i
        return -1

    def save_profile(self):
        """Save or update the black market profile."""

        # TODO Validate before saving

        session = get_session()

        # Fetch existing profile or create new one
        if self.data:
            blackmarket = session.merge(self.data)  # Reattach to session
        else:
            blackmarket = BlackMarket()

        blackmarket.item_name = self.ui.name_lineEdit.text()
        blackmarket.purchase_rss = self.ui.rss_btn.isChecked()
        blackmarket.purchase_gems = self.ui.gems_btn.isChecked()
        blackmarket.purchase_gold = self.ui.gold_btn.isChecked()

        session.add(blackmarket)
        session.commit()

        # Handle new or modified templates
        for template in self.templates:
            file_path = template["file_path"]
            filename = os.path.basename(file_path)
            dest_path = os.path.join(ASSETS_PATH, filename)

            if not self.is_same_file(file_path, dest_path):
                shutil.copy(file_path, dest_path)

            if not any(item.item_image == filename for item in blackmarket.items):
                new_item = BlackMarketItem(blackmarket_id=blackmarket.id, item_image=filename)
                session.add(new_item)

        # Handle removed templates
        for removed_file in self.removed_templates:
            filename = os.path.basename(removed_file)
            item = session.query(BlackMarketItem).filter_by(
                blackmarket_id=blackmarket.id, item_image=filename).one_or_none()
            if item:
                session.delete(item)

            file_path = os.path.join(ASSETS_PATH, filename)
            if os.path.exists(file_path):
                os.remove(file_path)

        # Add a new empty profile only if it’s a new profile
        if not self.data:
            self.add_new_empty_profile()

        # Now update self.data with the saved profile instance
        if not self.data:
            self.data = blackmarket  # Assign the saved instance to self.data

        session.commit()
        session.close()


        QMessageBox.information(self, "Saved", "Black market profile saved successfully!")

        # Enable delete button for saved profiles
        self.ui.delete_btn.setEnabled(True)



    def add_new_empty_profile(self):
        """Add a new empty profile to the flow layout."""
        new_profile = BlackMarketProfileWidget(parent=self.parent(), flow_layout=self.flow_layout)
        self.flow_layout.addWidget(new_profile)

    def delete_profile(self):
        """Delete the black market profile with confirmation."""
        reply = QMessageBox.question(
            self, "Confirm Delete", "Are you sure you want to delete this profile?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            with get_session() as session:
                # Merge the data to ensure it's attached to the current session
                blackmarket = session.merge(self.data)

                # Delete related templates from disk
                for item in blackmarket.items:
                    file_path = os.path.join(ASSETS_PATH, item.item_image)
                    if os.path.exists(file_path):
                        os.remove(file_path)

                # Delete the blackmarket profile (items will be deleted due to cascade)
                session.delete(blackmarket)
                session.commit()

            QMessageBox.information(self, "Deleted", "Black market profile deleted successfully!")

            # Remove the widget from the UI
            self.flow_layout.removeWidget(self)
            self.deleteLater()

    def is_same_file(self, src, dest):
        """Check if the source and destination files are identical."""
        if not os.path.exists(dest):
            return False
        return md5(open(src, 'rb').read()).digest() == md5(open(dest, 'rb').read()).digest()

    def load_profile_data(self):
        """Load existing profile data into the UI."""
        self.ui.name_lineEdit.setText(self.data.item_name)
        self.ui.rss_btn.setChecked(self.data.purchase_rss)
        self.ui.gems_btn.setChecked(self.data.purchase_gems)
        self.ui.gold_btn.setChecked(self.data.purchase_gold)

        for item in self.data.items:
            file_path = os.path.join(ASSETS_PATH, item.item_image)
            template_button = self.create_template_button(file_path)
            layout = self.ui.scroll_area_frame.layout()
            layout.insertWidget(self.get_add_template_button_index(layout), template_button)

            self.templates.append({"file_path": file_path, "button": template_button})
