from calculatereturn import *
import csv

with open('namereturn.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'return']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


    #writer.writeheader()
    names = getallnames()
    for n in names:
        print(n)
        r = getreturn(n)
        writer.writerow({'name': n, 'return': r})

