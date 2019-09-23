import http.client

conn = http.client.HTTPSConnection("www.alphavantage.co")

conn.request("GET","/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))