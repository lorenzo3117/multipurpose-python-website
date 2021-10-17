# Imports
from Project import Project
from ProjectsDB import ProjectsDB
from flask import Flask, render_template

# Variables
app = Flask(__name__)

project1 = Project("3D Computer Graphics", "Implementing a raytracer", "https://github.com/ucll-3dcg-2122/raytracer-de-maboetoe-s", "26/12/2021")
project2 = Project("Distributed Applications", "Making an auction website in Elixir", "https://github.com/distributed-applications/assignment-jan-lorenzo", "08/12/2021")
project3 = Project("Mobile Applications", "Making a simple game with Unity", "https://github.com/ucll-ma2021/mobileproject-alt-gr", "23/12/2021")
project4 = Project("Systeembeheer", "My systeembeheer course", "https://github.com/lorenzo3117/systeembeheer", "10/12/2021")

projectsDB = ProjectsDB()
projectsDB.add_project(project1)
projectsDB.add_project(project2)
projectsDB.add_project(project3)
projectsDB.add_project(project4)

# Routes
@app.route("/")
def index():
    return render_template("index.html", projects=projectsDB.get_projects())


# Start
if __name__ == "__main__":
    app.run(debug=True)