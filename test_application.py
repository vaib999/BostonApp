import pytest
from application import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200

def test_predict(client):
    input_data = {
                    'crim': 0.02, 
                    'zn': 18.0,
                    'indus': 2.18,
                    'chas': 10.0,
                    'tox': 0.458,
                    'rm': 6.98,
                    'age': 45.2,
                    'dis': 6.34,
                    'rad': 3.0,
                    'tax': 222.0,
                    'ptratio': 18.5,
                    'b': 396.90,
                    'lstat': 2.94,
                }

    rv = client.post("/predict", data = input_data)
    assert b"51.29509103" in rv.data
