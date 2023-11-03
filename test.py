import http.client

conn = http.client.HTTPSConnection("twelve-data1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "8924238577b744eeaf43e08122f84342",
    'X-RapidAPI-Host': "twelve-data1.p.rapidapi.com"
}

conn.request("GET", "/stocks?exchange=NASDAQ&symbol=AAPL&format=json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))