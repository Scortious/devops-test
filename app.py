from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict
import random

app = FastAPI()

# Serve static files on a dedicated path
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory storage for stock prices
stocks: Dict[str, float] = {
    "AAPL": 150.0,
    "GOOGL": 2800.0,
    "MSFT": 300.0,
    "AMZN": 3300.0,
}

class Stock(BaseModel):
    symbol: str
    price: float

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Stock Price Tracker API"}

@app.get("/stocks")
async def get_all_stocks():
    return [{"symbol": symbol, "price": price} for symbol, price in stocks.items()]

@app.get("/stock/{symbol}")
async def get_stock(symbol: str):
    if symbol not in stocks:
        raise HTTPException(status_code=404, detail="Stock not found")
    return {"symbol": symbol, "price": stocks[symbol]}

@app.put("/update_prices")
async def update_prices():
    for symbol in stocks:
        # Simulate price change
        change = random.uniform(-5, 5)
        stocks[symbol] = round(stocks[symbol] * (1 + change / 100), 2)
    return {"message": "Prices updated"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
