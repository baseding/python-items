#!/usr/bin/env python
import MySQLdb

def DoUpdate(item_name="none",result="none",currenttime="none"):
    #
    db = MySQLdb.connect("localhost","yfding","yfding","MonitorBook",3307 )
    cursor = db.cursor()

    #
    sql = """INSERT INTO Pings(ITEM_NAME,RESULT, DATETIME) 
             VALUES ('%s', '%s', '%s')""" % (item_name,result,currenttime)

    try:
        #
        cursor.execute(sql)
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

