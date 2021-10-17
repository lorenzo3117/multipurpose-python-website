# Imports
from flask import Flask, render_template, flash, redirect, url_for
from forms import ProjectForm
from Project import Project
from ProjectsDB import ProjectsDB

# Variables
app = Flask(__name__)
app.config['SECRET_KEY'] = "whyisthisevenneeded"

project1 = Project("3D Computer Graphics", "Implementing a raytracer", "https://github.com/ucll-3dcg-2122/raytracer-de-maboetoe-s", "2021-12-26")
project2 = Project("Distributed Applications", "Making an auction website in Elixir", "https://github.com/distributed-applications/assignment-jan-lorenzo", "2021-12-08")
project3 = Project("Mobile Applications", "Making a simple game with Unity", "https://github.com/ucll-ma2021/mobileproject-alt-gr", "2021-12-23")
project4 = Project("Systeembeheer", "My systeembeheer course", "https://github.com/lorenzo3117/systeembeheer", "2021-12-10")

projectsDB = ProjectsDB()
projectsDB.add_project(project1)
projectsDB.add_project(project2)
projectsDB.add_project(project3)
projectsDB.add_project(project4)

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html", projects=projectsDB.get_projects())

@app.route("/projects/new", methods=["GET", "POST"])
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        new_project = Project(form.name.data, form.description.data, form.github_repo.data, form.deadline.data)
        projectsDB.add_project(new_project)
        flash("Project added", "success")
        return redirect(url_for("projects"))
    
    return render_template("project_form.html", form=form)

@app.route("/projects/<int:project_id>/delete", methods=["GET", "POST"])
def delete_project(project_id):
    projectsDB.remove_project(project_id)
    return redirect(url_for("projects"))

# Start
if __name__ == "__main__":
    app.run(debug=True)