class Project:
    def __init__(self, name, description, github_repo, deadline):
        self.name = name
        self.description = description
        self.github_repo = github_repo
        self.deadline = deadline

    def set_id(self, new_id):
        self.id = new_id