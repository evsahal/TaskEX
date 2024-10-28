# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'champion_profile.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QWidget)

class Ui_ChampionProfile(object):
    def setupUi(self, ChampionProfile):
        if not ChampionProfile.objectName():
            ChampionProfile.setObjectName(u"ChampionProfile")
        ChampionProfile.resize(327, 246)
        self.horizontalLayout = QHBoxLayout(ChampionProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(ChampionProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(ChampionProfile)

        QMetaObject.connectSlotsByName(ChampionProfile)
    # setupUi

    def retranslateUi(self, ChampionProfile):
        ChampionProfile.setWindowTitle(QCoreApplication.translate("ChampionProfile", u"Form", None))
    # retranslateUi

