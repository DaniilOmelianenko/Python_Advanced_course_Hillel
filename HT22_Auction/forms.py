import base64
from wtforms import Form, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired


# from wtforms.widgets import TextInput, PasswordInput


class DBMixin:
    def __init__(self, *args, **kwargs):
        self.db = kwargs.pop('db')
        super(DBMixin, self).__init__(*args, **kwargs)


class RegisterForm(DBMixin, Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password_confirm = PasswordField('password_confirm', validators=[DataRequired()])

    def validate_username(self, field):
        result = self.db['users'].find_one({'username': field.data})
        if result:
            raise ValidationError('------------------------------Username already exists')

    def validate_password_confirm(self, field):
        if self.password.data != field.data:
            raise ValidationError("------------------------------Passwords don't match")

    async def save(self, db):
        saved_data = await db['users'].insert_one(
            {
                'username': self.username.data,
                'password': base64.b16encode(bytes(self.password.data, 'utf-8'))
            }
        )
        return str(saved_data.inserted_id)


class LoginForm(DBMixin, Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def validate_password(self, field):
        password = base64.b16encode(bytes(self.password.data, 'utf-8'))
        result = self.db['users'].find_one({'username': self.username.data, 'password': password})
        if not result:
            raise ValidationError('---------------------------your data is incorrect')
        self.user_id = str(result['_id'])
