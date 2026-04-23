from logger import setup_logger
from client import BinanceClient
from orders import Orders

setup_logger()

API_KEY = "53Td3pGSbpjHUPdv6LIpiwGoBgrDkmWEUgdVIdcbKV10mu6j98z4ngkuRM2OQUrY"
API_SECRET = "dJT0LrVwulfZxqOIuuyytvIleevuhvFSOwu2UCpZlx94yF4i0z8Ql0aatrXZ8LZu"

bot = BinanceClient(API_KEY, API_SECRET)
orders = Orders(bot)

print("=== BINANCE FUTURES BOT ===")

symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
side = input("Enter side (BUY/SELL): ").upper()
order_type = input("Enter order type (MARKET/LIMIT): ").upper()

try:
    quantity = float(input("Enter quantity: "))
except:
    print("Invalid quantity ❌")
    exit()

if order_type == "LIMIT":
    try:
        price = float(input("Enter price: "))
    except:
        print("Invalid price ❌")
        exit()

    result = orders.limit_order(symbol, side, quantity, price)

elif order_type == "MARKET":
    result = orders.market_order(symbol, side, quantity)

else:
    print("Invalid order type ❌")
    result = None

print("\n📊 FINAL RESPONSE:")
print(result)
