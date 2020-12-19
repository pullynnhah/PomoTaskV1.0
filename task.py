class Task:
    def __init__(self, project=None):
        if project is None:
            self.project = self.create_project()
        else:
            self.project = project
        self.create_task(project)

    def create_project(self):
        project = Project()
