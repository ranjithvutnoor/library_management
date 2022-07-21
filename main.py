#creating database Library
#creating tables bookrecord,member,issue
import mysql.connector as connection

def dbcreate():
    cnx = connection.connect(user='root',host='localhost',password='!dsai21@mysqL',use_pure=True)
    query="create database if not exists Library"
    cur = cnx.cursor()
    cur.execute(query)
    cnx.commit()
    cur.close()
    cnx.close()
print('database created')
def table_create():
    cnx = connection.connect(user='root',host='localhost',password='!dsai21@mysqL',use_pure=True,database='Library')
    cur = cnx.cursor()
    cur.execute("create table if not exists bookrecord(bno int(10),bname varchar(32),auth varchar(32),price int(20),publi varchar(32),quantity int(10),date_of_purchase Date)")
    cur.execute("create table if not exists member(mno int(10),mname varchar(32),date_of_membership Date,address varchar(32),mobile int(12))")
    cur.execute("create table if not exists issue(bno int(10),mno int(10),d_o_issue_date Date,d_o_return_date Date)")
    cur.close()
    cnx.close()

dbcreate()
table_create()
print('table created')
