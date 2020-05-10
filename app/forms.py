from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from instapy import InstaPy
from time import sleep

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    print(str(password))
    def validate_password(self, field):
        try:
            print(self.username.data, self.password.data)
            session = InstaPy(username=str(self.username.data),password=str(self.password.data),headless_browser=True)
            sleep(3)
            return True
        except:
            raise ValidationError('Instagram account does not exist')