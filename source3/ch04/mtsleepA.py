#!/usr/bin/env python

import pymysql

conn = pymysql.connect(host='10.133.146.250',port = 3306,user='root',passwd='Midea@123',db = 'search')

cur = conn.cursor()

cur.execute("SELECT * FROM tenant_info")

for r in cur.fetchall():

           print(r[1])

cur.close()

conn.close()