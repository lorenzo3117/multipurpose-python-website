class ProjectsDB:
    projects = {}

    def get_projects(self):
        return self.projects.values()

    def add_project(self, project):
        new_id = list(self.projects)[-1] + 1 if len(self.projects.keys()) != 0 else 1
        project.set_id(new_id)
        self.projects[new_id] = project

    def remove_project(self, project_id):
        if project_id in self.projects.keys():
            del self.projects[project_id]
            return True
        else:
            return False