# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generals_selection.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_GeneralsSelectionDialog(object):
    def setupUi(self, GeneralsSelectionDialog):
        if not GeneralsSelectionDialog.objectName():
            GeneralsSelectionDialog.setObjectName(u"GeneralsSelectionDialog")
        GeneralsSelectionDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        GeneralsSelectionDialog.resize(679, 760)
        GeneralsSelectionDialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QListWidget */\n"
"QListWidget {\n"
"    background-color: #222; /* Dark base background */\n"
"    border: none; /* Remove default border */\n"
"    color: #d3d3d3; /* Lighter text color for contrast */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: rgba(40, 44, 52, 0.8); /* Slightly lighter background for items */\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.15); /* Subtle separator */\n"
"    padding: 10px; /* Adjust spacing around text"
                        " */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: rgba(50, 55, 65, 0.9); /* Highlight on hover */\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.25); /* Enhanced separator */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color:  rgba(40, 44, 52, 0.8); /* Darker background for selected items */\n"
"    color: #ffffff; /* White text for better visibility */\n"
"}\n"
"\n"
"\n"
"/* QTabBar */\n"
"QTabWidget::pane {\n"
"  border: 2px solid rgb(33, 37, 43);\n"
"  top:-1px; \n"
"  left:2px;\n"
"  background-color: rgba(40, 44, 52, 0.9);\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"	background-color: rgba(30, 35, 43, 0.9); \n"
"   /* background-color: rgba(50, 55, 65, 0.9);*/\n"
"    min-width: 150px; \n"
"    min-height:28px;\n"
"    padding: 0px  0px; \n"
"    /*color: #aaa;*/\n"
"	color: rgb(255, 121, 198);\n"
" 	border: 2px solid rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    margin-left:2px;\n"
"    margin-right:2px;\n"
"}\n"
"QTabBar::tab:selected {  \n"
"    color: rg"
                        "b(161, 110, 235);\n"
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
"\n"
"QPushButton {\n"
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
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-rep"
                        "eat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel { font-size: 11px; color: rgb(113, 126, 149);  }\n"
"\n"
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
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49"
                        ", 60);\n"
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
"/* //////////////////////////////////////////////////////////////////////////////////////////////"
                        "///\n"
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
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    backg"
                        "round: rgb(55, 63, 77);\n"
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
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    "
                        " border: none;\n"
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
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBo"
                        "x::indicator:hover {\n"
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
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rg"
                        "b(33, 37, 43);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);"
                        "\n"
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
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {"
                        "\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
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
"\n"
"/* QGroupBox */\n"
"QGroupBox { border: 1px solid  rgb(255, 121, 198); border-radius: 5px; margin-top: 0.5em; }\n"
"QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }\n"
"QGroupBox::title { color: rgb(161, 110, 235); }\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(GeneralsSelectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(GeneralsSelectionDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(GeneralsSelectionDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_3.addWidget(self.label_2)

        self.all_generals_main = QListWidget(self.frame_4)
        self.all_generals_main.setObjectName(u"all_generals_main")
        self.all_generals_main.setAcceptDrops(True)
        self.all_generals_main.setFrameShape(QFrame.Shape.Panel)
        self.all_generals_main.setFrameShadow(QFrame.Shadow.Raised)
        self.all_generals_main.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.all_generals_main.setDragEnabled(False)
        self.all_generals_main.setDragDropOverwriteMode(False)
        self.all_generals_main.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.all_generals_main.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.all_generals_main.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.all_generals_main.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.all_generals_main.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.all_generals_main.setMovement(QListView.Movement.Snap)
        self.all_generals_main.setFlow(QListView.Flow.TopToBottom)
        self.all_generals_main.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.all_generals_main.setSpacing(2)
        self.all_generals_main.setViewMode(QListView.ViewMode.ListMode)
        self.all_generals_main.setWordWrap(True)
        self.all_generals_main.setSelectionRectVisible(False)
        self.all_generals_main.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.all_generals_main)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.selected_generals_main = QListWidget(self.frame_5)
        self.selected_generals_main.setObjectName(u"selected_generals_main")
        self.selected_generals_main.setAcceptDrops(True)
        self.selected_generals_main.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.selected_generals_main.setDragEnabled(False)
        self.selected_generals_main.setDragDropOverwriteMode(False)
        self.selected_generals_main.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.selected_generals_main.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.selected_generals_main.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.selected_generals_main.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.selected_generals_main.setMovement(QListView.Movement.Snap)
        self.selected_generals_main.setSpacing(2)
        self.selected_generals_main.setWordWrap(True)
        self.selected_generals_main.setSortingEnabled(False)

        self.verticalLayout_4.addWidget(self.selected_generals_main)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalLayout_5.setStretch(0, 7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_7.addWidget(self.label_4)

        self.all_generals_assistant = QListWidget(self.frame_6)
        self.all_generals_assistant.setObjectName(u"all_generals_assistant")
        self.all_generals_assistant.setFrameShape(QFrame.Shape.Panel)
        self.all_generals_assistant.setFrameShadow(QFrame.Shadow.Raised)
        self.all_generals_assistant.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.all_generals_assistant.setDragEnabled(False)
        self.all_generals_assistant.setDragDropOverwriteMode(False)
        self.all_generals_assistant.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.all_generals_assistant.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.all_generals_assistant.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.all_generals_assistant.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.all_generals_assistant.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.all_generals_assistant.setMovement(QListView.Movement.Snap)
        self.all_generals_assistant.setFlow(QListView.Flow.TopToBottom)
        self.all_generals_assistant.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.all_generals_assistant.setSpacing(2)
        self.all_generals_assistant.setViewMode(QListView.ViewMode.ListMode)
        self.all_generals_assistant.setWordWrap(True)
        self.all_generals_assistant.setSelectionRectVisible(False)
        self.all_generals_assistant.setSortingEnabled(True)

        self.verticalLayout_7.addWidget(self.all_generals_assistant)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_8.addWidget(self.label_5)

        self.selected_generals_assistant = QListWidget(self.frame_7)
        self.selected_generals_assistant.setObjectName(u"selected_generals_assistant")
        self.selected_generals_assistant.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.selected_generals_assistant.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.selected_generals_assistant.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.selected_generals_assistant.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.selected_generals_assistant.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.selected_generals_assistant.setMovement(QListView.Movement.Snap)
        self.selected_generals_assistant.setSpacing(2)
        self.selected_generals_assistant.setWordWrap(True)
        self.selected_generals_assistant.setSortingEnabled(False)

        self.verticalLayout_8.addWidget(self.selected_generals_assistant)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.verticalLayout_10.setStretch(0, 7)
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_8 = QFrame(GeneralsSelectionDialog)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(11, 0, 11, 0)
        self.groupBox_3 = QGroupBox(self.frame_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_9 = QFrame(self.groupBox_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 7, 0, 7)
        self.widget_7 = QWidget(self.frame_9)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 11)
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.general_category_dd = QComboBox(self.widget_7)
        self.general_category_dd.addItem("")
        self.general_category_dd.addItem("")
        self.general_category_dd.addItem("")
        self.general_category_dd.addItem("")
        self.general_category_dd.addItem("")
        self.general_category_dd.setObjectName(u"general_category_dd")
        self.general_category_dd.setMinimumSize(QSize(0, 0))
        self.general_category_dd.setMaximumSize(QSize(160, 16777215))

        self.verticalLayout_14.addWidget(self.general_category_dd)


        self.horizontalLayout_5.addWidget(self.widget_7)

        self.general_filter_widget = QWidget(self.frame_9)
        self.general_filter_widget.setObjectName(u"general_filter_widget")

        self.horizontalLayout_5.addWidget(self.general_filter_widget)

        self.widget_2 = QWidget(self.frame_9)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.swipe_attempts = QSpinBox(self.widget_2)
        self.swipe_attempts.setObjectName(u"swipe_attempts")
        self.swipe_attempts.setMinimumSize(QSize(100, 35))
        self.swipe_attempts.setMaximumSize(QSize(100, 35))
        self.swipe_attempts.setMaximum(20)
        self.swipe_attempts.setProperty(u"profile_id", 0)

        self.verticalLayout_9.addWidget(self.swipe_attempts)


        self.horizontalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_16.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_3 = QFrame(GeneralsSelectionDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.exit_general_selection = QPushButton(self.frame_3)
        self.exit_general_selection.setObjectName(u"exit_general_selection")
        self.exit_general_selection.setMinimumSize(QSize(80, 32))

        self.horizontalLayout_3.addWidget(self.exit_general_selection, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(GeneralsSelectionDialog)

        self.tabWidget.setCurrentIndex(0)
        self.general_category_dd.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GeneralsSelectionDialog)
    # setupUi

    def retranslateUi(self, GeneralsSelectionDialog):
        GeneralsSelectionDialog.setWindowTitle(QCoreApplication.translate("GeneralsSelectionDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Rally General Selection", None))
        self.label_2.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"All Generals", None))
        self.all_generals_main.setProperty(u"item_info", "")
        self.label_3.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Selected Generals", None))
        self.selected_generals_main.setProperty(u"item_info", "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("GeneralsSelectionDialog", u"Main General", None))
        self.label_4.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"All Generals", None))
        self.all_generals_assistant.setProperty(u"item_info", "")
        self.label_5.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Selected Generals", None))
        self.selected_generals_assistant.setProperty(u"item_info", "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("GeneralsSelectionDialog", u"Assistant General", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("GeneralsSelectionDialog", u"Filter Settings", None))
        self.label_9.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"General Category", None))
        self.general_category_dd.setItemText(0, QCoreApplication.translate("GeneralsSelectionDialog", u"All", None))
        self.general_category_dd.setItemText(1, QCoreApplication.translate("GeneralsSelectionDialog", u"Military", None))
        self.general_category_dd.setItemText(2, QCoreApplication.translate("GeneralsSelectionDialog", u"Development", None))
        self.general_category_dd.setItemText(3, QCoreApplication.translate("GeneralsSelectionDialog", u"Duty", None))
        self.general_category_dd.setItemText(4, QCoreApplication.translate("GeneralsSelectionDialog", u"Subordinate City", None))

        self.label_6.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Swipe Attempts", None))
        self.swipe_attempts.setSuffix(QCoreApplication.translate("GeneralsSelectionDialog", u" Times", None))
        self.exit_general_selection.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Exit", None))
    # retranslateUi

