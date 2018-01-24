import time
import pgdb
import getpass
from datetime import datetime, timedelta

username = input('Enter username for SQL: ')
password = getpass.getpass()
hostname = 'localhost'
db = 'testdb'
table = 'testtable'

connection = pgdb.connect(host = hostname,
                          user = username, 
                          database = db
                          )
cur = connection.cursor()
def get_highscore():
    print('Highscore called')
    cur.execute("SELECT * FROM %s ORDER BY %s DESC, %s LIMIT 1 "%(table, 'amount', 'date'))
    return cur.fetchone()

def get_user(input_name):
    cur.execute("SELECT * FROM %s WHERE name = '%s' ORDER BY %s DESC LIMIT 1"%(table,
            input_name, 'amount'))
    return cur.fetchone()


def print_hs_data():
    result = get_highscore()
    score = result.amount
    time = result.date + timedelta(hours=2)
    text =  'Kovin heiluttelija on %s indeksin arvolla %s.\n\
            Saavutus  tehtiin %s'%(result.name,score,time)
    return text

def print_user_data(input_name):
    result = get_user(input_name)
    return 'Kyseinen heppu heilutteli arvon %s.'%(result.amount)


while 1:
    print('Starting test')
    nimi = input('Nimi?')
    if (nimi == ''):
        print(print_hs_data())
    else:
        print(print_user_data(nimi))
        time.sleep(5)
