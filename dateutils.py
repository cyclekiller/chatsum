from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def parse(s):
    datetime.strptime(s, DATETIME_FORMAT)
