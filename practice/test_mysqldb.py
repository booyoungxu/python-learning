# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='test_db')
cursor = conn.cursor()
insert = 'insert into lend_data values (2, 20, 0, 0, "good"), (3, 20, 1, 0, "good"), (4, 20, 1, 1, "general"), (5, 20, 0, 0, "general") '
cursor.execute(insert)
select = 'select * from lend_data'
cursor.execute(select)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
