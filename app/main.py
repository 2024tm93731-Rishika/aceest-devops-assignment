from flask import Flask, jsonify, request

app = Flask(__name__)

programs = {
    "Fat Loss": {"factor":22},
    "Muscle Gain": {"factor":35},
    "Beginner": {"factor":26}
}

clients = []

@app.route("/")
def home():
    return "ACEest Fitness API Version 1.1"

@app.route("/programs")
def get_programs():
    return jsonify(programs)

@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify(clients)

@app.route("/clients/add", methods=["POST"])
def add_client():
    data = request.json
    clients.append(data)
    return {"message":"client added"}