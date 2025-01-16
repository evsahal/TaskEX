from utils.get_controls_info import get_join_rally_controls


def run_join_rally(thread):
    controls = get_join_rally_controls(thread.main_window, thread.index)
    # print(controls)

    count = 0
    while thread._running:
        thread.capture_and_validate_screen()
        try:
            if thread.index == 1:
                thread.adb_manager.swipe(100, 300, 500, 300)
            else:
                thread.adb_manager.swipe(250, 100, 250, 700)

            count += 1
            if count > 20:
                break
        except Exception as e:
            thread.logger.error(f"Error during emulator operation: {e}")
            break