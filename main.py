import psycopg2
import matplotlib.pyplot as plt

query_1 = '''
CREATE VIEW ChargeForHuman AS
SELECT ins_charge,hum_name
FROM insuranse INNER JOIN humans ON insuranse.hum_id = humans.hum_id
'''
query_2 = '''
CREATE VIEW SmokeStat AS
SELECT hum_smoker,COUNT(*)
FROM humans 
GROUP BY hum_smoker
'''

query_3 = '''
CREATE VIEW HumansAge AS
SELECT ins_charge,hum_age 
FROM insuranse INNER JOIN humans ON insuranse.hum_id = humans.hum_id
'''

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host="localhost",
            database="studentTorba",
            user="postgres",
            password="sobaka123")
		
        with conn:
            cur = conn.cursor()

            cur.execute('DROP VIEW IF EXISTS ChargeForHuman')
            print('Query 1:')
            cur.execute(query_1)
            cur.execute('SELECT * FROM ChargeForHuman')
            values = []
            names = []
            for row in cur:
                print(row)
                values.append(row[0])
                names.append(row[1])
            
            fig1 = plt.bar(names, values,width = 0.7)

            cur.execute('DROP VIEW IF EXISTS SmokeStat')
            print('\nQuery 2:')
            cur.execute(query_2)
            cur.execute('SELECT * FROM SmokeStat')
            smokes = []
            count = []
            for row in cur:
                print(row)
                smokes.append(row[0])
                count.append(row[1])

            fig2, ax = plt.subplots()
            ax.pie(count, labels=smokes)
            ax.axis("equal")
            
            cur.execute('DROP VIEW IF EXISTS HumansAge')
            print('\nQuery 3:')
            cur.execute(query_3)
            cur.execute('SELECT * FROM HumansAge')
            moneys=[]
            ages=[]
            for row in cur:
                print(row)
                moneys.append(row[0])
                ages.append(row[1])
            
            fig3 = plt.bar(ages, moneys,width = 0.5)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        plt.show()
        if conn is not None:
            conn.close()
            print('Database connection closed.')

connect()
plt.show()
