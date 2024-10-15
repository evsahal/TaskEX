# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monster_upload_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Monster_Upload_Dialog(object):
    def setupUi(self, Monster_Upload_Dialog):
        if not Monster_Upload_Dialog.objectName():
            Monster_Upload_Dialog.setObjectName(u"Monster_Upload_Dialog")
        Monster_Upload_Dialog.resize(779, 775)
        self.verticalLayout = QVBoxLayout(Monster_Upload_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Monster_Upload_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 11, 0, 11)
        self.add_monster_btn = QPushButton(self.frame)
        self.add_monster_btn.setObjectName(u"add_monster_btn")
        self.add_monster_btn.setMinimumSize(QSize(130, 40))

        self.horizontalLayout.addWidget(self.add_monster_btn)

        self.import_monster_btn = QPushButton(self.frame)
        self.import_monster_btn.setObjectName(u"import_monster_btn")
        self.import_monster_btn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout.addWidget(self.import_monster_btn)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(Monster_Upload_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 755, 403))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 0, 5)
        self.monsters_list_frame = QFrame(self.widget)
        self.monsters_list_frame.setObjectName(u"monsters_list_frame")
        self.monsters_list_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.monsters_list_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.monsters_list_frame)

        self.scrollArea.setWidget(self.widget)

        self.horizontalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Monster_Upload_Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"font: 10pt \"Source Code Pro\";")
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.plainTextEdit)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(Monster_Upload_Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 11, 0, -1)
        self.upload_monsters_btn = QPushButton(self.frame_4)
        self.upload_monsters_btn.setObjectName(u"upload_monsters_btn")
        self.upload_monsters_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.upload_monsters_btn)

        self.exit_btn = QPushButton(self.frame_4)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.exit_btn)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Monster_Upload_Dialog)

        QMetaObject.connectSlotsByName(Monster_Upload_Dialog)
    # setupUi

    def retranslateUi(self, Monster_Upload_Dialog):
        Monster_Upload_Dialog.setWindowTitle(QCoreApplication.translate("Monster_Upload_Dialog", u"Upload Monsters", None))
        self.add_monster_btn.setText(QCoreApplication.translate("Monster_Upload_Dialog", u"Add Monster", None))
        self.import_monster_btn.setText(QCoreApplication.translate("Monster_Upload_Dialog", u"Import Monster", None))
        self.plainTextEdit.setDocumentTitle("")
        self.upload_monsters_btn.setText(QCoreApplication.translate("Monster_Upload_Dialog", u"Upload Monsters", None))
        self.exit_btn.setText(QCoreApplication.translate("Monster_Upload_Dialog", u"Exit", None))
    # retranslateUi

