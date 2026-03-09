import json
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# HOME ENDPOINT
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness API" in response.data

# ADD CLIENT
def test_add_client(client):
    payload = {
        "name": "TestUser",
        "age": 25,
        "height": 170,
        "weight": 65
    }
    response = client.post(
        "/clients/add",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 200

# LIST CLIENTS
def test_list_clients(client):
    response = client.get("/clients")
    assert response.status_code == 200

# ADD PROGRESS
def test_add_progress(client):
    payload = {
        "client": "TestUser",
        "week": "Week 1",
        "adherence": 80
    }
    response = client.post(
        "/progress/add",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 200

# GET PROGRESS
def test_get_progress(client):
    response = client.get("/progress")
    assert response.status_code == 200


# ADD WORKOUT
def test_add_workout(client):
    payload = {
        "client": "TestUser",
        "date": "2026-03-09",
        "type": "Strength",
        "duration": 60,
        "notes": "Leg workout"
    }
    response = client.post(
        "/workouts/add",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 200

# GET WORKOUTS
def test_get_workouts(client):
    response = client.get("/workouts")
    assert response.status_code == 200

# ADD BODY METRICS
def test_add_metrics(client):
    payload = {
        "client": "TestUser",
        "date": "2026-03-09",
        "weight": 65,
        "waist": 32,
        "bodyfat": 18
    }
    response = client.post(
        "/metrics/add",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 200

# GET METRICS
def test_get_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200

# BMI CALCULATION
def test_bmi(client):
    response = client.get("/bmi/TestUser")
    assert response.status_code == 200

# ANALYTICS
def test_analytics(client):
    response = client.get("/analytics")
    assert response.status_code == 200

# PDF REPORT
def test_report(client):
    response = client.get("/report/TestUser")
    assert response.status_code == 200