__author__ = 'tomstelk'
import sqlite3
db_name='buy2letDB.sqlite'
zooplaTable='ZooplaPrices'
conn = sqlite3.connect(db_name)
c=conn.cursor()
c.execute('DROP TABLE IF EXISTS ' + zooplaTable)
c.execute('CREATE TABLE ' + zooplaTable + ' (zpID int NOT NULL, zpPrice int NOT NULL, zpAddress varchar(255), zpPostCode varchar(5), zpNumBeds int NOT NULL,PRIMARY KEY (zpID, zpAddress))')
conn.commit()
conn.close()

