from datetime import datetime
from time import time
from subtask import Subtask

class Task:
    def __init__(self, task):
        self.task = task
        self.subtasks = []
        self.creation_date = datetime.now()
        self.duration = 0
        self.start_date = None
        self.close_date = None
        self.start_time = None


    def add_subtask(self, subtask):
        subtask_obj = Subtask(subtask)
        if len(self.subtasks) < 5:
            self.subtasks.append(subtask_obj)

    def start_task(self):
        self.start_date = datetime.now()

    def close_task(self):
        self.close_date = datetime.now()

    def log_in(self):
        self.start_time = time()

    def log_out(self):
        self.duration += round((time() - self.start_time) / 60)
        self.start_time = None