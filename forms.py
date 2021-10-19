from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.widgets.html5 import NumberInput
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, URL, NumberRange

class ProjectForm(FlaskForm):
    name = StringField("Name",
        render_kw={"placeholder": "Project name"},
        validators=[DataRequired(), Length(min=2, max=32)])

    description = StringField("Description",
        render_kw={"placeholder": "Project description"},
        validators=[DataRequired(), Length(min=2, max=64)])

    github_repo = StringField("Github repository URL",
        render_kw={"placeholder": "https://github.com/lorenzo3117/multipurpose-python-website.git"},
        validators=[DataRequired(), URL()])

    deadline = DateField("Deadline",
        render_kw={"placeholder": "Project deadline"},
        validators=[DataRequired()])

    submit = SubmitField("Add project")

class PasswordForm(FlaskForm):
    length = IntegerField("Password length",
        render_kw={"placeholder": "Between 1 and 128"},
        widget=NumberInput(min=1, max=128, step=1),
        validators=[DataRequired(), NumberRange(min=1, max=128)])

    lowerCase = BooleanField("Include lower case letters?")
    upperCase = BooleanField("Include upper case letters?")
    numbers = BooleanField("Include numbers?")
    specials = BooleanField("Include special characters?")
    
    submit = SubmitField("Generate password")

    def validate(self, extra_validators=None):
        if not super().validate(extra_validators=extra_validators):
            return False

        for field in [self.lowerCase, self.upperCase, self.numbers, self.specials]:
            if field.data:
                return True
        
        return False