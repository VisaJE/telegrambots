import time
import pgdb
import getpass


username = input('Enter username for SQL: ')
password = getpass.getpass()
hostname = 'localhost'
db = 'testdb'
table = 'testtable'

highscore = 0
scoring_time = 0
scorer = 'Nobody'

connection = pgdb.connect(host = hostname,
                            user = username, 
                            password = password, 
                            database = db
                            )
cur = connection.cursor()

def get_highscore():
    try:
        cur.execute("SELECT MAX(%s) FROM %s;"%('amount', table))
        cur.fetchone()
    except:
        print('There was a problem with fetching data from db.')

def get_user(input_name):
    try:
        cur.execute("SELECT * FROM %s HAVING name = %s AND MAX(%s);"%(table, input_name, 'amount'))
        cur.fetchone
    except:
        raise ValueError('No datapoints were found for this name.')

def print_hs_data():
    result = get_highscore()
    score = result.amount
    if result > highscore:
        highscore = score        
        scorer = result.name
        scoring_time = result.date
    'Kovin käsienheiluttelija on %s heilutteluindeksillä %s.\n'%(scorer, highscore)
    'Ennätys tehtiin %s tuntia sitten.'%(scoring_time)

def print_user_data(input_name):
    try:
        result = get_user(input_name)
        'Tämä heppu heilutteli arvon %s %s.'%(result.amount, result.date)
    except Exception as e:
        e.args[0]


while 1:
    nimi = input('Name?')
    if (nimi != "Pekka"):
        print(print_hs_data())
    else:
    time.sleep(5)
