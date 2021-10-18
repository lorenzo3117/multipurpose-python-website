# Imports
from flask import Flask, render_template, flash, redirect, url_for
from forms import ProjectForm, PasswordForm
from Project import Project
from ProjectsDB import ProjectsDB
from password_generator import generate_password

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
    return render_template("projects/projects.html", projects=projectsDB.get_projects())

@app.route("/projects/new", methods=["GET", "POST"])
def create_project():
    form = ProjectForm()

    if form.validate_on_submit():
        new_project = Project(form.name.data, form.description.data, form.github_repo.data, form.deadline.data)
        projectsDB.add_project(new_project)
        flash("Your project has successfully been added!", "succes")
        return redirect(url_for("projects"))
    
    return render_template("projects/project_form.html", form=form)

@app.route("/projects/<int:project_id>/delete", methods=["GET", "POST"])
def delete_project(project_id):
    if projectsDB.remove_project(project_id):
        flash("Your project has successfully been added!", "succes")
    else:
        flash("There has been an error removing your project!", "danger")

    return redirect(url_for("projects"))

@app.route("/password_generator", methods=["GET", "POST"])
def password_generator():
    form = PasswordForm()

    if form.validate_on_submit():
        print(form.lowerCase.data)
        password = generate_password(form.length.data, form.lowerCase.data, form.upperCase.data, form.numbers.data, form.specials.data)
        flash(f"Here's your generated password:<br><b>{password}</b>", "success")
        return render_template("password_generator/password_generator.html", form=PasswordForm())

    if form.is_submitted() and not form.validate():
        flash("At least one option has to be checked!", "danger")

    return render_template("password_generator/password_generator.html", form=form)

# Start
if __name__ == "__main__":
    app.run(debug=True)