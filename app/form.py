from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import TextAreaField
from wtforms.validators import  DataRequired


class RegistrationForm(FlaskForm):
    name = StringField('Username',validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    subject =StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    