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

from core.custom_widgets.QCheckComboBox import QCheckComboBox

class Ui_GeneralsSelectionDialog(object):
    def setupUi(self, GeneralsSelectionDialog):
        if not GeneralsSelectionDialog.objectName():
            GeneralsSelectionDialog.setObjectName(u"GeneralsSelectionDialog")
        GeneralsSelectionDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        GeneralsSelectionDialog.resize(695, 760)
        GeneralsSelectionDialog.setStyleSheet(u"QDialog{\n"
"background-color: rgba(40, 44, 52, 0.9);\n"
"}\n"
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
"    padding: 10px; /* Adjust spacing around text */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: rgba(50, 55, 65, 0.9); /* Highlight on hover */\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.25); /* Enhanced separator */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color:  rgba(40, 44, 52, 0.8); /* Darker background for selected items */\n"
"    color: #ffffff; /* White text for b"
                        "etter visibility */\n"
"}\n"
"\n"
"\n"
"/* QTabBar */\n"
"QTabWidget::pane {\n"
"  border: 2px solid rgb(33, 37, 43);\n"
"  top:-1px; \n"
"  left:2px;\n"
"  background-color: rgba(30, 35, 43, 0.9); \n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"    background-color: rgba(35, 40, 48, 0.9);\n"
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
"    color: rgb(161, 110, 235);\n"
"    background-color: rgba(30, 35, 43, 0.9); \n"
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
"\n"
"\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////////////////////"
                        "/////\n"
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
"\n"
"\n"
"QLabel { font-size: 11px; color: rgb(113, 126, 149);  }\n"
"\n"
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
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	bord"
                        "er-top-right-radius: 4px;\n"
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
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
""
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
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QCo"
                        "mboBox::drop-down {\n"
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
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_10)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.manage_preset_frame = QFrame(self.groupBox)
        self.manage_preset_frame.setObjectName(u"manage_preset_frame")
        self.manage_preset_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.manage_preset_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.manage_preset_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.preset_combobox = QComboBox(self.manage_preset_frame)
        self.preset_combobox.addItem("")
        self.preset_combobox.setObjectName(u"preset_combobox")
        self.preset_combobox.setMinimumSize(QSize(180, 40))

        self.horizontalLayout_6.addWidget(self.preset_combobox)

        self.edit_btn = QPushButton(self.manage_preset_frame)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(40, 40))
        self.edit_btn.setMaximumSize(QSize(40, 40))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.edit_btn.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.edit_btn)

        self.delete_btn = QPushButton(self.manage_preset_frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(40, 40))
        self.delete_btn.setMaximumSize(QSize(40, 40))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_btn.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.delete_btn)

        self.add_btn = QPushButton(self.manage_preset_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(40, 40))
        self.add_btn.setMaximumSize(QSize(40, 40))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_btn.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.add_btn)


        self.horizontalLayout_8.addWidget(self.manage_preset_frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_12 = QFrame(self.groupBox)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.save_btn = QPushButton(self.frame_12)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(130, 40))
        self.save_btn.setMaximumSize(QSize(16777215, 40))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.save_btn.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.save_btn)


        self.horizontalLayout_8.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_7.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(GeneralsSelectionDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
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
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
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
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.frame_9)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.category_combobox = QComboBox(self.widget_7)
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.setObjectName(u"category_combobox")
        self.category_combobox.setMinimumSize(QSize(0, 40))
        self.category_combobox.setMaximumSize(QSize(160, 16777215))

        self.verticalLayout_14.addWidget(self.category_combobox)


        self.horizontalLayout_5.addWidget(self.widget_7)

        self.widget_4 = QWidget(self.frame_9)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.view__combobox = QComboBox(self.widget_4)
        self.view__combobox.addItem("")
        self.view__combobox.addItem("")
        self.view__combobox.setObjectName(u"view__combobox")
        self.view__combobox.setMinimumSize(QSize(0, 40))

        self.verticalLayout_11.addWidget(self.view__combobox)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.general_filter_widget = QWidget(self.frame_9)
        self.general_filter_widget.setObjectName(u"general_filter_widget")
        self.verticalLayout_12 = QVBoxLayout(self.general_filter_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.general_filter_widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)

        self.comboBox = QCheckComboBox(self.general_filter_widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(130, 40))

        self.verticalLayout_12.addWidget(self.comboBox)


        self.horizontalLayout_5.addWidget(self.general_filter_widget)

        self.widget_2 = QWidget(self.frame_9)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.swipe_attempts_spinbox = QSpinBox(self.widget_2)
        self.swipe_attempts_spinbox.setObjectName(u"swipe_attempts_spinbox")
        self.swipe_attempts_spinbox.setMinimumSize(QSize(110, 40))
        self.swipe_attempts_spinbox.setMaximumSize(QSize(100, 35))
        self.swipe_attempts_spinbox.setMaximum(20)
        self.swipe_attempts_spinbox.setValue(5)
        self.swipe_attempts_spinbox.setProperty(u"profile_id", 0)

        self.verticalLayout_9.addWidget(self.swipe_attempts_spinbox)


        self.horizontalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_16.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_3 = QFrame(GeneralsSelectionDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 11, 0)
        self.exit_btn = QPushButton(self.frame_3)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_3.addWidget(self.exit_btn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalLayout.setStretch(1, 15)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(GeneralsSelectionDialog)

        self.tabWidget.setCurrentIndex(0)
        self.category_combobox.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(GeneralsSelectionDialog)
    # setupUi

    def retranslateUi(self, GeneralsSelectionDialog):
        GeneralsSelectionDialog.setWindowTitle(QCoreApplication.translate("GeneralsSelectionDialog", u"Manage General Presets", None))
        self.groupBox.setTitle(QCoreApplication.translate("GeneralsSelectionDialog", u"Manage Preset", None))
        self.preset_combobox.setItemText(0, QCoreApplication.translate("GeneralsSelectionDialog", u"Default", None))

        self.preset_combobox.setPlaceholderText(QCoreApplication.translate("GeneralsSelectionDialog", u"Select Preset", None))
        self.edit_btn.setText("")
        self.delete_btn.setText("")
        self.add_btn.setText("")
        self.save_btn.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"  Save Preset", None))
        self.label_2.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"All Generals", None))
        self.all_generals_main.setProperty(u"item_info", "")
        self.label_3.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Selected Generals (Main Generals)", None))
        self.selected_generals_main.setProperty(u"item_info", "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("GeneralsSelectionDialog", u"Main General", None))
        self.label_4.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"All Generals", None))
        self.all_generals_assistant.setProperty(u"item_info", "")
        self.label_5.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Selected Generals (Assistant Generals)", None))
        self.selected_generals_assistant.setProperty(u"item_info", "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("GeneralsSelectionDialog", u"Assistant General", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("GeneralsSelectionDialog", u"Filter Settings", None))
        self.label_9.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"General Category", None))
        self.category_combobox.setItemText(0, QCoreApplication.translate("GeneralsSelectionDialog", u"All", None))
        self.category_combobox.setItemText(1, QCoreApplication.translate("GeneralsSelectionDialog", u"Military", None))
        self.category_combobox.setItemText(2, QCoreApplication.translate("GeneralsSelectionDialog", u"Development", None))
        self.category_combobox.setItemText(3, QCoreApplication.translate("GeneralsSelectionDialog", u"Duty", None))
        self.category_combobox.setItemText(4, QCoreApplication.translate("GeneralsSelectionDialog", u"Subordinate City", None))

        self.category_combobox.setPlaceholderText(QCoreApplication.translate("GeneralsSelectionDialog", u"Select Category", None))
        self.label_7.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"General View", None))
        self.view__combobox.setItemText(0, QCoreApplication.translate("GeneralsSelectionDialog", u"Details View", None))
        self.view__combobox.setItemText(1, QCoreApplication.translate("GeneralsSelectionDialog", u"List View", None))

        self.view__combobox.setPlaceholderText(QCoreApplication.translate("GeneralsSelectionDialog", u"Select View", None))
        self.label_8.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"General Filter", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("GeneralsSelectionDialog", u"Favorite", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("GeneralsSelectionDialog", u"Idle", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("GeneralsSelectionDialog", u"None", None))
        self.label_6.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Swipe Attempts", None))
        self.swipe_attempts_spinbox.setSuffix(QCoreApplication.translate("GeneralsSelectionDialog", u" Times", None))
        self.exit_btn.setText(QCoreApplication.translate("GeneralsSelectionDialog", u"Exit", None))
    # retranslateUi

