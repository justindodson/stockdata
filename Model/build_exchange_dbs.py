import sqlite3

def insert_file_into_db(file_name):
    file = open(file_name + '.txt')
    db = sqlite3.connect(file_name + '.sqlite')

    db.execute("CREATE TABLE IF NOT EXISTS stocks (symbol TEXT, name TEXT)")

    for line in file:
        name = line.split('\t', 1)
        db.execute("INSERT INTO stocks(symbol, name) VALUES('{}', '{}')".format(name[0], name[1].strip().replace("'", "")))
    file.close()
    db.commit()
    db.close()

insert_file_into_db('NYSE')
insert_file_into_db('AMEX')
insert_file_into_db('NASDAQ')


