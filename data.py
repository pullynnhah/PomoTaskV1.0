import json


class ProjectData:
    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

    def update_project(self, new_data):
        data = self.get_data()
        data["Projects"].append(new_data)
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def get_projects(self):
        data = self.get_data()
        projects = data["Projects"]
        return projects

    def list_projects(self):
        return [project["Project"] for project in self.get_projects()]

    def find_project(self, project_name):
        projects = self.get_projects()
        projects_names = self.list_projects()

        for idx, project in enumerate(projects_names):
            if project_name == project:
                return projects[idx]

    def get_tasks(self, project_name):
        project = self.find_project(project_name)
        return [task for task in project["Tasks"]]

    def list_tasks(self, project_name):
        return [task["Task"] for task in self.get_tasks(project_name)]

    def find_task(self, project_name, task_name):
        tasks = self.get_tasks(project_name)
        tasks_names = self.list_tasks(project_name)
        for idx, task in enumerate(tasks_names):
            if task_name == task:
                return tasks[idx]

    def get_subtasks(self, project_name, task_name):
        task = self.find_task(project_name, task_name)
        return task["Subtasks"]

    def list_subtasks(self, project_name, task_name):
        return [task['Subtask'] for task in self.get_subtasks(project_name, task_name)]
