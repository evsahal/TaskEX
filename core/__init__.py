import os
import ctypes

from sqlalchemy.exc import NoResultFound

from db.db_setup import get_session
from db.models import ScreenConfig
from utils.helper_utils import get_screen_resolution


def set_approximate_dpi():
    # Get the real screen resolution
    screen_resolution = get_screen_resolution()
    session = get_session()
    try:
        # Check if the resolution exists in the database
        screen_config = session.query(ScreenConfig).filter_by(screen_resolution=screen_resolution).one()
        dpi = screen_config.dpi
        # print(f"Found DPI for resolution {screen_resolution}: {dpi}")
    except NoResultFound:
        # If no match is found, insert the new resolution with default DPI(96)
        # print(f"No entry found for resolution {screen_resolution}. Creating new entry with DPI {dpi}.")
        new_config = ScreenConfig(screen_resolution=screen_resolution)
        session.add(new_config)
        session.commit()
        dpi = new_config.dpi
    finally:
        session.close()
        # Set QT_FONT_DPI environment variable
        os.environ["QT_FONT_DPI"] = str(dpi)



# Call the function to set DPI before creating QApplication
set_approximate_dpi()
