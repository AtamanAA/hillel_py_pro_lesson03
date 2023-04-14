from flask import Flask, render_template, request
import statistics
import csv
from faker import Faker
import requests


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/requirements/")
def requirements():
    with open("requirements.txt", encoding='utf-16', mode="r") as file:
        requirements_list = [line for line in file]
    return render_template('requirements.html', requirements_list=requirements_list)


@app.route("/users/generate/", methods=['POST', 'GET'])
def users_generate():
    if request.method == 'POST':
        count = int(request.form['count'])
    else:
        count = 100

    fake_users = []
    fake = Faker()
    for number in range(count):
        name = fake.name()
        email = fake.email()
        fake_users.append({"id": number + 1, "name": name, "email": email})

    return render_template('users_generate.html', fake_users=fake_users, count=count)


@app.route("/mean/", methods=['GET'])
def mean():
    height_list = []
    weight_list = []

    with open('hw.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                try:
                    height_list.append(float(row[1]))
                    weight_list.append(float(row[2]))
                except ValueError:
                    continue

    mean_height_cm = round(2.54 * statistics.mean(height_list), 1)
    mean_weight_kg = round(0.453592 * statistics.mean(weight_list), 1)
    count_people = len(height_list)

    return render_template('mean.html',
                           mean_height_cm=mean_height_cm,
                           mean_weight_kg=mean_weight_kg,
                           count_people=count_people)


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    astro_data = r.json()
    astronauts_count = astro_data["number"]
    astronauts = astro_data["people"]

    return render_template('space.html', astronauts_count=astronauts_count, astronauts=astronauts)


if __name__ == "__main__":
    app.run()
