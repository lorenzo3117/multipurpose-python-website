from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, URL

class ProjectForm(FlaskForm):
    name = StringField("Name",
                        validators=[DataRequired(), Length(min=2, max=32)])
    description = StringField("Description",
                        validators=[DataRequired(), Length(min=2, max=64)])
    github_repo = StringField("Github repository URL",
                        validators=[DataRequired(), URL()])
    deadline = DateField("Deadline",
                        validators=[DataRequired()])
    submit = SubmitField("Add project")