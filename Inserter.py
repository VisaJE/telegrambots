import time
import pgdb
from random import randint
connection = pgdb.connect(host = 'localhost',
                          user = 'testuser',
                          database = 'testdb'
                          )
i = int(raw_input('How many? '))

cur = connection.cursor()
for n in range(0, i):
    date = '2018-1-{} {}:00:00'.format(randint(1,23),randint(1,23)) 
    cur.execute("INSERT INTO testtable VALUES('{}', {}, '{}');".format(randint(0,12), \
            randint(1,100), date))
connection.commit()
