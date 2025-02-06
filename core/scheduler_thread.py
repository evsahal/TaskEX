import datetime
import time
from contextlib import contextmanager
from PySide6.QtCore import Signal, QThread
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import Integer, Column, DateTime, Boolean, String
from db.db_setup import Base, get_session


class SchedulerThread(QThread):
    task_triggered = Signal(str)  # Signal for task execution

    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks
        self.scheduler = BackgroundScheduler()

    def run(self):
        with get_session() as session:
            for task in self.tasks:

                # Check if the task is enabled
                task_status = session.query(TaskStatus).filter_by(name=task.name).first()
                if task_status and not task_status.enabled:
                    continue  # Skip the task if it is not enabled.

                if task.schedule_type == "cron":
                    start_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    end_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

                    self.scheduler.add_job(
                        self.execute_task,
                        'cron',
                        args=[task.name],
                        hour=task.cron_expression.split()[0],
                        minute=task.cron_expression.split()[1],
                        start_date=start_date,
                        end_date=end_date,
                        id=f"{task.name}_cron",
                    )

                elif task.schedule_type == "interval":
                    last_run = task_status.last_run if task_status else None
                    try:
                        next_run_time = last_run + datetime.timedelta(
                            **task.interval) if last_run else datetime.datetime.now()
                    except TypeError as e:
                        print(f"Invalid interval configuration: {e}")
                        next_run_time = datetime.datetime.now()

                    self.scheduler.add_job(
                        self.execute_task, 'interval', args=[task.name], **task.interval,
                        next_run_time=next_run_time if next_run_time > datetime.datetime.now() else None,
                        id=f"{task.name}_interval"
                    )

            self.scheduler.start()

            try:
                while True:
                    time.sleep(1)  # Keep the scheduler thread alive
            except (KeyboardInterrupt, SystemExit):
                pass  # Allow clean exit

    def execute_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                with session_scope() as session:
                    try:
                        task.run(session)  # Pass the session to the task's run method
                        self.task_triggered.emit(task_name)
                    except Exception as e:  # Handle potential exceptions
                        print(f"Error executing task '{task_name}': {e}")


@contextmanager
def session_scope():
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Session error: {e}")
    finally:
        session.close()


class SchedulerTask:
    def __init__(self, name, schedule_type, **kwargs):
        self.name = name
        self.schedule_type = schedule_type
        self.kwargs = kwargs  # Store scheduling parameters

        # Default values for start and end times
        self.start_time = kwargs.get("start_time", "0:00")
        self.end_time = kwargs.get("end_time", "23:59")

    def run(self, session):
        print(f"Running task: {self.name}")


class TaskStatus(Base):
    __tablename__ = 'task_status'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    enabled = Column(Boolean, default=True)
    last_run = Column(DateTime)