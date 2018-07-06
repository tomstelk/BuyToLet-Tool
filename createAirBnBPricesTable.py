__author__ = 'tomstelk'
import sqlite3
db_name='buy2letDB.sqlite'
airBnBTable='AirBnBPrices'
conn = sqlite3.connect(db_name)
c=conn.cursor()
c.execute('DROP TABLE IF EXISTS ' + airBnBTable)
c.execute('CREATE TABLE ' + airBnBTable + ' (airID int NOT NULL, airPrice int NOT NULL, airAddress varchar(255), airPostCode varchar(5), airNumGuests int NOT NULL,PRIMARY KEY (airID, airAddress))')
conn.commit()
conn.close()
