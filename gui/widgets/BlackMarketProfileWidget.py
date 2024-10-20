from PySide6.QtWidgets import QWidget, QPushButton

from gui.generated.black_market_profile import Ui_BlackMarket_Profile


class BlackMarketProfileWidget(QWidget):
    def __init__(self, parent=None,flow_layout=None,data=None):
        super(BlackMarketProfileWidget, self).__init__(parent)
        self.ui = Ui_BlackMarket_Profile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout
        self.data = data

        # Set widget object name
        # self.setObjectName(f"blackmarket_profile_{self.data.id}")

        # Set Purchase button styles
        style_sheet = """
        QPushButton{ background-color:  #777; }
        QPushButton:checked { background-color:  #FF79C6; color:black; font-weight: bold; }
        """
        self.ui.purchase_button_frame.setStyleSheet(style_sheet)

        # Connect the add template button
        self.ui.add_template_btn.clicked.connect(self.insert_new_template)

    def insert_new_template(self):
        # Create a new button without text
        new_button = QPushButton("")
        new_button.setFixedSize(60, 60)

        # Find the layout of the scroll area frame
        layout = self.ui.scroll_area_frame.layout()

        # Find the position of the add_template_btn
        add_template_btn_index = -1
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget == self.ui.add_template_btn:
                add_template_btn_index = i
                break

        # Insert the new button before the add_template_btn
        if add_template_btn_index != -1:
            layout.insertWidget(add_template_btn_index, new_button)
        else:
            # Handle the case where add_template_btn is not found
            layout.addWidget(new_button)

        # Optional: Connect signals for the new button if needed
        new_button.clicked.connect(lambda: print("New Template Button Clicked"))



