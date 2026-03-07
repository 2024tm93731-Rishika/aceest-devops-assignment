import os

def test_app_file_exists():
    assert os.path.exists("app.py")

def test_python_import():
    import app
    assert app is not None