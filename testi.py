import time
import pgdb
import getpass


username = input('Enter username for SQL: ')
password = getpass.getpass()
hostname = 'localhost'
db = 'testdb'
table = 'testtable'

connection = pgdb.connect(host = hostname,
                          user = username, 
                          database = db
                          )

def get_highscore():
    try:
        cur = connection.cursor()
        cur.execute("SELECT * FROM %s ORDER BY %s DESC, %s"%(table, 'amount', 'date'))
        result = cur.fetchone()
        cur.close()
        return result
    except:
        print('There was a problem with fetching data from db.')

def get_user(input_name):
    try:
        cur = connection.cursor()
        cur.execute("SELECT * FROM %s WHERE name = %s ORDER BY %s DESC"%(table,
            input_name, 'amount'))
        result = cur.fetchone()
        cur.close()
        return result
    except:
        raise ValueError('No datapoints were found for this name.')

def print_hs_data():
    result = get_highscore()
    score = result.amount
    time = result.date
    text =  'Kovin heiluttelija on %s indeksin arvolla %s.\n'%(result.name,score)
    'Suoritus tehtiin ajanhetkella.'%(time)
    return text

def print_user_data(input_name):
    try:
        result = get_user(input_name)
        return 'Kyseinen heppu heilutteli arvon %s.'%(result.amount)
    except Exception as e:
        e.args[0]


while 1:
    print('Starting test')
    nimi = input('Nimi?')
    if (nimi == ''):
        print(print_hs_data())
    else:
        print(print_user_data(nimi))
        time.sleep(5)
