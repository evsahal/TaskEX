# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instance_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_InstancePage(object):
    def setupUi(self, InstancePage):
        if not InstancePage.objectName():
            InstancePage.setObjectName(u"InstancePage")
        InstancePage.resize(1130, 836)
        InstancePage.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/*\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border: 1px solid rgb(255, 121, 198);\n"
""
                        "	 border-radius: 5px;\n"
"                              \n"
"                        }\n"
"QToolBox::tab:selected {\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"   background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left :10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QTimeEdit {\n"
"  background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left :10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox {\n"
"   background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left :10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
""
                        "	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49,"
                        " 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255)"
                        ";\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollB"
                        "ar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-rad"
                        "ius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 8"
                        "1);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
                        "	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QListWidget{\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QComman"
                        "dLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 2px solid rgb(33, 37, 43);\n"
"  top:-1px; \n"
"	left: 2px;\n"
"  background-color: rgba(40, 44, 52, 0.9);\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"	background-color: rgba(30, 35, 43, 0.9); \n"
"    min-width: 140px; \n"
"    min-height:28px;\n"
"    padding: 0px  0px; \n"
"	color: rgb(255, 121, 198);\n"
" 	border: 2px solid rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"	margin-left:2px;\n"
"    margin-right:2px;\n"
"}\n"
"QTabBar::tab:selected {  \n"
"    color: rgb(161, 110, 235);\n"
"    background-color: rgba(35, 40, 48, 0.9);\n"
"    margin-top: 0px;\n"
"}\n"
"QTabBar::tab:hover {  \n"
"	color: #aaa;\n"
"	background-color: rgb(40, 44, 52);\n"
"    margin-top: 0px;\n"
"}\n"
"\n"
"\n"
"QGroupBox { border: 1px solid  rgb(255, 121, 198); border-radius: 5px; marg"
                        "in-top: 0.5em; }\n"
"QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }\n"
"QGroupBox::title { color: rgb(161, 110, 235); }\n"
"\n"
" QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"*/")
        self.verticalLayout = QVBoxLayout(InstancePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(InstancePage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.run_main_frame = QFrame(self.tab)
        self.run_main_frame.setObjectName(u"run_main_frame")
        self.run_main_frame.setStyleSheet(u"")
        self.run_main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.run_main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.run_main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.run_main_frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.frame_4 = QFrame(self.run_main_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(0,0,0);\n"
"font: 9pt \"Source Code Pro\";\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.textEdit)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.run_main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_run_frame = QFrame(self.frame_3)
        self.top_run_frame.setObjectName(u"top_run_frame")
        self.top_run_frame.setStyleSheet(u"#top_run_frame{ border: 1px solid  rgb(255, 121, 198); border-radius: 5px; margin-top: 0.5em; }")
        self.top_run_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_run_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_run_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_10 = QFrame(self.top_run_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(7, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.frame_10)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(170, 45))

        self.horizontalLayout_8.addWidget(self.comboBox_2)

        self.emu_name_ = QLineEdit(self.frame_10)
        self.emu_name_.setObjectName(u"emu_name_")
        self.emu_name_.setMinimumSize(QSize(180, 45))
        self.emu_name_.setMaximumSize(QSize(200, 16777215))
        self.emu_name_.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.emu_name_)

        self.emu_port_ = QLineEdit(self.frame_10)
        self.emu_port_.setObjectName(u"emu_port_")
        self.emu_port_.setMinimumSize(QSize(0, 45))
        self.emu_port_.setMaximumSize(QSize(90, 16777215))
        self.emu_port_.setMaxLength(10)
        self.emu_port_.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.emu_port_)

        self.run_btn_ = QPushButton(self.frame_10)
        self.run_btn_.setObjectName(u"run_btn_")
        self.run_btn_.setMinimumSize(QSize(45, 45))
        self.run_btn_.setStyleSheet(u"background:transparent;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.run_btn_.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.run_btn_)


        self.horizontalLayout_6.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_11 = QFrame(self.top_run_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 7, 0)
        self.delete_instance_ = QPushButton(self.frame_11)
        self.delete_instance_.setObjectName(u"delete_instance_")
        self.delete_instance_.setMinimumSize(QSize(140, 45))
        self.delete_instance_.setStyleSheet(u"background:transparent;")

        self.horizontalLayout_9.addWidget(self.delete_instance_)


        self.horizontalLayout_6.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.top_run_frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_7 = QFrame(self.groupBox_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_9)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 45))
        self.comboBox.setMaximumSize(QSize(16777215, 45))
        self.comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.preset_save_btn_ = QPushButton(self.widget)
        self.preset_save_btn_.setObjectName(u"preset_save_btn_")
        self.preset_save_btn_.setMinimumSize(QSize(45, 45))
        self.preset_save_btn_.setMaximumSize(QSize(45, 45))
        self.preset_save_btn_.setStyleSheet(u"background:transparent;")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.preset_save_btn_.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.preset_save_btn_)

        self.preset_delete_btn_ = QPushButton(self.widget)
        self.preset_delete_btn_.setObjectName(u"preset_delete_btn_")
        self.preset_delete_btn_.setMinimumSize(QSize(45, 45))
        self.preset_delete_btn_.setMaximumSize(QSize(45, 45))
        self.preset_delete_btn_.setStyleSheet(u"background:transparent;")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.preset_delete_btn_.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.preset_delete_btn_)

        self.preset_add_btn_ = QPushButton(self.widget)
        self.preset_add_btn_.setObjectName(u"preset_add_btn_")
        self.preset_add_btn_.setMinimumSize(QSize(45, 45))
        self.preset_add_btn_.setMaximumSize(QSize(45, 45))
        self.preset_add_btn_.setStyleSheet(u"background:transparent;")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.preset_add_btn_.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.preset_add_btn_)


        self.verticalLayout_9.addWidget(self.widget)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scheduler_table_ = QTableWidget(self.frame_5)
        if (self.scheduler_table_.columnCount() < 2):
            self.scheduler_table_.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.scheduler_table_.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.scheduler_table_.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.scheduler_table_.setObjectName(u"scheduler_table_")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduler_table_.sizePolicy().hasHeightForWidth())
        self.scheduler_table_.setSizePolicy(sizePolicy)
        self.scheduler_table_.setMouseTracking(False)
        self.scheduler_table_.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.scheduler_table_.setAcceptDrops(True)
        self.scheduler_table_.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scheduler_table_.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.scheduler_table_.setDragEnabled(True)
        self.scheduler_table_.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.scheduler_table_.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.scheduler_table_.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.scheduler_table_.setShowGrid(True)
        self.scheduler_table_.setGridStyle(Qt.PenStyle.SolidLine)
        self.scheduler_table_.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.scheduler_table_)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(self.groupBox_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.spinBox = QSpinBox(self.frame_15)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(120, 40))
        self.spinBox.setValue(5)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout_11.addWidget(self.frame_15, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_13)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_11.addWidget(self.checkBox)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 5, 0, 0)
        self.timeEdit = QTimeEdit(self.frame_14)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(110, 40))
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)

        self.gridLayout_2.addWidget(self.timeEdit, 1, 3, 1, 1)

        self.timeEdit_2 = QTimeEdit(self.frame_14)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setMinimumSize(QSize(110, 40))
        self.timeEdit_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)

        self.gridLayout_2.addWidget(self.timeEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_11.addWidget(self.frame_12)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.groupBox_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.profile_settings = QGroupBox(self.frame_17)
        self.profile_settings.setObjectName(u"profile_settings")
        self.profile_settings.setStyleSheet(u"#profile_settings{\n"
"/*border: 1px solid  rgb(29, 33, 38); */\n"
"border: 1px solid #dddddd;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.profile_settings)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_18 = QFrame(self.profile_settings)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_14.addWidget(self.label_6)

        self.comboBox_3 = QComboBox(self.frame_18)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_14.addWidget(self.comboBox_3)

        self.pushButton_6 = QPushButton(self.frame_18)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(45, 45))
        self.pushButton_6.setStyleSheet(u"background:transparent;")
        self.pushButton_6.setIcon(icon3)

        self.horizontalLayout_14.addWidget(self.pushButton_6)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)
        self.horizontalLayout_14.setStretch(2, 1)

        self.verticalLayout_12.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.profile_settings)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_19)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_19)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(45, 45))
        self.pushButton_7.setMaximumSize(QSize(45, 45))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.pushButton_7.setIcon(icon4)

        self.gridLayout_3.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_19)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(45, 45))
        self.pushButton_9.setMaximumSize(QSize(45, 45))
        self.pushButton_9.setIcon(icon2)

        self.gridLayout_3.addWidget(self.pushButton_9, 0, 4, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_19)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(45, 45))
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.pushButton_8.setIcon(icon5)

        self.gridLayout_3.addWidget(self.pushButton_8, 3, 4, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_19)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.comboBox_4, 3, 1, 1, 3)

        self.lineEdit_3 = QLineEdit(self.frame_19)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 2)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.profile_settings)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.frame_20)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 5)

        self.horizontalLayout_13.addWidget(self.profile_settings)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.verticalLayout_7.setStretch(0, 7)

        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 6)

        self.horizontalLayout_5.addWidget(self.groupBox_4)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 6)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 6)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(1, 2)

        self.verticalLayout_2.addWidget(self.run_main_frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(InstancePage)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(InstancePage)
    # setupUi

    def retranslateUi(self, InstancePage):
        InstancePage.setWindowTitle(QCoreApplication.translate("InstancePage", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("InstancePage", u"Panel", None))
        self.groupBox.setTitle(QCoreApplication.translate("InstancePage", u"Console", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("InstancePage", u"Default", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Choose a Profile", None))
        self.emu_name_.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Emulator Name", None))
        self.emu_port_.setInputMask("")
        self.emu_port_.setText("")
        self.emu_port_.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Port No.", None))
        self.run_btn_.setText("")
        self.delete_instance_.setText(QCoreApplication.translate("InstancePage", u"Delete Instance", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("InstancePage", u"Scheduler", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("InstancePage", u"Main Preset", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("InstancePage", u"Alt Preset", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Select Preset", None))
        self.preset_save_btn_.setText("")
        self.preset_delete_btn_.setText("")
        self.preset_add_btn_.setText("")
        ___qtablewidgetitem = self.scheduler_table_.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InstancePage", u"Tasks", None));
        self.label.setText(QCoreApplication.translate("InstancePage", u"Scheduler Status", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("InstancePage", u"Game Settings", None))
        self.label_5.setText(QCoreApplication.translate("InstancePage", u"Kick & Reload", None))
        self.spinBox.setSuffix(QCoreApplication.translate("InstancePage", u"  Mins", None))
        self.checkBox.setText(QCoreApplication.translate("InstancePage", u"Add Break", None))
        self.label_3.setText(QCoreApplication.translate("InstancePage", u"Start Time", None))
        self.label_4.setText(QCoreApplication.translate("InstancePage", u"End Time", None))
        self.profile_settings.setTitle(QCoreApplication.translate("InstancePage", u"Profile Settings", None))
        self.label_6.setText(QCoreApplication.translate("InstancePage", u"Load Profile", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("InstancePage", u"Default", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("InstancePage", u"Alt", None))

        self.pushButton_6.setText("")
        self.label_8.setText(QCoreApplication.translate("InstancePage", u"Copy Profile", None))
        self.pushButton_7.setText("")
        self.label_7.setText(QCoreApplication.translate("InstancePage", u"Profile Name", None))
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("InstancePage", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("InstancePage", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("InstancePage", u"Join Rally", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("InstancePage", u"Monster Hunting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("InstancePage", u"Resource Gathering", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("InstancePage", u"World Map Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("InstancePage", u"Troops Training", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("InstancePage", u"Black Market", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("InstancePage", u"Patrol", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("InstancePage", u"More Activities", None))
    # retranslateUi

