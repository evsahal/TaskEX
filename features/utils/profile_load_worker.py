import json

from PySide6.QtCore import QRunnable, Signal, QObject

from db.db_setup import get_session
from db.models import ProfileData


class ProfileLoadWorker(QRunnable):
    """
    Worker for loading profile data using QThreadPool.
    """
    profile_loaded_signal = Signal(dict)

    def __init__(self, profile_id):
        super().__init__()
        self.profile_id = profile_id


    def run(self):
        """
        Perform the database fetch operation.
        """
        try:
            session = get_session()  # Assuming get_session is defined elsewhere
            profile_data = session.query(ProfileData).filter_by(profile_id=self.profile_id).first()
            session.close()
            # Parse the JSON settings or return an empty dict if no data
            settings = json.loads(profile_data.settings) if profile_data else {}
            # Emit the signal with the loaded data
            self.profile_loaded_signal.emit(settings)
        except Exception as e:
            error_message = f"Error loading profile data: {e}"
            print(error_message)
            self.profile_loaded_signal.emit(None)

