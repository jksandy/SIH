import csv
import sqlite3
from pathlib import Path  
import pandas as pd
connection = sqlite3.connect('crime.db')
cursor = connection.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS crime_records(
                id NUMBER NOT NULL,
                article TEXT NOT NULL,
                keywords TEXT NOT NULL,
                location TEXT NOT NULL,
                latitude NUMBER NOT NULL,
                longitude NUMBER NOT NULL,
                timestamp TIME NOT NULL,
                date DATE NOT NULL,
                crime TEXT NOT NULL);'''
cursor.execute(create_table)
datadf = pd.read_csv("SIH Data.csv")
datanew = pd.DataFrame(datadf[~datadf['Article'].isnull()])
datanew.to_csv("SIH Data2.csv")
file = open('SIH Data2.csv', encoding="utf8")
contents = csv.reader(file)
insert_records = "INSERT INTO crime_records VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"
cursor.executemany(insert_records, contents)
select_all = "SELECT * from crime_records;"
rows = cursor.execute(select_all).fetchall()
for i in rows:
    print(i)