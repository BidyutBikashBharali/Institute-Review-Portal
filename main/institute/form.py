from flask_wtf import Form

from wtforms import StringField, validators, SubmitField

from wtforms.validators import ValidationError, DataRequired, Length


class InstituteForm(Form):

     institute_name = StringField('Institute Name', validators=[validators.DataRequired(message="Can't leave blank!"), Length(min=3, max=35, message=("Characters should be between 6 to 35 only."))])
     institute_address = StringField('Institute Address', validators=[validators.DataRequired(message="Can't leave blank!"), Length(min=3, max=35, message=("Characters should be between 6 to 35 only."))])
     submit = SubmitField('Submit')