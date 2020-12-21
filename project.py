from datetime import datetime
from time import time
from task import Task

class Project:
    def __init__(self, project):
        self.project = project
        self.tasks = []
        self.creation_date = datetime.now()
        self.duration = 0
        self.start_date = None
        self.close_date = None
        self.start_time = None

    def add_task(self, task):
        task_object = Task(task)
        if len(self.tasks) < 25:
            self.tasks.append(task_object)

    def start_project(self):
        self.start_date = datetime.now()

    def close_project(self):
        self.close_date = datetime.now()

    def log_in(self):
        self.start_time = time()

    def log_out(self):
        self.duration += round((time() - self.start_time) / 60)
        self.start_time = None