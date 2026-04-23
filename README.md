# Binance Futures Testnet Trading Bot

## 📌 Overview
This is a simple Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## 🚀 Features
- Market Orders (BUY/SELL)
- Limit Orders (BUY/SELL)
- CLI Input
- Logging system
- Error handling

## ⚙️ Setup

1. Clone repo / download code
2. Install dependencies:
   pip install -r requirements.txt

3. Add your API keys in cli.py

## ▶️ Run

Market Order:
python cli.py

Then input:
BTCUSDT
BUY
MARKET
0.001

Limit Order:
BTCUSDT
BUY
LIMIT
0.001
50000

## 📁 Logs
All requests and responses are saved in:
bot.log

## 🧠 Assumptions
- Using Binance Futures Testnet
- Valid API keys required