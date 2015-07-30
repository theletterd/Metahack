from flask import Flask
from flask import render_template
import generator

app = Flask(__name__)

IDEAS = [
    "Build a service to fly moons to Norway",
    "Disrupt Poverty with node.js",
    "Give Bizowners bats"
]

generate_engine = generator.HackathonIdeaGenerator("test_ideas.txt")

@app.route('/')
def index():
    hackathon_idea = generate_engine.get_hackathon_idea()
    return render_template(
        'index.html',
        hackathon_idea=hackathon_idea
    )

@app.route('/get_idea')
def get_idea():
    return generate_engine.get_hackathon_idea()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
