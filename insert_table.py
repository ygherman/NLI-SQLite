import pandas as pd
import sqlite3
from peewee import *

connection = sqlite3.connect('NLI-VA-TEST.sqlite')

df = pd.read_excel("countries.xlsx")
df.geoname_id = df.geoname_id.apply(str)
countries = [tuple(x) for x in df.to_records(index=False)]
print(countries)
print(list(df))


def create_countries(data):
    with connection:
        cur = connection.cursor()
        cur.executemany('INSERT INTO Countries VALUES (?, ?, ?, ?)', data)
        # connection.commit()


create_countries(countries)
