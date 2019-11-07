from datetime import datetime, timezone
import sqlite3

def convert_time_to_utc(date_string):
    # TODO: get year, month, and day nums from date_string argument and set into test variable
    date_list = date_string.split()
    test = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]), tzinfo=timezone.utc).timestamp()
    print(test)
