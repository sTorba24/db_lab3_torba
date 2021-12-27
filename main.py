import psycopg2
import matplotlib.pyplot as plt

query_1 = '''
CREATE VIEW ChargeForHuman AS
SELECT ins_charge,hum_name
FROM insuranse INNER JOIN humans ON insuranse.hum_id = humans.hum_id
'''
query_2 = '''
CREATE VIEW SmokeStat AS
SELECT isSmoker,COUNT(*)
FROM smokers 
GROUP BY isSmoker
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

            cur.execute(query_1)

            cur.execute('SELECT * FROM ChargeForHuman')

            data_to_visualise = {}

            for row in cur:
                data_to_visualise[row[1]] = row[0]

            x_range = range(len(data_to_visualise.keys()))
        
            figure, bar_ax = plt.subplots()
            bar = bar_ax.bar(x_range, data_to_visualise.values(), label='Total')
            bar_ax.set_title('Charge for every human')
            bar_ax.set_xlabel('Human')
            bar_ax.set_ylabel('Charge')
            bar_ax.set_xticks(x_range)
            bar_ax.set_xticklabels(data_to_visualise.keys())


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

            cur.execute(query_3)

            cur.execute('SELECT * FROM HumansAge')

            data_to_visualise = {}

            for row in cur:
                data_to_visualise[row[1]] = row[0]

            x_range = range(len(data_to_visualise.keys()))
        
            figure, bar_ax = plt.subplots()
            bar = bar_ax.bar(x_range, data_to_visualise.values(), label='Total')
            bar_ax.set_title('Dependency charge from age')
            bar_ax.set_xlabel('Human')
            bar_ax.set_ylabel('Age')
            bar_ax.set_xticks(x_range)
            bar_ax.set_xticklabels(data_to_visualise.keys())

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        mng = plt.get_current_fig_manager()
        mng.resize(1400, 600)

        plt.show()
        if conn is not None:
            conn.close()
            print('Database connection closed.')

connect()
