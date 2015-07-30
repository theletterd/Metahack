import random

from flask import Flask
from flask import render_template

app = Flask(__name__)

IDEAS = [
    "Build a service to fly moons to Norway",
    "Disrupt Poverty with node.js",
    "Give Bizowners bats"
]

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/get_idea')
def get_idea():
    return random.choice(IDEAS)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
