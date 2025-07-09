from PySide6.QtWidgets import QStackedWidget, QFrame, QPushButton

from config.settings import VERSION, TESTED_ON


def init_home_ui(main_window):

    # Init About and Donation UI
    init_about_donation_ui(main_window)

def init_about_donation_ui(main_window):
    ui = main_window.widgets

    stacked_widget: QStackedWidget = ui.stacked_widget_about_donation
    donate_now_btn: QPushButton = ui.donate_now_btn
    about_frame_page: QFrame = ui.about_frame_page
    donation_frame_page: QFrame = ui.donation_frame_page

    ui.about_version_label.setText(VERSION)
    ui.about_tested_on_label.setText(TESTED_ON)

    def toggle_about_and_donation_frame(checked):
        if checked:
            stacked_widget.setCurrentWidget(donation_frame_page)
        else:
            stacked_widget.setCurrentWidget(about_frame_page)

    def about_and_donation_enter_event(event):
        if not donate_now_btn.isChecked():
            stacked_widget.setCurrentWidget(donation_frame_page)

    def about_and_donation_leave_event(event):
        if not donate_now_btn.isChecked():
            stacked_widget.setCurrentWidget(about_frame_page)

    donate_now_btn.toggled.connect(toggle_about_and_donation_frame)
    donate_now_btn.enterEvent = about_and_donation_enter_event
    donate_now_btn.leaveEvent = about_and_donation_leave_event
