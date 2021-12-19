import csv
import psycopg2


INPUT_CSV_FILE = 'insurance.csv'

query_0 = '''
CREATE TABLE humans_new
(
  hum_age INTEGER NOT NULL,
  hum_smoker VARCHAR(40) NOT NULL,
  hum_sex VARCHAR(40) NOT NULL
)
'''

query_1 = '''
DELETE FROM humans_new
'''

query_2 = '''
INSERT INTO humans_new (hum_age, hum_smoker, hum_sex) VALUES (%s, %s, %s)
'''

conn = psycopg2.connect(
  host="localhost",
  database="studentTorba",
  user="postgres",
  password="sobaka123")

with conn:

    cur = conn.cursor()
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)

        for idx, row in enumerate(reader):
            values = (row['age'], row['smoker'], row['sex'])
            cur.execute(query_2, values)

    conn.commit()