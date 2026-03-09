from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

programs = {
    "Fat Loss": {"factor":22},
    "Muscle Gain": {"factor":35},
    "Beginner": {"factor":26}
}

clients = []

@app.route("/")
def home():
    return "ACEest Fitness API Version 2.0"

@app.route("/programs")
def get_programs():
    return jsonify(programs)

@app.route("/clients/add", methods=["POST"])
def add_client():
    data=request.json
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO clients(name,age,weight) VALUES(?,?,?)",
        (data["name"],data["age"],data["weight"])
    )
    conn.commit()
    conn.close()
    return {"message":"client saved"}

@app.route("/clients")
def get_clients():
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute("SELECT * FROM clients")
    rows=cur.fetchall()
    conn.close()
    return jsonify(rows)

DB="aceest.db"

def init_db():
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        weight REAL
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/progress/add",methods=["POST"])
def add_progress():
    data=request.json
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO progress(client,week,adherence) VALUES(?,?,?)",
        (data["client"],data["week"],data["adherence"])
    )
    conn.commit()
    conn.close()
    return {"message":"progress saved"}

@app.route("/analytics")
def analytics():
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute("SELECT AVG(adherence) FROM progress")
    avg=cur.fetchone()[0]
    conn.close()
    return {"average_adherence":avg}