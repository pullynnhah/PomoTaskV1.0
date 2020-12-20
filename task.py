from datetime import datetime


class Task:
    def __init__(self, task):
        self.task = task
        self.subtasks = []
        self.creation_date = datetime.now()
        self.start_date = None
        self.close_date = None

    def add_subtask(self, subtask):
        if len(self.subtasks) <= 5:
            self.subtasks.append(subtask)

    def start_task(self):
        self.start_date = datetime.now()

    def close_task(self):
        self.close_date = datetime.now()
