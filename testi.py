import time
import pgdb
import getpass

username = input('Enter username for SQL: ')
password = getpass.getpass()
hostname = 'localhost'
db = 'testdb'
connection = pgdb.connect(host = hostname, user = username, password = password, database = db)
cur = connection.cursor()

