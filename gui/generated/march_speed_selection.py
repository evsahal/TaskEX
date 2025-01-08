# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'march_speed_selection.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MarchSpeedSelectionDialog(object):
    def setupUi(self, MarchSpeedSelectionDialog):
        if not MarchSpeedSelectionDialog.objectName():
            MarchSpeedSelectionDialog.setObjectName(u"MarchSpeedSelectionDialog")
        MarchSpeedSelectionDialog.resize(504, 559)
        self.verticalLayout = QVBoxLayout(MarchSpeedSelectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(MarchSpeedSelectionDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(MarchSpeedSelectionDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(MarchSpeedSelectionDialog)

        QMetaObject.connectSlotsByName(MarchSpeedSelectionDialog)
    # setupUi

    def retranslateUi(self, MarchSpeedSelectionDialog):
        MarchSpeedSelectionDialog.setWindowTitle(QCoreApplication.translate("MarchSpeedSelectionDialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("MarchSpeedSelectionDialog", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("MarchSpeedSelectionDialog", u"Save", None))
    # retranslateUi

