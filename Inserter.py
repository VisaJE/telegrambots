import time
import pgdb

connection = pgdb.connect(host = 'localhost',
                          user = 'testuser',
                          database = 'testdb'
                          )
i = raw_input('How many? ')

cur = connection.cursor()
for n in range(1, i):
    date = "timestamp('2018-{}-1' {}:00:00)".format(randomint(23), randomint(23))
    cur.execute("INSERT INTO testtable VALUES({}, {}, {})".format(randomint(12), \
    randomint(100), date))
