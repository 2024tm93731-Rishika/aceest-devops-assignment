import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_programs():
    client = app.test_client()
    response = client.get("/programs")
    assert response.status_code == 200