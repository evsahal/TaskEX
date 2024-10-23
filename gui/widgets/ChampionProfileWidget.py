from PySide6.QtWidgets import QWidget

from gui.generated.champion_profile import Ui_ChampionProfile


class ChampionProfileWidget(QWidget):
    def __init__(self, parent=None, flow_layout=None, data=None):
        super(ChampionProfileWidget, self).__init__(parent)
        self.ui = Ui_ChampionProfile()
        self.ui.setupUi(self)

        self.flow_layout = flow_layout
        self.data = data