from getstocks import *
from getpolis import *

def getreturn(name: str):
    #get all rows with name
    rows = getnamerows(name)
    trades = dict()
    for index, row in rows.iterrows():
        print(row)

getreturn("Robert J. Wittman")
