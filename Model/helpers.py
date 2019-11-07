import sqlite3

# Method to search each db to find certain stock symbol
def search_for_stock_ticker(stock_symbol):
    name = None
    if name is None:
        db = sqlite3.connect('Model/NYSE.sqlite')
        name = __search_db(db, stock_symbol)
        db.close()

    if name is None:
        db = sqlite3.connect('Model/NASDAQ.sqlite')
        name = __search_db(db, stock_symbol)
        db.close()

    if name is None:
        db = sqlite3.connect('Model/AMEX.sqlite')
        name = __search_db(db, stock_symbol)
        db.close()

    return name

# Create a search of given db and return the search result
def __search_db(db, stock_symbol):
    cursor = db.cursor()
    cursor.execute("Select * from stocks where(symbol='{}')".format(stock_symbol))
    name = cursor.fetchone()
    cursor.close()
    return name

