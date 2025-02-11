import datetime
import time
from contextlib import contextmanager
from PySide6.QtCore import Signal, QThread
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import Integer, Column, DateTime, Boolean, String
from db.db_setup import Base, get_session


class SchedulerThread(QThread):
    task_triggered = Signal(str)  # Signal for task execution

    def __init__(self, tasks, main_task):
        super().__init__()
        self.tasks = tasks
        self.main_task = main_task  # Store the main task function
        self.scheduler = BackgroundScheduler()

    def run(self):
        # Schedule other intermittent tasks
        self._schedule_intermittent_tasks()
        self.scheduler.start()

        try:
            while True:
                # Execute the main task continuously
                self.main_task_execution()
                time.sleep(0.1)  # Small sleep to reduce busy-waiting
        except (KeyboardInterrupt, SystemExit):
            self.scheduler.shutdown()

    def _schedule_intermittent_tasks(self):
        """Schedule intermittent tasks based on their configuration."""
        with get_session() as session:
            for task in self.tasks:
                task_status = session.query(TaskStatus).filter_by(name=task.name).first()
                if task_status and not task_status.enabled:
                    continue

                if task.schedule_type == "cron":
                    self.scheduler.add_job(
                        self.execute_task,
                        'cron',
                        args=[task.name],
                        hour=task.cron_expression.split()[0],
                        minute=task.cron_expression.split()[1],
                        id=f"{task.name}_cron",
                    )

                elif task.schedule_type == "interval":
                    self.scheduler.add_job(
                        self.execute_task, 'interval', args=[task.name], **task.interval,
                        id=f"{task.name}_interval"
                    )

    def main_task_execution(self):
        """Execute the main task while allowing scheduled tasks."""
        print("Executing main task...")
        self.main_task()  # Run the user-defined main task

    def execute_task(self, task_name):
        """Interrupt main task execution and perform a scheduled task."""
        for task in self.tasks:
            if task.name == task_name:
                print(f"Executing intermittent task: {task_name}")
                with session_scope() as session:
                    try:
                        task.run(session)  # Pass the session to the task's run method
                        self.task_triggered.emit(task_name)
                    except Exception as e:
                        print(f"Error executing task '{task_name}': {e}")


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
