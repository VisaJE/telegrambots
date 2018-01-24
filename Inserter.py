import time
import pgdb

connection = pgdb.connect(host = 'localhost',
                          user = 'testuser', 
                          database = 'testdb'
                          )
i = input('How many? ')

cur = connection.cursor()
for n in range(1, i):
    date = "timestamp('2018-%s-1' %s:00:00)"%(randomInt(23), randomInt(23))
    cur.execute("INSERT INTO testtable VALUES(%s, %s, %s)"%(randomint(12),
        randomint(100), date)
connection.close()