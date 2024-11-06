import os
import shutil
import time
import zipfile

import cv2
import numpy as np
import yaml
from PySide6.QtWidgets import QMessageBox, QFileDialog, QVBoxLayout, QWidget, QLabel
from sqlalchemy import asc
from sqlalchemy.orm import joinedload

from core.custom_widgets.SelectionTool import SelectionTool
from db.db_setup import get_session
from db.models import BossMonster, MonsterImage, MonsterCategory, MonsterLogic, MonsterLevel
from utils.helper_utils import copy_image_to_template, copy_image_to_preview
from utils.image_recognition_utils import template_match_coordinates


def get_all_boss_monster_data():
    # Get all the bosses
    session = get_session()

    # Eagerly load the related MonsterImage, MonsterCategory, and MonsterLogic using joinedload
    sorted_logic_1_with_category_1 = (
        session.query(BossMonster)
        .join(MonsterImage)
        .join(MonsterCategory)
        .join(MonsterLogic)
        .options(
            joinedload(BossMonster.monster_image),  # Eagerly load monster_image
            joinedload(BossMonster.monster_category),  # Eagerly load monster_category
            joinedload(BossMonster.monster_logic)  # Eagerly load monster_logic
        )
        .filter(BossMonster.monster_logic_id == 1, BossMonster.monster_category_id == 1)
        .order_by(BossMonster.id)  # Sort by ID
        .all()
    )

    sorted_logic_1_except_category_1_and_logic_2_3_4 = (
        session.query(BossMonster)
        .join(MonsterImage)
        .join(MonsterCategory)
        .join(MonsterLogic)
        .options(
            joinedload(BossMonster.monster_image),  # Eagerly load monster_image
            joinedload(BossMonster.monster_category),  # Eagerly load monster_category
            joinedload(BossMonster.monster_logic)  # Eagerly load monster_logic
        )
        .filter(
            BossMonster.monster_logic_id.in_([1, 2, 3, 4]),
            ~BossMonster.id.in_([boss.id for boss in sorted_logic_1_with_category_1])
        )
        .order_by(asc(BossMonster.preview_name))  # Sort by preview_name
        .all()
    )

    # Combine the results
    boss_monsters = sorted_logic_1_with_category_1 + sorted_logic_1_except_category_1_and_logic_2_3_4

    session.close()
    return boss_monsters


def export_selected_bosses(boss_ids):
    session = get_session()
    export_data = []

    # Directory to store the export data
    export_folder = QFileDialog.getExistingDirectory(None, "Select Export Folder")
    if not export_folder:
        return  # User canceled the operation

    # Temporary folder for staging files before zipping
    temp_export_folder = os.path.join(export_folder, "export_temp")
    os.makedirs(temp_export_folder, exist_ok=True)

    # Create an images folder to store the images
    images_folder = os.path.join(temp_export_folder, "images")
    os.makedirs(images_folder, exist_ok=True)

    # Loop through each selected boss id
    for boss_id in boss_ids:
        boss = (
            session.query(BossMonster)
            .options(
                joinedload(BossMonster.monster_category),
                joinedload(BossMonster.monster_image),
                joinedload(BossMonster.monster_logic),
                joinedload(BossMonster.levels)
            )
            .filter(BossMonster.id == boss_id)
            .one_or_none()
        )

        if boss:
            # Collect data for YAML
            boss_data = {
                "preview_name": boss.preview_name,
                "category": boss.monster_category.name,
                "logic": boss.monster_logic.logic,
                "enable_map_scan": boss.enable_map_scan,
                "levels": [{"level": lvl.level, "name": lvl.name, "power": lvl.power} for lvl in boss.levels]
            }

            if boss.monster_image:
                image_data = {"preview_image": boss.monster_image.preview_image}

                if boss.enable_map_scan:
                    # Include these fields only when enable_map_scan is True
                    if boss.monster_image.img_540p:
                        image_data["img_540p"] = boss.monster_image.img_540p
                    if boss.monster_image.img_threshold:
                        image_data["img_threshold"] = boss.monster_image.img_threshold
                    if boss.monster_image.click_pos:
                        image_data["click_pos"] = boss.monster_image.click_pos

                boss_data["image"] = image_data

                # Copy images if they exist
                copy_image_to_export(images_folder, boss.monster_image.preview_image, "preview")
                if boss.enable_map_scan and boss.monster_image.img_540p:
                    copy_image_to_export(images_folder, boss.monster_image.img_540p, "540p")

            export_data.append(boss_data)

    # Create the YAML file
    yaml_file_path = os.path.join(temp_export_folder, "boss_monsters.yaml")
    with open(yaml_file_path, "w") as yaml_file:
        yaml.dump(export_data, yaml_file, default_flow_style=False)

    # Zip everything
    # Get current time in milliseconds
    current_time_ms = int(time.time() * 1000)

    # Generate zip file name with datetime in milliseconds
    zip_file_name = f"boss_monsters_{current_time_ms}.zip"
    zip_file_path = os.path.join(export_folder, zip_file_name)

    zip_export_files(temp_export_folder, zip_file_path)

    # Clean up temporary export folder
    shutil.rmtree(temp_export_folder)

    # Confirmation message
    QMessageBox.information(None, "Export Successful", f"File saved to: {zip_file_path}")

    session.close()


def create_monster_from_zip_data(data, temp_extract_folder):
    """Create a BossMonster object from YAML data."""
    session = get_session()

    monster = BossMonster(
        preview_name=data["preview_name"],
        enable_map_scan=data.get("enable_map_scan", False)
    )

    # Set category and logic
    category = session.query(MonsterCategory).filter_by(name=data["category"]).one_or_none()
    logic = session.query(MonsterLogic).filter_by(logic=data["logic"]).one_or_none()
    if category:
        monster.monster_category_id = category.id
    if logic:
        monster.monster_logic_id = logic.id

    # Handle images
    if "image" in data:
        monster_image = MonsterImage(
            preview_image=data["image"].get("preview_image"),
            img_540p=data["image"].get("img_540p"),
            img_threshold=data["image"].get("img_threshold"),
            click_pos=data["image"].get("click_pos")
        )
        monster.monster_image = monster_image

        # Store image path for later use
        monster.preview_img_path = os.path.join(temp_extract_folder, "images", monster.monster_image.preview_image)
        monster.p540_img_path = os.path.join(temp_extract_folder, "images",
                                             monster.monster_image.img_540p) if monster.monster_image.img_540p else None

    # Add levels
    for level_data in data.get("levels", []):
        level = MonsterLevel(
            level=level_data["level"],
            name=level_data["name"],
            power=level_data["power"]
        )
        monster.levels.append(level)

    session.close()
    return monster


def copy_image_to_export(images_folder, image_name, image_type):
    """Copy the image to the export folder."""
    if image_type == "preview":
        base_folder = os.path.join('assets', 'preview')
    else:
        base_folder = os.path.join('assets', '540p', 'monsters')
    image_path = os.path.join(base_folder, image_name)
    print(image_path)

    if os.path.exists(image_path):
        dest_image_path = os.path.join(images_folder, f"{image_name}")
        shutil.copy(image_path, dest_image_path)


def zip_export_files(folder_to_zip, output_zip_path):
    """Zip the exported folder into a zip file."""
    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_to_zip):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_to_zip)
                zip_file.write(file_path, arcname)


def generate_monster_template(captured_images):
    """Generate a template from captured images and calculate a single scalar threshold."""
    try:
        # Stack the images along the first axis (n_images, height, width, channels)
        image_stack = np.stack(captured_images, axis=0)

        # Generate the median template image to reduce noise
        template = np.median(image_stack, axis=0).astype(np.uint8)

        # Convert the template to grayscale (required for thresholding)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Use Otsu's thresholding to calculate a single scalar threshold
        _, threshold_image = cv2.threshold(template_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Calculate the average value of the threshold image as a scalar threshold (normalized to [0, 1])
        scalar_threshold = np.mean(threshold_image) / 255.0

        print(f"[INFO] Calculated scalar threshold: {scalar_threshold}")

        return template, scalar_threshold

    except Exception as e:
        print(f"[ERROR] Failed to generate template: {e}")
        return None, None


def find_optimal_threshold(image):
    """Find the best threshold by analyzing the image histogram."""
    try:
        # Compute histogram of pixel intensities
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])

        # Normalize the histogram to [0, 1] range
        hist = hist / np.sum(hist)

        # Use Otsu's method to find the optimal threshold
        _, threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return threshold / 255.0  # Normalize to [0, 1] range

    except Exception as e:
        print(f"[ERROR] Failed to find optimal threshold: {e}")
        return 0.5  # Default threshold in case of error


def start_simulate_monster_click(thread):
    try:
        # Get the threshold value
        threshold = thread.ref.threshold_spin_box.value()
        # Get the file_path
        file_path = thread.ref.p540_image_line_edit.property('file_path')

        # Capture the emulator image
        src_img = thread.adb_manager.take_screenshot()
        template_img = cv2.imread(file_path)

        cords = template_match_coordinates(src_img, template_img, convert_gray=False, threshold=threshold)
        if cords:
            x = thread.ref.click_x_spin_box.value() + cords[0]
            y = thread.ref.click_y_spin_box.value() + cords[1]
            thread.adb_manager.tap(x, y)

    except Exception as e:
        print(f"[ERROR] Failed to simulate the click: {e}")
