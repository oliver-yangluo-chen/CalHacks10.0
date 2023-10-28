from getstocks import *
from getpolis import *



def getreturn(name: str):
    #get all rows with name
    rows = getnamerows(name)
    rows.sort_values(by=['TransactionDate'], ascending = True)
    #print(rows)
    for index, row in rows.iterrows(): print(rows.at[index, 'TransactionDate'])
    return
    shares = dict() #ticker: number of shares
    spent = 0.0 #sum of purchases
    earned = 0.0 #sum of sells
    for index, row in rows.iterrows():
        ticker = rows.at[index, 'Ticker']
        transaction = rows.at[index, 'Transaction']
        amount = rows.at[index, 'Amount']
        date = rows.at[index, 'TransactionDate']
        if ticker not in shares:
            return

        
        



getreturn("Robert J. Wittman")
