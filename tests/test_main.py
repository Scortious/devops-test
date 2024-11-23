from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Stock Price Tracker API"}

def test_get_all_stocks():
    response = client.get("/stocks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_stock():
    response = client.get("/stock/AAPL")
    assert response.status_code == 200
    assert "symbol" in response.json()
    assert "price" in response.json()

def test_update_prices():
    response = client.put("/update_prices")
    assert response.status_code == 200
    assert response.json() == {"message": "Prices updated"}
    