from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):


    def validate_username(self, username_to_check):  
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(f'Username is taken')

    def validate_email_address(self, email_address_to_check):  
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError(f'That email address already exists')

    username = StringField(validators=[Length(min=5, max=30), DataRequired()])
    email_address = StringField(validators=[Email(), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField()


class LoginForm(FlaskForm):

    
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

    
