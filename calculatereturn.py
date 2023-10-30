from getstocks import *
from getpolis import *

def profit(shares, earned, spent):
    for k in shares.keys():
        earned += getlatestprice(k)
    print(earned, spent)
    return (earned-spent)/spent

def getreturn(name: str):
    #get all rows with name
    rows = getnamerows(name)
    shares = dict() #ticker: number of shares
    spent = 0.0 #sum of purchases
    earned = 0.0 #sum of sells
    for index, row in rows.iterrows():
        ticker = rows.at[index, 'Ticker']
        transaction = rows.at[index, 'Transaction']
        amount = rows.at[index, 'Amount']
        print(earned, spent)
        date = rows.at[index, 'TransactionDate']
        try:
            price = getprice(ticker, date)
            print(price)
        except:
            continue
        if ticker not in shares:
            shares[ticker] = 0.0
        if transaction == 'Purchase':
            spent += amount
            shares[ticker] += amount/price
        else: #sell
            earned += amount
            shares[ticker] -= amount/price
    return profit(shares, earned, spent)
        


print(getreturn("Robert J. Wittman"))
