from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

import generator

app = Flask(__name__)

IDEAS = [
    "Build a service to fly moons to Norway",
    "Disrupt Poverty with node.js",
    "Give Bizowners bats"
]

generate_engine = generator.HackathonIdeaGenerator("test_ideas.txt")

@app.route('/', methods=['GET'])
def index():
    hackathon_idea = generate_engine.get_hackathon_idea()
    message = None
    if request.args.get('from_submission'):
        message = 'Thanks for your contribution!'
    return render_template(
        'index.html',
        hackathon_idea=hackathon_idea,
        message=message
    )

@app.route('/get_idea', methods=['GET'])
def get_idea():
    return generate_engine.get_hackathon_idea()

@app.route('/submit', methods=['GET', 'POST'])
def submit_idea():
    if request.method == 'POST':
        idea = request.form['idea']
        generate_engine.add_new_idea(idea)
        return redirect('/?from_submission=1')
    else:
        return render_template(
            'submit.html'
        )

if __name__ == '__main__':
    app.run(host="0.0.0.0")
