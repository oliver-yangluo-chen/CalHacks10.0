import nasdaqdatalink

nasdaqdatalink.ApiConfig.api_key = "QVRxb17n4WTYRCcchyMR"

def formatnum(num: int):
    if num < 10: return '0' + str(num)
    return str(num)

def nextdate(date: str):
    yearmonthday = [int(x) for x in date.split("-")]
    year = yearmonthday[0]
    month = yearmonthday[1]
    day = yearmonthday[2]

    month = month + 1 if day != 1 else month
    nextday = 1
    nextmonth = [x for x in [month, month+1, month+2] if (x-1)%3 == 0][0]
    nextyear = year + 1 if nextmonth > 12 else year
    nextmonth = (nextmonth-1)%12 + 1

    return str(nextyear) + '-' + formatnum(nextmonth) + '-' + formatnum(nextday)

def nextyear(date: str):
    yearmonthday = [int(x) for x in date.split("-")]
    year = yearmonthday[0]
    month = yearmonthday[1]
    day = yearmonthday[2]

    return str(year+1) + '-' + formatnum(month) + '-' + formatnum(day)




def getprice(ticker: str, date: str):
    #mydata = nasdaqdatalink.get(code, start_date=date, end_date="2023-01-01") #has data every january, april, july, october
    #return mydata
    #return mydata.at[nextdate(date), 'Value']

    mydata = nasdaqdatalink.get("WIKI/"+ticker, start_date=date, end_date=nextyear(date))
    return mydata.iloc[0]['Close']

def getlatestprice(ticker: str):
    mydata = nasdaqdatalink.get("WIKI/"+ticker)
    return mydata.iloc[-1]['Close']


#code = "FRED/GDP"
date = "2005-03-23"
#print(nextdate(date))

#print(getprice(code, date))

#print(getlatestprice(code))


#print(getprice("AAPL", date))
#print(getlatestprice("AAPL"))
#print(getlatestprice("APPL"))
#print(mydata)