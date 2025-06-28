import json

from PySide6.QtCore import QRunnable, Signal, QObject

from db.db_setup import get_session
from db.models import ProfileData


class ProfileLoadWorkerSignals(QObject):
    profile_loaded = Signal(dict)
    error = Signal(str)

    def __init__(self):
        super().__init__()

class ProfileLoadWorker(QRunnable):
    """
    Worker for loading profile data using QThreadPool.
    """
    def __init__(self, profile_id):
        super().__init__()
        self.profile_id = profile_id
        self.signals = ProfileLoadWorkerSignals()

    def run(self):
        """
        Perform the database fetch operation.
        """
        with get_session() as session:
            try:
                profile_data = session.query(ProfileData).filter_by(profile_id=self.profile_id).first()
                # Parse the JSON settings or return an empty dict if no data
                settings = json.loads(profile_data.settings) if profile_data else {}
                # Emit the signal with the loaded data
                # print(f"Emitting profile_loaded signal with settings: {settings}")
                self.signals.profile_loaded.emit(settings)
            except Exception as e:
                error_message = f"Error loading profile data: {e}"
                print(error_message)
                self.signals.error.emit(error_message)
