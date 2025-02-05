import datetime
import time

import cv2

from utils.get_controls_info import get_join_rally_controls
from utils.image_recognition_utils import is_template_match, draw_template_match
from utils.navigate_utils import navigate_join_rally_window


def run_join_rally(thread):
    # Get the controls and store it in the thread cache
    if 'join_rally_controls' not in thread.cache:
        thread.cache['join_rally_controls'] = get_join_rally_controls(thread.main_window, thread.index)
    # print(thread.cache['join_rally_controls']['settings']['join_oldest_rallies_first'])
    join_oldest_rallies_first = thread.cache['join_rally_controls']['settings']['join_oldest_rallies_first']
    # Set the rally joining position based on the oldest rallies checkbox value
    scroll_through_rallies(thread,join_oldest_rallies_first,5,True)
    # Switch the swipe direction after setting up the join_oldest_rallies_first option
    swipe_direction = False if join_oldest_rallies_first else True

    swipe_iteration  = 0
    max_swipe_iteration  = 0
    # Initialize the cache to store the skipped monster cords images
    thread.cache['join_rally_controls'].setdefault('cache', {}).setdefault('skipped_monster_cords_img', [])

    while thread.thread_status():
        try:
            # Process boss monster rallies
            process_monster_rallies(thread,join_oldest_rallies_first)
            print(
                f"Swipe Direction : {swipe_direction} :: iteration : {swipe_iteration} itr cap : {max_swipe_iteration}")
            time.sleep(1)

            # Swipe based on the direction
            scroll_through_rallies(thread, swipe_direction)

            # Update iterations
            swipe_iteration += 1
            max_swipe_iteration += 1

            # Switch direction if limit reached
            if swipe_iteration == 5:
                swipe_direction = not swipe_direction
                swipe_iteration = 0

            # Reset navigation after reaching max iteration
            if max_swipe_iteration >= 20:
                # Clear skipped cords images
                thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img'] = []
                # Press back
                thread.adb_manager.press_back()
                time.sleep(1)
                if not navigate_join_rally_window(thread):
                    break
                # Update the swipe to scroll down
                swipe_direction = True
                max_swipe_iteration = 0
        finally:
            # Clear skipped cords images
            thread.cache['join_rally_controls']['cache']['skipped_monster_cords_img'] = []

def process_monster_rallies(thread,scan_direction):
    pass



def scroll_through_rallies(thread,swipe_direction,swipe_limit=1,initial_swipe = False):
    """
    swipe_direction True = scroll down, False = scroll up
    """
    # Swipe coordinates based on direction
    swipe_cords = [250, 810, 250, 320] if swipe_direction else [250, 320, 250, 810]
    # Navigate to the alliance war window
    if not navigate_join_rally_window(thread):
        print("Cannot navigate to join rally window")
        return False
    # If the join oldest rally is not checked, then skip this.
    if initial_swipe and not swipe_direction:
        return True
    # Load the template image
    background_img = cv2.imread("assets/540p/join rally/alliance_war_window_background.png")
    for i in range(swipe_limit):
        # Check if there is any rallies to scroll through
        src_img = thread.capture_and_validate_screen(ads=False)
        if is_template_match(src_img, background_img,False, 0.95):
            # print("No more rallies in the list")
            # cv2.imwrite(r"E:\Projects\PyCharmProjects\TaskEX\temp\demo.png",draw_template_match(src_img, background_img,False, 0.95))
            break
        thread.adb_manager.swipe(*swipe_cords, 1500)
        time.sleep(1)
    return True


