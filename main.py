from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Home page</p>"


@app.route("/requirements")
def requirements():
    with open("requirements.txt", encoding='utf-16', mode="r") as file:
        requirements_list = [line for line in file]
    return render_template('requirements.html', requirements_list=requirements_list)

if __name__ == "__main__":
    app.run(debug=True)
