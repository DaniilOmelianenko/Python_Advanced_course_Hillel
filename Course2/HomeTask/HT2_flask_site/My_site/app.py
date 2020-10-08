from flask import Flask, render_template, request
from faker import Faker
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/requirements/')
def requirements():
    with open('templates/requirements/requirements.txt') as required:
        requirements_list = required.read().splitlines()
        return render_template('/requirements/requirements.html', requirements_list=requirements_list)


@app.route('/users/', methods=['POST', 'GET'])
def generate_users():
    fake = Faker()
    users = {}
    number_of_users = 0
    if request.method == 'POST' and request.form['usr_num'].isdigit():
        number_of_users = int(request.form['usr_num'])
    for random_user in range(number_of_users):
        temp_name = fake.name()
        users[temp_name] = str(temp_name.replace(' ', ''))+'@mail.com'
    return render_template('/generate_users/generate_users.html', users=users, number_of_users=number_of_users)


@app.route('/astros/')
def astros():
    astro_request = requests.get('http://api.open-notify.org/astros.json')
    number_of_astros = astro_request.json()["number"]
    astros_in_space = astro_request.json()["people"]
    context = {
        'number_of_astros': number_of_astros,
        'astros_in_space': astros_in_space
    }
    return render_template('/astros/astros.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
