import sqlite3


def search_for_stock_ticker(stock_symbol):
    name = None
    if name == None:
        db = sqlite3.connect('../Model/NYSE.sqlite')
        cursor = db.cursor()
        cursor.execute("Select * from stocks where(symbol='{}')".format(stock_symbol))
        name = cursor.fetchone()
        cursor.close()
        db.commit()
        db.close()
    if name == None:
        db = sqlite3.connect('../Model/NASDAQ.sqlite')
        cursor = db.cursor()
        cursor.execute("Select * from stocks where(symbol='{}')".format(stock_symbol))
        name = cursor.fetchone()
        cursor.close()
        db.commit()
        db.close()
    if name == None:
        db = sqlite3.connect('../Model/AMEX.sqlite')
        cursor = db.cursor()
        cursor.execute("Select * from stocks where(symbol='{}')".format(stock_symbol))
        name = cursor.fetchone()
        cursor.close()
        db.commit()
        db.close()

    return name

