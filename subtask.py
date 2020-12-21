from datetime import datetime
from time import time

class Subtask:
    def __init__(self, subtask):
        self.subtask = subtask
        self.duration = 0
        self.start_time = None

    def log_in(self):
        self.start_time = time()

    def log_out(self):
        self.duration += round((time() - self.start_time) / 60)
        self.start_time = None
        