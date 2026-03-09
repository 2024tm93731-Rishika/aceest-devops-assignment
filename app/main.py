from flask import Flask, jsonify, request
import sqlite3
from fpdf import FPDF

app = Flask(__name__)

DB = "aceest.db"

# DATABASE INITIALIZATION
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        height REAL,
        weight REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT,
        week TEXT,
        adherence INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS workouts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT,
        date TEXT,
        workout_type TEXT,
        duration INTEGER,
        notes TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT,
        date TEXT,
        weight REAL,
        waist REAL,
        bodyfat REAL
    )
    """)

    conn.commit()
    conn.close()


init_db()

programs = {
    "Fat Loss": {"factor":22},
    "Muscle Gain": {"factor":35},
    "Beginner": {"factor":26}
}

# BASIC ROUTE
@app.route("/")
def home():
    return "ACEest Fitness API Version 3.0"

@app.route("/programs")
def get_programs():
    return jsonify(programs)

@app.route("/clients/add", methods=["POST"])
def add_client():
    data=request.json
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO clients(name,age,height,weight) VALUES(?,?,?,?)",
        (data["name"], data["age"], data["height"], data["weight"])
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

# PROGRESS TRACKING
@app.route("/progress/add", methods=["POST"])
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
    
@app.route("/progress")
def get_progress():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM progress")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)
    
# WORKOUT LOGGING
@app.route("/workouts/add", methods=["POST"])
def add_workout():
    data = request.json
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO workouts(client,date,workout_type,duration,notes)
        VALUES(?,?,?,?,?)
        """,
        (
            data["client"],
            data["date"],
            data["type"],
            data["duration"],
            data["notes"]
        )
    )
    conn.commit()
    conn.close()
    return {"message": "workout logged"}


@app.route("/workouts")
def get_workouts():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM workouts")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

# BODY METRICS
@app.route("/metrics/add", methods=["POST"])
def add_metrics():
    data = request.json
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO metrics(client,date,weight,waist,bodyfat)
        VALUES(?,?,?,?,?)
        """,
        (
            data["client"],
            data["date"],
            data["weight"],
            data["waist"],
            data["bodyfat"]
        )
    )
    conn.commit()
    conn.close()
    return {"message": "metrics saved"}


@app.route("/metrics")
def get_metrics():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM metrics")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

# BMI CALCULATION
@app.route("/bmi/<name>")
def bmi(name):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT height, weight FROM clients WHERE name=?", (name,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return {"error": "client not found"}
    height = row[0] / 100
    weight = row[1]
    bmi_value = weight / (height * height)
    return {"client": name, "bmi": round(bmi_value, 2)}
    
# ANALYTICS
@app.route("/analytics")
def analytics():
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute("SELECT AVG(adherence) FROM progress")
    avg=cur.fetchone()[0]
    conn.close()
    return {"average_adherence":avg}
    
# PDF REPORT
@app.route("/report/<name>")
def generate_report(name):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients WHERE name=?", (name,))
    client = cur.fetchone()
    conn.close()
    if not client:
        return {"error": "client not found"}

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="ACEest Client Report", ln=True)
    pdf.cell(200, 10, txt=f"Name: {client[1]}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {client[2]}", ln=True)
    pdf.cell(200, 10, txt=f"Height: {client[3]}", ln=True)
    pdf.cell(200, 10, txt=f"Weight: {client[4]}", ln=True)
    file_name = f"{name}_report.pdf"
    pdf.output(file_name)
    return {"message": "report generated", "file": file_name}