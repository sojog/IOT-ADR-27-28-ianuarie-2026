
import requests

URL = "https://api3.binance.com/api/v3/avgPrice?symbol=BTCUSDT"

reponse = requests.get(URL)
print(reponse)
print(reponse.content)