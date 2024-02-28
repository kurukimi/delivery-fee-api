from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)

def test_basic_fees():
    body = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 4,
        "time": "2024-01-28T14:59:59Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 200}

def test_rush_time_low():
    body = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 4,
        "time": "2024-01-26T15:00:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 240}

def test_rush_time_high():
    body = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 4,
        "time": "2024-01-26T19:00:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 240}

def test_cart_value_less():
    body = {
        "cart_value": 100,
        "delivery_distance": 1000,
        "number_of_items": 4,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 1100}

def test_cart_value_free():
    body = {
        "cart_value": 20000,
        "delivery_distance": 1000,
        "number_of_items": 4,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 0}

def test_delivery_distance():
    body = {
        "cart_value": 1000,
        "delivery_distance": 2000,
        "number_of_items": 4,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 400}

def test_delivery_distance_higher():
    body = {
        "cart_value": 1000,
        "delivery_distance": 2001,
        "number_of_items": 4,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 500}

def test_additional_items():
    body = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 5,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 250}

def test_max_fee():
    body = {
        "cart_value": 1000,
        "delivery_distance": 100000,
        "number_of_items": 5,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 1500}


def test_incorrect_request():
    body = {
        "cart_value": "...",
        "delivery_distance": 1000,
        "number": 5,
        "time": "2024-01-28T14:59:00Z"
    }
    response = client.post("/delivery_fee/", json=body)
    assert response.status_code == 422