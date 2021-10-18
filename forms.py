from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.widgets.html5 import NumberInput
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, URL, NumberRange

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

class PasswordForm(FlaskForm):
    length = IntegerField("Length",
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