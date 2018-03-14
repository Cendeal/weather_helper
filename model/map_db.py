#!/usr/bin/python
#coding:utf-8
import sqlite3

def initdata(dbname,sqlfile):
	db=sqlite3.connect(dbname)
	db_cursor=db.cursor()
	db_cursor.execute('''
		CREATE TABLE IF NOT EXISTS PROVINCES
		(PID INT PRIMARY KEY NOT NULL,
		PROVINCE VARCHAR(50) NOT NULL);
		''')

	db_cursor.execute('''
		CREATE TABLE IF NOT EXISTS CITYS
		(CID INT 		KEY NOT NULL,
		CITY VARCHAR(50) PRIMARY KEY NOT NULL,
		PID INT 		NOT NULL);
		''')
	msg=db_cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
	print(msg.fetchall())
	file=open(sqlfile,'r')
	for l in file.readlines():
		db_cursor.execute(l.strip('\n'))
	file.close()
	db.commit()
	db.close()
	print('finsh')
def search_province_by_city(dbname,city):
	sql='select province from provinces join citys on provinces.pid = citys.pid and city = \''+city+'\''
	db=sqlite3.connect(dbname)
	db_cursor=db.cursor()
	cur=db_cursor.execute(sql)
	province=''
	data_cur=cur.fetchone()
	if data_cur!=None:
		province=data_cur[0]
	#print(province)
	db.close()
	return province