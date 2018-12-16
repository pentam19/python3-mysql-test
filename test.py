#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ドライバをimport
import mysql.connector

if __name__ == '__main__':
    connect = mysql.connector.connect(host='127.0.0.1', 
                                  user='root', 
                                  password='mysql', 
                                  port='3306', 
                                  database='test_db')
    cursor = connect.cursor()
    name = 'テストユーザ'
    id = 1

    # insert
    cursor.execute('insert into personal (id, name) values (%s, %s)', (id, name))

    # select
    cursor.execute('select * from personal')
    row = cursor.fetchone()

    for i in row:
        print(i)

    cursor.close()
    connect.close()
