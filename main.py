from flask import Flask
from flask import render_template
from flask import request
from faker import Faker

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Home page</p>"


@app.route("/requirements")
def requirements():
    with open("requirements.txt", encoding='utf-16', mode="r") as file:
        requirements_list = [line for line in file]
    return render_template('requirements.html', requirements_list=requirements_list)


@app.route("/users/generate", methods=['POST', 'GET'])
def users_generate():
    if request.method == 'POST':
        count = int(request.form['count'])
    else:
        count = 100

    fake_users = []
    for number in range(count):
        fake = Faker()
        name = fake.name()
        email = fake.email()
        fake_users.append({"id": number + 1, "name": name, "email": email})

    return render_template('users_generate.html', fake_users=fake_users, count=count)


if __name__ == "__main__":
    app.run(debug=True)
