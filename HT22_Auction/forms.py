import base64
from wtforms import Form, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired


# from wtforms.widgets import TextInput, PasswordInput


class RegisterForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password_confirm = PasswordField('password_confirm', validators=[DataRequired()])

    def validate_password_confirm(self, field):
        if self.password.data != field.data:
            raise ValidationError("Passwords don't match")

    async def save(self, db):
        saved_data = await db['users'].insert_one(
            {
                'username': self.username.data,
                'password': base64.b16encode(bytes(self.password.data, 'utf-8'))
            }
        )
        return str(saved_data.inserted_id)
