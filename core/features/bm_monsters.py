import os
import shutil
import time
import zipfile

import yaml
from PySide6.QtWidgets import QMessageBox, QFileDialog
from sqlalchemy import asc
from sqlalchemy.orm import joinedload

from config.settings import BASE_DIR
from db.db_setup import get_session
from db.models import BossMonster, MonsterImage, MonsterCategory, MonsterLogic

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


def copy_image_to_export(images_folder, image_name, image_type):
    """Copy the image to the export folder."""
    if image_type == "preview":
        base_folder = os.path.join(BASE_DIR, 'assets', 'preview')
    else:
        base_folder = os.path.join(BASE_DIR, 'assets', '540p')
    image_path = os.path.join(base_folder, image_name)

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