# Imports
from flask import Flask, render_template, flash, redirect, url_for, request
from werkzeug.datastructures import RequestCacheControl
from forms import ProjectForm, PasswordForm
from Project import Project
from ProjectsDB import ProjectsDB
from password_generator import generate_password
from file_information import gather_file_information

# Variables
app = Flask(__name__)
app.config['SECRET_KEY'] = "whyisthisevenneeded"

PROJECTSDB = ProjectsDB()

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects/projects.html", projects=PROJECTSDB.get_projects())

@app.route("/projects/new", methods=["GET", "POST"])
def create_project():
    form = ProjectForm()

    if form.validate_on_submit():
        new_project = Project(form.name.data, form.description.data, form.github_repo.data, form.deadline.data)
        PROJECTSDB.add_project(new_project)
        flash("Your project has successfully been added!", "success")
        return redirect(url_for("projects"))
    
    return render_template("projects/project_form.html", form=form)

@app.route("/projects/<int:project_id>/delete", methods=["GET", "POST"])
def delete_project(project_id):
    if PROJECTSDB.remove_project(project_id):
        flash("Your project has successfully been removed!", "success")
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

@app.route("/file_information", methods=["GET", "POST"])
def file_information():
    fileInformation = None
    clear = False

    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.content_type != "text/plain":
            flash("Please upload only .txt files!", "danger")
        else:
            flash("File successfully parsed!", "success")
            fileInformation = gather_file_information(file)
            clear = True

    return render_template("file_information/file_information.html", fileInformation=fileInformation, clear=clear)

# Start
if __name__ == "__main__":
    app.run(debug=True)