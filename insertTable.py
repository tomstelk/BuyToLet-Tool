__author__ = 'tomstelk'
import sqlite3
def insertTable(dbName,tableName,dataList):
    #Connect to SQLite database
    conn = sqlite3.connect(dbName)
    c=conn.cursor()
    print len(dataList)
    #Insert results into table
    c.executemany('INSERT OR IGNORE INTO ' + tableName + ' VALUES (?,?,?,?,?)', dataList)
    conn.commit()


    conn.close()