class ProjectsDB:
    projects = []

    def get_projects(self):
        return self.projects

    def add_project(self, project):
        new_id = len(self.projects) + 1
        project.set_id(new_id)
        self.projects.append(project)