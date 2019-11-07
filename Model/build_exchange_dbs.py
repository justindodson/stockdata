import sqlite3

# def insert_file_into_db(file_name):
#     file = open(file_name + '.txt')
#     db = sqlite3.connect(file_name + '.sqlite')
#
#     db.execute("CREATE TABLE IF NOT EXISTS stocks (symbol TEXT, name TEXT)")
#
#     for line in file:
#         name = line.split('\t', 1)
#         db.execute("INSERT INTO stocks(symbol, name) VALUES('{}', '{}')".format(name[0], name[1].strip().replace("'", "")))
#     file.close()
#     db.commit()
#     db.close()

# insert_file_into_db('NYSE')
# insert_file_into_db('AMEX')
# insert_file_into_db('NASDAQ')

# db = sqlite3.connect('NYSE.sqlite')
# cursor = db.cursor()
# cursor.execute("Select * from stocks where(symbol='{}')".format('GE'))
# name = cursor.fetchone()
# print(name)
# cursor.close()
# db.commit()
# db.close()

db = sqlite3.connect('NYSE.sqlite')
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
