# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from core.custom_widgets.QCheckComboBox import QCheckComboBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1328, 852)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border: 1px solid rgb(255, 121, 198);\n"
"	 border-radius: 5px;\n"
"                              \n"
"                        }\n"
"QToolBox::tab:selected {\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/*\n"
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
"QDoubleSpinBox {\n"
"   background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding"
                        "-left :10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"} */\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
""
                        "#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-"
                        "align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
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
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color:"
                        " rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/cil-clone.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	bo"
                        "rder-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	backgroun"
                        "d-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
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
"    border-bottom: 1px"
                        " solid rgb(44, 49, 60);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* ////////////////////////////"
                        "/////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
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
"QSc"
                        "rollBar::add-line:horizontal {\n"
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
"	borde"
                        "r-radius: 4px\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-rad"
                        "ius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: r"
                        "gb(27, 29, 35);\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    "
                        "height: 10px;\n"
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
"    background-"
                        "color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QListWidget */\n"
"QListWidget{\n"
"	border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* QTabBar */\n"
"QTabWidget::pane {\n"
"  border: 2px solid rgb(33, 37, 43);\n"
"  top:-1px; \n"
"	left: 2px;\n"
"  background-color: rgba(40, 44, 52, 0.9);\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"	background-color: rgba(30, 35, 43"
                        ", 0.9); \n"
"   /* background-color: rgba(50, 55, 65, 0.9);*/\n"
"    min-width: 140px; \n"
"    min-height:28px;\n"
"    padding: 0px  0px; \n"
"    /*color: #aaa;*/\n"
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
"    /*color: rgb(161, 110, 235);*/\n"
"	color: #aaa;\n"
"	background-color: rgb(40, 44, 52);\n"
"   /* background-color: rgba(255, 255, 255, 100);*/\n"
"    margin-top: 0px;\n"
"}\n"
"\n"
"/* QGroupBox */\n"
"QGroupBox { border: 1px solid  rgb(255, 121, 198); border-radius: 5px; margin-top: 0.5em; }\n"
"QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }\n"
"QGroupBox::title { color: rgb(161, 110, 235); }\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////"
                        "/////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"font-weight:normal;")
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_task_manager = QPushButton(self.topMenu)
        self.btn_task_manager.setObjectName(u"btn_task_manager")
        self.btn_task_manager.setMinimumSize(QSize(0, 45))
        self.btn_task_manager.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-library-add.png);")

        self.verticalLayout_8.addWidget(self.btn_task_manager)

        self.btn_coordinate_manager = QPushButton(self.topMenu)
        self.btn_coordinate_manager.setObjectName(u"btn_coordinate_manager")
        self.btn_coordinate_manager.setMinimumSize(QSize(0, 45))
        self.btn_coordinate_manager.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-map.png);")

        self.verticalLayout_8.addWidget(self.btn_coordinate_manager)

        self.btn_add = QPushButton(self.topMenu)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QSize(0, 45))
        self.btn_add.setFont(font)
        self.btn_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_add.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-plus.png)")

        self.verticalLayout_8.addWidget(self.btn_add)

        self.btn_bot_manager = QPushButton(self.topMenu)
        self.btn_bot_manager.setObjectName(u"btn_bot_manager")
        sizePolicy.setHeightForWidth(self.btn_bot_manager.sizePolicy().hasHeightForWidth())
        self.btn_bot_manager.setSizePolicy(sizePolicy)
        self.btn_bot_manager.setMinimumSize(QSize(0, 45))
        self.btn_bot_manager.setFont(font)
        self.btn_bot_manager.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_bot_manager.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_bot_manager.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_bot_manager)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clone.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.extraTopMenu.sizePolicy().hasHeightForWidth())
        self.extraTopMenu.setSizePolicy(sizePolicy1)
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.port_display_table = QTableWidget(self.extraTopMenu)
        if (self.port_display_table.columnCount() < 3):
            self.port_display_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.port_display_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.port_display_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.port_display_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.port_display_table.setObjectName(u"port_display_table")
        self.port_display_table.setMaximumSize(QSize(16777215, 165))
        self.port_display_table.setStyleSheet(u"QTableWidget {\n"
"	border: 1px solid black;\n"
"}\n"
"QTableWidget::item {\n"
"	border: 1px solid black;\n"
"}")
        self.port_display_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.port_display_table.setAlternatingRowColors(False)
        self.port_display_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.port_display_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.port_display_table.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.port_display_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.port_display_table.setCornerButtonEnabled(True)
        self.port_display_table.horizontalHeader().setVisible(True)
        self.port_display_table.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.port_display_table)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.extraCenter.sizePolicy().hasHeightForWidth())
        self.extraCenter.setSizePolicy(sizePolicy2)
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.extraCenterArea = QScrollArea(self.extraCenter)
        self.extraCenterArea.setObjectName(u"extraCenterArea")
        self.extraCenterArea.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.extraCenterArea.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenterArea.setFrameShadow(QFrame.Shadow.Plain)
        self.extraCenterArea.setLineWidth(0)
        self.extraCenterArea.setWidgetResizable(True)
        self.extraCenterAreaWidgetContents = QWidget()
        self.extraCenterAreaWidgetContents.setObjectName(u"extraCenterAreaWidgetContents")
        self.extraCenterAreaWidgetContents.setGeometry(QRect(0, 0, 16, 537))
        self.extraCenterArea.setWidget(self.extraCenterAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.extraCenterArea)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        sizePolicy1.setHeightForWidth(self.extraBottom.sizePolicy().hasHeightForWidth())
        self.extraBottom.setSizePolicy(sizePolicy1)
        self.extraBottom.setMinimumSize(QSize(0, 45))
        self.extraBottom.setMaximumSize(QSize(16777215, 45))
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font-weight: normal;")
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.coordinate_manager = QWidget()
        self.coordinate_manager.setObjectName(u"coordinate_manager")
        self.verticalLayout_21 = QVBoxLayout(self.coordinate_manager)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_2 = QLabel(self.coordinate_manager)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.coordinate_manager)
        self.task_manager = QWidget()
        self.task_manager.setObjectName(u"task_manager")
        self.task_manager.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.task_manager)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.task_manager)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.task_manager)
        self.bot_manager = QWidget()
        self.bot_manager.setObjectName(u"bot_manager")
        self.bot_manager.setStyleSheet(u"QComboBox{\n"
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
"}")
        self.verticalLayout_20 = QVBoxLayout(self.bot_manager)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tabWidget = QTabWidget(self.bot_manager)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.scan_generals = QWidget()
        self.scan_generals.setObjectName(u"scan_generals")
        sizePolicy2.setHeightForWidth(self.scan_generals.sizePolicy().hasHeightForWidth())
        self.scan_generals.setSizePolicy(sizePolicy2)
        self.verticalLayout_17 = QVBoxLayout(self.scan_generals)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_3 = QFrame(self.scan_generals)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scan_generals_category = QComboBox(self.frame_8)
        self.scan_generals_category.addItem("")
        self.scan_generals_category.addItem("")
        self.scan_generals_category.addItem("")
        self.scan_generals_category.addItem("")
        self.scan_generals_category.addItem("")
        self.scan_generals_category.setObjectName(u"scan_generals_category")
        self.scan_generals_category.setMinimumSize(QSize(0, 45))
        self.scan_generals_category.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.scan_generals_category)

        self.scan_generals_view = QComboBox(self.frame_8)
        self.scan_generals_view.addItem("")
        self.scan_generals_view.addItem("")
        self.scan_generals_view.setObjectName(u"scan_generals_view")
        sizePolicy1.setHeightForWidth(self.scan_generals_view.sizePolicy().hasHeightForWidth())
        self.scan_generals_view.setSizePolicy(sizePolicy1)
        self.scan_generals_view.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_16.addWidget(self.scan_generals_view)

        self.scan_generals_type = QCheckComboBox(self.frame_8)
        self.scan_generals_type.addItem("")
        self.scan_generals_type.addItem("")
        self.scan_generals_type.setObjectName(u"scan_generals_type")
        self.scan_generals_type.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_16.addWidget(self.scan_generals_type)

        self.scan_generals_filter = QCheckComboBox(self.frame_8)
        self.scan_generals_filter.addItem("")
        self.scan_generals_filter.addItem("")
        self.scan_generals_filter.setObjectName(u"scan_generals_filter")
        self.scan_generals_filter.setMinimumSize(QSize(130, 45))

        self.horizontalLayout_16.addWidget(self.scan_generals_filter)

        self.scan_generals_port = QLineEdit(self.frame_8)
        self.scan_generals_port.setObjectName(u"scan_generals_port")
        self.scan_generals_port.setMinimumSize(QSize(0, 45))
        self.scan_generals_port.setMaximumSize(QSize(100, 16777215))
        self.scan_generals_port.setMaxLength(10)
        self.scan_generals_port.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.scan_generals_port)

        self.scan_generals_btn = QPushButton(self.frame_8)
        self.scan_generals_btn.setObjectName(u"scan_generals_btn")
        self.scan_generals_btn.setMinimumSize(QSize(140, 45))

        self.horizontalLayout_16.addWidget(self.scan_generals_btn)


        self.horizontalLayout_7.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignLeft)

        self.toggle_general_view_frame = QFrame(self.frame_3)
        self.toggle_general_view_frame.setObjectName(u"toggle_general_view_frame")
        self.toggle_general_view_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.toggle_general_view_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.toggle_general_view_frame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scan_generals)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bm_generals_scroll_area = QScrollArea(self.frame_4)
        self.bm_generals_scroll_area.setObjectName(u"bm_generals_scroll_area")
        self.bm_generals_scroll_area.setStyleSheet(u"#bm_generals_scroll_area{\n"
"	border: 1px solid  rgb(255, 121, 198); border-radius: 5px;margin-top: 0.2em\n"
"}")
        self.bm_generals_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.bm_generals_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 925, 586))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.generals_list_frame = QFrame(self.scrollAreaWidgetContents)
        self.generals_list_frame.setObjectName(u"generals_list_frame")
        self.generals_list_frame.setStyleSheet(u"")
        self.generals_list_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.generals_list_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.generals_list_frame)

        self.bm_generals_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_15.addWidget(self.bm_generals_scroll_area)

        self.scan_general_console_frame = QFrame(self.frame_4)
        self.scan_general_console_frame.setObjectName(u"scan_general_console_frame")
        self.scan_general_console_frame.setStyleSheet(u"#scan_general_console_frame{ border: 1px solid  rgb(255, 121, 198); border-radius: 5px;margin-top: 0.2em}\n"
"\n"
"/* */")
        self.scan_general_console_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_general_console_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.scan_general_console_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scan_general_console = QPlainTextEdit(self.scan_general_console_frame)
        self.scan_general_console.setObjectName(u"scan_general_console")
        self.scan_general_console.setStyleSheet(u"background-color: rgb(0,0,0);\n"
"font: 9pt \"Source Code Pro\";\n"
"border-radius: 5px;")
        self.scan_general_console.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.scan_general_console)

        self.general_preset_btn = QPushButton(self.scan_general_console_frame)
        self.general_preset_btn.setObjectName(u"general_preset_btn")
        self.general_preset_btn.setMinimumSize(QSize(0, 45))

        self.verticalLayout_19.addWidget(self.general_preset_btn)


        self.horizontalLayout_15.addWidget(self.scan_general_console_frame)

        self.horizontalLayout_15.setStretch(0, 8)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_17.addWidget(self.frame_4)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 10)
        self.tabWidget.addTab(self.scan_generals, "")
        self.monsters = QWidget()
        self.monsters.setObjectName(u"monsters")
        self.verticalLayout_16 = QVBoxLayout(self.monsters)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame = QFrame(self.monsters)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.upload_monsters_btn = QPushButton(self.frame)
        self.upload_monsters_btn.setObjectName(u"upload_monsters_btn")
        self.upload_monsters_btn.setMinimumSize(QSize(150, 45))
        self.upload_monsters_btn.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_11.addWidget(self.upload_monsters_btn)

        self.export_monster_btn_frame = QFrame(self.frame)
        self.export_monster_btn_frame.setObjectName(u"export_monster_btn_frame")
        self.export_monster_btn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.export_monster_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.export_monster_btn_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.export_monsters_btn = QPushButton(self.export_monster_btn_frame)
        self.export_monsters_btn.setObjectName(u"export_monsters_btn")
        self.export_monsters_btn.setMinimumSize(QSize(150, 45))
        self.export_monsters_btn.setMaximumSize(QSize(16777215, 45))
        self.export_monsters_btn.setStyleSheet(u"QPushButton:checked {\n"
"        background-color: rgb(57, 65, 80);\n"
"		border: 2px solid rgb(43, 50, 61);\n"
"    }")
        self.export_monsters_btn.setCheckable(True)
        self.export_monsters_btn.setChecked(False)

        self.horizontalLayout_13.addWidget(self.export_monsters_btn)


        self.horizontalLayout_11.addWidget(self.export_monster_btn_frame)


        self.verticalLayout_16.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.monsters)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bm_monsters_scroll_area = QScrollArea(self.frame_2)
        self.bm_monsters_scroll_area.setObjectName(u"bm_monsters_scroll_area")
        self.bm_monsters_scroll_area.setStyleSheet(u"#bm_monsters_scroll_area{\n"
"	border: 1px solid  rgb(255, 121, 198); border-radius: 5px;margin-top: 0.2em \n"
"}")
        self.bm_monsters_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.bm_monsters_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1166, 513))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.monsters_list_frame = QFrame(self.scrollAreaWidgetContents_2)
        self.monsters_list_frame.setObjectName(u"monsters_list_frame")
        self.monsters_list_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.monsters_list_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_14.addWidget(self.monsters_list_frame)

        self.bm_monsters_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_12.addWidget(self.bm_monsters_scroll_area)


        self.verticalLayout_16.addWidget(self.frame_2)

        self.export_monster_confirm_frame = QFrame(self.monsters)
        self.export_monster_confirm_frame.setObjectName(u"export_monster_confirm_frame")
        self.export_monster_confirm_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.export_monster_confirm_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.export_monster_confirm_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cancel_export_btn = QPushButton(self.export_monster_confirm_frame)
        self.cancel_export_btn.setObjectName(u"cancel_export_btn")
        self.cancel_export_btn.setMinimumSize(QSize(100, 45))

        self.horizontalLayout_6.addWidget(self.cancel_export_btn)

        self.confirm_export_btn = QPushButton(self.export_monster_confirm_frame)
        self.confirm_export_btn.setObjectName(u"confirm_export_btn")
        self.confirm_export_btn.setMinimumSize(QSize(100, 45))

        self.horizontalLayout_6.addWidget(self.confirm_export_btn)


        self.verticalLayout_16.addWidget(self.export_monster_confirm_frame, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 10)
        self.verticalLayout_16.setStretch(2, 1)
        self.tabWidget.addTab(self.monsters, "")
        self.black_market = QWidget()
        self.black_market.setObjectName(u"black_market")
        self.horizontalLayout_10 = QHBoxLayout(self.black_market)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_6 = QFrame(self.black_market)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bm_black_market_scroll_area = QScrollArea(self.frame_6)
        self.bm_black_market_scroll_area.setObjectName(u"bm_black_market_scroll_area")
        self.bm_black_market_scroll_area.setStyleSheet(u"#bm_black_market_scroll_area{\n"
"	border: 1px solid  rgb(255, 121, 198); border-radius: 5px;margin-top: 0.2em\n"
"}")
        self.bm_black_market_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1166, 646))
        self.horizontalLayout_17 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.blackmarket_list_frame = QFrame(self.scrollAreaWidgetContents_4)
        self.blackmarket_list_frame.setObjectName(u"blackmarket_list_frame")
        self.blackmarket_list_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.blackmarket_list_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_17.addWidget(self.blackmarket_list_frame)

        self.bm_black_market_scroll_area.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_23.addWidget(self.bm_black_market_scroll_area)


        self.horizontalLayout_10.addWidget(self.frame_6)

        self.tabWidget.addTab(self.black_market, "")
        self.champions = QWidget()
        self.champions.setObjectName(u"champions")
        self.horizontalLayout_8 = QHBoxLayout(self.champions)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_5 = QFrame(self.champions)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bm_champions_scroll_area = QScrollArea(self.frame_5)
        self.bm_champions_scroll_area.setObjectName(u"bm_champions_scroll_area")
        self.bm_champions_scroll_area.setStyleSheet(u"#bm_champions_scroll_area{\n"
"	border: 1px solid  rgb(255, 121, 198); border-radius: 5px;margin-top: 0.2em\n"
"}")
        self.bm_champions_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1166, 646))
        self.horizontalLayout_18 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.champions_list_frame = QFrame(self.scrollAreaWidgetContents_3)
        self.champions_list_frame.setObjectName(u"champions_list_frame")
        self.champions_list_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.champions_list_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_18.addWidget(self.champions_list_frame)

        self.bm_champions_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_22.addWidget(self.bm_champions_scroll_area)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.tabWidget.addTab(self.champions, "")

        self.verticalLayout_20.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.bot_manager)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_support = QPushButton(self.topMenus)
        self.btn_support.setObjectName(u"btn_support")
        sizePolicy.setHeightForWidth(self.btn_support.sizePolicy().hasHeightForWidth())
        self.btn_support.setSizePolicy(sizePolicy)
        self.btn_support.setMinimumSize(QSize(0, 45))
        self.btn_support.setFont(font)
        self.btn_support.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_support.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_support.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-coffee.png);")

        self.verticalLayout_14.addWidget(self.btn_support)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        self.scan_generals_category.setCurrentIndex(0)
        self.scan_generals_view.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"TaskEX", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_task_manager.setText(QCoreApplication.translate("MainWindow", u"Task Manager", None))
        self.btn_coordinate_manager.setText(QCoreApplication.translate("MainWindow", u"Coordinate Manager", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Create Instance", None))
        self.btn_bot_manager.setText(QCoreApplication.translate("MainWindow", u"Bot Manager", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Instance Manager", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Instance Manager", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        ___qtablewidgetitem = self.port_display_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Emulator Name", None));
        ___qtablewidgetitem1 = self.port_display_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Port No.", None));
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\n"
"<html><head/><body><span style=\" font-size:12pt;font-weight:bold;\">TaskEnforcerX - </span> <span style=\" font-size:10pt;\">Smart Automation For Evony</span></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Collective", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Task Manager", None))
        self.scan_generals_category.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.scan_generals_category.setItemText(1, QCoreApplication.translate("MainWindow", u"Military", None))
        self.scan_generals_category.setItemText(2, QCoreApplication.translate("MainWindow", u"Development", None))
        self.scan_generals_category.setItemText(3, QCoreApplication.translate("MainWindow", u"Duty", None))
        self.scan_generals_category.setItemText(4, QCoreApplication.translate("MainWindow", u"Subordinate City", None))

        self.scan_generals_category.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scan Category", None))
        self.scan_generals_view.setItemText(0, QCoreApplication.translate("MainWindow", u"Details View", None))
        self.scan_generals_view.setItemText(1, QCoreApplication.translate("MainWindow", u"List View", None))

        self.scan_generals_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scan View", None))
        self.scan_generals_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Epic Historic", None))
        self.scan_generals_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Legendary Historic", None))

        self.scan_generals_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scan Type", None))
        self.scan_generals_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"Favorite", None))
        self.scan_generals_filter.setItemText(1, QCoreApplication.translate("MainWindow", u"Idle", None))

        self.scan_generals_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scan Filter", None))
        self.scan_generals_port.setText("")
        self.scan_generals_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port No.", None))
        self.scan_generals_btn.setText(QCoreApplication.translate("MainWindow", u"Scan Generals", None))
        self.scan_general_console.setPlainText(QCoreApplication.translate("MainWindow", u"Note: Double-tap on the general's name tag to rename it.\n"
"", None))
        self.general_preset_btn.setText(QCoreApplication.translate("MainWindow", u"Manage General Presets", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_generals), QCoreApplication.translate("MainWindow", u"Scan Generals", None))
        self.upload_monsters_btn.setText(QCoreApplication.translate("MainWindow", u"Upload Monsters", None))
        self.export_monsters_btn.setText(QCoreApplication.translate("MainWindow", u"Export Monsters", None))
        self.cancel_export_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confirm_export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monsters), QCoreApplication.translate("MainWindow", u"Monsters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.black_market), QCoreApplication.translate("MainWindow", u"Black Market", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.champions), QCoreApplication.translate("MainWindow", u"Champions", None))
        self.btn_support.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: ", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

