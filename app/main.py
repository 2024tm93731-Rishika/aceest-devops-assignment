from flask import Flask, jsonify

app = Flask(__name__)

programs = {
    "Fat Loss": {
        "workout": "Back Squat + Cardio",
        "diet": "Egg Whites + Oats"
    },
    "Muscle Gain": {
        "workout": "Squat + Bench + Deadlift",
        "diet": "Eggs + Chicken"
    },
    "Beginner": {
        "workout": "Pushups + Air Squats",
        "diet": "Balanced Diet"
    }
}

@app.route("/")
def home():
    return "ACEest Fitness API Version 1.0"

@app.route("/programs")
def get_programs():
    return jsonify(programs)