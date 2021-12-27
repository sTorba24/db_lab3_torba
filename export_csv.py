import csv
import psycopg2

OUTPUT_FILE_T = 'torba_DB_{}.csv'

TABLES = [
    'smokers',
    'humans',
    'children',
    'insuranse'
]


conn = psycopg2.connect(
  host="localhost",
  database="studentTorba",
  user="postgres",
  password="sobaka123")

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]

        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x).lstrip() for x in row])
