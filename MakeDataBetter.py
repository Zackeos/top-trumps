import csv
import sqlite3
import os
import json


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect("store.db")
conn.row_factory = dict_factory

# conn.execute("""CREATE TABLE if not exists Cards
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#               name TEXT NOT NULL,
#               price TEXT NOT NULL,
#               sale DOUBLE NOT NULL,
#               photo TEXT NOT NULL
#             );
#              """)


def makeJson(filename):
    cards={}
    rows = []
    with open(f"Stats Data/CSVs{filename}.csv", 'r') as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)
        for row in csvreader:
            rows.append(row)
            cards[row[0]] = {}
            for x in range(1,len(row)):
                cards[row[0]][headers[x]] = row[x] 
    with open(f"Stats Data/Jsons/{filename}.json", "w") as file:
        json.dump(cards, file)

allfiles = [i.replace(".csv","") for i in os.listdir("Stats Data")]
for name in allfiles:
    if name=="Jsons":
        pass
    else:
        makeJson(name)

# makeJson("Dogs")