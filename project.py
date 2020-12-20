from datetime import datetime


class Project:
    def __init__(self, project):
        self.project = project
        self.tasks = []
        self.creation_date = datetime.now()
        self.start_date = None
        self.close_date = None

    def add_task(self, task):
        if len(self.tasks) <= 25:
            self.tasks.append(task)

    def start_project(self):
        self.start_date = datetime.now()

    def close_project(self):
        self.close_date = datetime.now()
