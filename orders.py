import logging

class Orders:
    def __init__(self, client):
        self.client = client

    def market_order(self, symbol, side, quantity):
        try:
            logging.info(f"MARKET ORDER REQUEST: {symbol} {side} {quantity}")

            order = self.client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logging.info(f"RESPONSE: {order}")

            print("\n✅ MARKET ORDER SUCCESS")
            print("Order ID:", order.get("orderId"))
            print("Status:", order.get("status"))

            return order

        except Exception as e:
            logging.error(f"MARKET ERROR: {str(e)}")
            print("\n❌ Market Order Error:", str(e))
            return None


    def limit_order(self, symbol, side, quantity, price):
        try:
            logging.info(f"LIMIT ORDER REQUEST: {symbol} {side} {quantity} price={price}")

            order = self.client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logging.info(f"RESPONSE: {order}")

            print("\n✅ LIMIT ORDER SUCCESS")
            print("Order ID:", order.get("orderId"))
            print("Status:", order.get("status"))

            return order

        except Exception as e:
            logging.error(f"LIMIT ERROR: {str(e)}")
            print("\n❌ Limit Order Error:", str(e))
            return None