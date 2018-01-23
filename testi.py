import time
import pgdb
import getpass


username = input('Enter username for SQL: ')
password = getpass.getpass()
hostname = 'localhost'
db = 'testdb'
table = 'testtable'

_highscore = 0
scoring_time = 0
scorer = 'Nobody'

connection = pgdb.connect(host = hostname,
                          user = username, 
                          database = db
                          )
cur = connection.cursor()

def get_highscore():
    try:
        cur.execute("SELECT * FROM %s ORDER BY %s DESC"%(table, 'amount'))
        return cur.fetchone()
    except:
        print('There was a problem with fetching data from db.')

def get_user(input_name):
    try:
        cur.execute("SELECT max(amount) FROM %s WHERE name = %s"%(table,
            input_name))
        return cur.fetchone()
    except:
        raise ValueError('No datapoints were found for this name.')

def print_hs_data():
    result = get_highscore()
    score = result.amount
    if result >  _highscore:
        _highscore = score        
        scorer = result.name
        scoring_time = result.date
    text =  'Kovin heiluttelija on %s indeksin arvolla %s.\n'%(scorer, highscore)
    'Suoritus tehtiin ajanhetkella.'%(scoring_time)
    return text

def print_user_data(input_name):
    try:
        result = get_user(input_name)
        return 'Kyseinen heppu heilutteli arvon %s.'%(result.amount)
    except Exception as e:
        e.args[0]


while 1:
    print('Starting test')
    cur.execute("SELECT * FROM testtable")
    print(cur.fetchone().name)
    print(cur.fetchone()[0])
    nimi = input('Nimi?')
    if (nimi != "Pekka"):
        print(print_hs_data())
    else:
        print(print_user_data('Pekka'))
        time.sleep(5)
