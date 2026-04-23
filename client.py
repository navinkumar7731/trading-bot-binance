from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

        # IMPORTANT: Binance Futures Testnet endpoints
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        self.client.API_URL = "https://testnet.binancefuture.com/api"

    def test_connection(self):
        try:
            # simple safe call to check connection
            account = self.client.futures_account()
            print("Connected to Binance Testnet ✅")
            return account

        except Exception as e:
            print("Connection Error ❌:", str(e))
            return None