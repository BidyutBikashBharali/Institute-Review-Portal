from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from . import review_bp


class ReviewForm(Form):
    first_name = StringField('First Name', validators=[Length(min=6, max=35, message="Character must be between 6-35 only."), validators.DataRequired(message="Can't leave blank!"), validators.DataRequired(message="Can't leave blank!")])
    last_name = StringField('Last Name', validators=[Length(min=6, max=35, message="Character must be between 6-35 only."), validators.DataRequired(message="Can't leave blank!"), validators.DataRequired(message="Can't leave blank!")])
    content = TextAreaField('Review', render_kw={"rows": 15, "cols": 45}, validators=[ Length(min=35, message="Character can not be less than 35 only."), validators.DataRequired(message="Can't leave blank!")])

    submit = SubmitField('Submit')
