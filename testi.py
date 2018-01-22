import time
import pgdb
import getpass


username = input('Enter username for SQL: ')
password = getpass.getpass()
hostname = 'localhost'
db = 'testdb'
table = 'handwave'
measure_name = 'amount'


connection = pgdb.connect(host = hostname,
                            user = username, 
                            password = password, 
                            database = db
                            )
cur = connection.cursor()

def get_highscore():
    try:
        cur.execute("SELECT MAX(%s) FROM %s"%(measureName, table))
        cur.fetchone()
    except:
        print('There was a problem with fetching data from db.')

def print_data():
    result = get_highscore()
    score = result.measure_name
    time = (time.time()*10**6 - result.date_added)/10**6/3600
    scorer = result.name
    'Kovin käsienheiluttelija on %s heilutteluindeksillä %s.\n'%(name, score)
    'Ennätys tehtiin %s tuntia sitten.'%(scorer)

while 1:
    input('Go?')
    print(print_data())