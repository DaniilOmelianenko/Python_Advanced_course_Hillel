from flask import Flask, render_template
from faker import Faker
import requests


# app = Flask(__name__, template_folder='requirements')
app = Flask(__name__)


@app.route('/index/')
def home():
    somee_var = 12
    user = {
        'name': 'BlueRam',
        'age': 29
    }
    # with open('requirements/requirements.txt') as tmps:
    # with open('templates/index.html') as tmps:
    # return tmps.read()
    context = {
        'some_var': somee_var,
        'user': user
    }
    return render_template(
        'requirements/requirements.txt', **context
    )


@app.route('/generate_users/')
def generate_users():
    fake = Faker()
    fake_name = fake.name()
    context = {
        'name': fake_name
    }
    # return render_template('generate_users/generate_users.html', **context)
    return f'{fake.name()} : {fake.name()}@mail.com' in range(100)


if __name__ == '__main__':
    app.run(debug=True)
