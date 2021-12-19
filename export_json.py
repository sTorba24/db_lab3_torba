import json
import psycopg2

OUTPUT_FILE_T = 'torba_DB_{}.csv'

TABLES = [
    'humans',
    'children',
    'insuranse'
]


conn = psycopg2.connect(
  host="localhost",
  database="studentTorba",
  user="postgres",
  password="sobaka123")

data = {}
with conn:
    cur = conn.cursor()

    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]
        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows


with open('torba_DB.json', 'w') as outf:
    json.dump(data, outf, default=str)