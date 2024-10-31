# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monster_edit_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Monster_Edit_Dialog(object):
    def setupUi(self, Monster_Edit_Dialog):
        if not Monster_Edit_Dialog.objectName():
            Monster_Edit_Dialog.setObjectName(u"Monster_Edit_Dialog")
        Monster_Edit_Dialog.resize(710, 714)
        self.verticalLayout = QVBoxLayout(Monster_Edit_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Monster_Edit_Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.category_combo_box = QComboBox(self.frame_8)
        self.category_combo_box.setObjectName(u"category_combo_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.category_combo_box.sizePolicy().hasHeightForWidth())
        self.category_combo_box.setSizePolicy(sizePolicy1)
        self.category_combo_box.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.category_combo_box, 1, 0, 1, 1)

        self.logic_combo_box = QComboBox(self.frame_8)
        self.logic_combo_box.setObjectName(u"logic_combo_box")
        sizePolicy1.setHeightForWidth(self.logic_combo_box.sizePolicy().hasHeightForWidth())
        self.logic_combo_box.setSizePolicy(sizePolicy1)
        self.logic_combo_box.setMinimumSize(QSize(110, 40))

        self.gridLayout.addWidget(self.logic_combo_box, 1, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.preview_name_line_edit = QLineEdit(self.frame_9)
        self.preview_name_line_edit.setObjectName(u"preview_name_line_edit")
        self.preview_name_line_edit.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_12.addWidget(self.preview_name_line_edit)

        self.map_scan_checkbox = QCheckBox(self.frame_9)
        self.map_scan_checkbox.setObjectName(u"map_scan_checkbox")

        self.horizontalLayout_12.addWidget(self.map_scan_checkbox, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.frame_9, 0, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignTop)

        self.groupBox_2 = QGroupBox(self.frame_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_10 = QFrame(self.groupBox_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.browse_preview_btn = QPushButton(self.frame_10)
        self.browse_preview_btn.setObjectName(u"browse_preview_btn")
        self.browse_preview_btn.setMinimumSize(QSize(40, 40))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.browse_preview_btn.setIcon(icon)

        self.gridLayout_2.addWidget(self.browse_preview_btn, 0, 4, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.click_x_spin_box = QSpinBox(self.frame_13)
        self.click_x_spin_box.setObjectName(u"click_x_spin_box")
        self.click_x_spin_box.setEnabled(False)
        self.click_x_spin_box.setMinimumSize(QSize(100, 40))
        self.click_x_spin_box.setMaximumSize(QSize(16777215, 16777215))
        self.click_x_spin_box.setMinimum(-50)
        self.click_x_spin_box.setMaximum(50)

        self.horizontalLayout_4.addWidget(self.click_x_spin_box)

        self.click_y_spin_box = QSpinBox(self.frame_13)
        self.click_y_spin_box.setObjectName(u"click_y_spin_box")
        self.click_y_spin_box.setEnabled(False)
        self.click_y_spin_box.setMinimumSize(QSize(100, 40))
        self.click_y_spin_box.setMaximumSize(QSize(16777215, 16777215))
        self.click_y_spin_box.setMinimum(-50)
        self.click_y_spin_box.setMaximum(50)

        self.horizontalLayout_4.addWidget(self.click_y_spin_box)

        self.simulate_click_btn = QPushButton(self.frame_13)
        self.simulate_click_btn.setObjectName(u"simulate_click_btn")
        self.simulate_click_btn.setEnabled(False)
        self.simulate_click_btn.setMinimumSize(QSize(40, 40))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaRecord))
        self.simulate_click_btn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.simulate_click_btn)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_7.addWidget(self.frame_13)


        self.gridLayout_2.addWidget(self.frame_11, 5, 0, 1, 5)

        self.preview_image_line_edit = QLineEdit(self.frame_10)
        self.preview_image_line_edit.setObjectName(u"preview_image_line_edit")
        self.preview_image_line_edit.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.preview_image_line_edit, 0, 0, 1, 4)

        self.find_template_btn = QPushButton(self.frame_10)
        self.find_template_btn.setObjectName(u"find_template_btn")
        self.find_template_btn.setEnabled(False)
        self.find_template_btn.setMinimumSize(QSize(40, 40))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemSearch))
        self.find_template_btn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.find_template_btn, 1, 4, 1, 1)

        self.browse_540p_btn = QPushButton(self.frame_10)
        self.browse_540p_btn.setObjectName(u"browse_540p_btn")
        self.browse_540p_btn.setEnabled(False)
        self.browse_540p_btn.setMinimumSize(QSize(40, 40))
        self.browse_540p_btn.setIcon(icon)

        self.gridLayout_2.addWidget(self.browse_540p_btn, 1, 3, 1, 1)

        self.p540_image_line_edit = QLineEdit(self.frame_10)
        self.p540_image_line_edit.setObjectName(u"p540_image_line_edit")
        self.p540_image_line_edit.setEnabled(False)
        self.p540_image_line_edit.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.p540_image_line_edit, 1, 0, 1, 3)

        self.threshold_spin_box = QDoubleSpinBox(self.frame_10)
        self.threshold_spin_box.setObjectName(u"threshold_spin_box")
        self.threshold_spin_box.setEnabled(False)
        self.threshold_spin_box.setMinimumSize(QSize(0, 40))
        self.threshold_spin_box.setMinimum(0.000000000000000)
        self.threshold_spin_box.setMaximum(0.990000000000000)
        self.threshold_spin_box.setSingleStep(0.010000000000000)
        self.threshold_spin_box.setValue(0.800000000000000)

        self.gridLayout_2.addWidget(self.threshold_spin_box, 3, 0, 1, 3)


        self.horizontalLayout_6.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.groupBox_2, 0, Qt.AlignmentFlag.AlignTop)

        self.groupBox_3 = QGroupBox(self.frame_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.groupBox_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(160, 0))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 0)
        self.port_lineEdit = QLineEdit(self.frame_5)
        self.port_lineEdit.setObjectName(u"port_lineEdit")
        self.port_lineEdit.setEnabled(False)
        self.port_lineEdit.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_8.addWidget(self.port_lineEdit)

        self.capture_image_btn = QPushButton(self.frame_5)
        self.capture_image_btn.setObjectName(u"capture_image_btn")
        self.capture_image_btn.setEnabled(False)
        self.capture_image_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_8.addWidget(self.capture_image_btn)

        self.lock_btn = QPushButton(self.frame_5)
        self.lock_btn.setObjectName(u"lock_btn")
        self.lock_btn.setEnabled(False)
        self.lock_btn.setMinimumSize(QSize(40, 40))
        self.lock_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.lock_btn)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.template_selection_frame = QFrame(self.groupBox_3)
        self.template_selection_frame.setObjectName(u"template_selection_frame")
        sizePolicy.setHeightForWidth(self.template_selection_frame.sizePolicy().hasHeightForWidth())
        self.template_selection_frame.setSizePolicy(sizePolicy)
        self.template_selection_frame.setStyleSheet(u"")
        self.template_selection_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.template_selection_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.template_selection_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.template_selection_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 263, 682))
        sizePolicy.setHeightForWidth(self.scrollAreaContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaContents.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaContents)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.configure_label = QLabel(self.scrollAreaContents)
        self.configure_label.setObjectName(u"configure_label")
        self.configure_label.setTextFormat(Qt.TextFormat.RichText)
        self.configure_label.setScaledContents(True)
        self.configure_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.configure_label.setWordWrap(True)
        self.configure_label.setMargin(0)

        self.horizontalLayout_5.addWidget(self.configure_label)

        self.scrollArea.setWidget(self.scrollAreaContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.template_selection_frame)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.horizontalLayout_9.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.frame_14)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.groupBox_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(7, 7, 0, 7)
        self.add_level_btn = QPushButton(self.frame_4)
        self.add_level_btn.setObjectName(u"add_level_btn")
        self.add_level_btn.setMinimumSize(QSize(110, 40))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_level_btn.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.add_level_btn, 0, Qt.AlignmentFlag.AlignLeft)

        self.smart_mode_check_box = QCheckBox(self.frame_4)
        self.smart_mode_check_box.setObjectName(u"smart_mode_check_box")

        self.horizontalLayout_10.addWidget(self.smart_mode_check_box, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.level_frame = QFrame(self.groupBox_4)
        self.level_frame.setObjectName(u"level_frame")
        sizePolicy.setHeightForWidth(self.level_frame.sizePolicy().hasHeightForWidth())
        self.level_frame.setSizePolicy(sizePolicy)
        self.level_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.level_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.level_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.level_scrollArea = QScrollArea(self.level_frame)
        self.level_scrollArea.setObjectName(u"level_scrollArea")
        self.level_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 339, 508))
        self.level_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_11.addWidget(self.level_scrollArea)


        self.verticalLayout_5.addWidget(self.level_frame)


        self.verticalLayout_4.addWidget(self.groupBox_4)


        self.horizontalLayout_2.addWidget(self.frame_14)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 6)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Monster_Edit_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(110, 45))

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.save_changes_btn = QPushButton(self.frame_2)
        self.save_changes_btn.setObjectName(u"save_changes_btn")
        self.save_changes_btn.setMinimumSize(QSize(150, 45))

        self.horizontalLayout.addWidget(self.save_changes_btn)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Monster_Edit_Dialog)

        QMetaObject.connectSlotsByName(Monster_Edit_Dialog)
    # setupUi

    def retranslateUi(self, Monster_Edit_Dialog):
        Monster_Edit_Dialog.setWindowTitle(QCoreApplication.translate("Monster_Edit_Dialog", u"Monster Details", None))
        self.groupBox.setTitle(QCoreApplication.translate("Monster_Edit_Dialog", u"Basic Info", None))
        self.category_combo_box.setPlaceholderText(QCoreApplication.translate("Monster_Edit_Dialog", u"Category", None))
        self.logic_combo_box.setPlaceholderText(QCoreApplication.translate("Monster_Edit_Dialog", u"Logic", None))
        self.preview_name_line_edit.setPlaceholderText(QCoreApplication.translate("Monster_Edit_Dialog", u"Preview Name", None))
        self.map_scan_checkbox.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"Map Scan", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Monster_Edit_Dialog", u"Image Info", None))
        self.browse_preview_btn.setText("")
        self.click_x_spin_box.setSuffix("")
        self.click_x_spin_box.setPrefix(QCoreApplication.translate("Monster_Edit_Dialog", u"Click X : ", None))
        self.click_y_spin_box.setPrefix(QCoreApplication.translate("Monster_Edit_Dialog", u"Click Y : ", None))
        self.simulate_click_btn.setText("")
        self.preview_image_line_edit.setPlaceholderText(QCoreApplication.translate("Monster_Edit_Dialog", u"Preview Image", None))
        self.find_template_btn.setText("")
        self.browse_540p_btn.setText("")
        self.p540_image_line_edit.setPlaceholderText(QCoreApplication.translate("Monster_Edit_Dialog", u"Image 540p", None))
        self.threshold_spin_box.setPrefix(QCoreApplication.translate("Monster_Edit_Dialog", u"Threshold: ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Monster_Edit_Dialog", u"Configure Template Area", None))
        self.port_lineEdit.setText("")
        self.port_lineEdit.setPlaceholderText(QCoreApplication.translate("Monster_Edit_Dialog", u"Port No.", None))
        self.capture_image_btn.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"Capture Image", None))
        self.lock_btn.setText("")
        self.configure_label.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Map Scan Template Configuration Guide</span><br/>- Enter the port number of the emulator for capturing the template image.<br/>- Navigate to the world map and ensure it is fully zoomed out.<br/>- Position the monster at the center of the map by either entering its coordinates manually or selecting it from bookmarks.<br/>- Click the &quot;Capture Image&quot; button to display the image for selecting the template area.<br/>- Mark the area around the monster where you want to apply the algorithm to generate the template image and the threshold.<br/>- Ensure the selected area contains only parts of the monster to improve matching accuracy (preferably static areas).<br/>- Lock the selected area by pressing the lock button.<br/>- Click the Magnifying Glass button next to the 540p image picker to generate the template and its threshold value.<br/>- Use the record button to adjust the click position for precise monster selection; modif"
                        "y the X and Y values if needed to fine-tune the click position.</p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Monster_Edit_Dialog", u"Level Info", None))
        self.add_level_btn.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"Add Level", None))
        self.smart_mode_check_box.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"Smart Mode", None))
        self.cancel_btn.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"Cancel", None))
        self.save_changes_btn.setText(QCoreApplication.translate("Monster_Edit_Dialog", u"Save Changes", None))
    # retranslateUi

