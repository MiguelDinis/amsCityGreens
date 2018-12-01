import sqlite3 as sql
import sys


def createTable(database):
	db = sql.connect(database)
	db.execute("CREATE TABLE clients (name text, email text, nif text, birth text, address text, bank text, list text)")
	db.execute("CREATE TABLE suppliers (name text, email text, nif text, birth text, address text, bank text)")
	db.execute("CREATE TABLE orders (list text)")
	db.execute("CREATE TABLE favorites (list text, users text)")
	
	db.close()

def addUser(user,database):
	dbase = sql.connect(database)
	db = dbase.cursor()
	if user.isSupplier():
		db.execute("INSERT INTO suppliers VALUES(?,?,?,?,?,?)",(user.getName(),user.getEmail(),user.getNif(),user.getBirth(),user.getAddress(),user.getBank()))
	else:
		db.execute("INSERT INTO clients VALUES(?,?,?,?,?,?,'')",(user.getName(),user.getEmail(),user.getNif(),user.getBirth(),user.getAddress(),user.getBank()))

	dbase.commit()
	dbase.close()

def remUser(user,database):
	dbase = sql.connect(database)
	db = dbase.cursor()

	if user.isSupplier():
		db.execute("DELETE FROM suppliers WHERE nif = ?",(user.getNif(),))
	else:
		db.execute("DELETE FROM clients WHERE nif = ?",(user.getNif(),))

	dbase.commit()
	dbase.close()

def addOrder(user,database,order):
	dbase = sql.connect(database)
	db = dbase.cursor()

	if user.isSupplier():
		return

	db.execute("INSERT INTO orders VALUES(?)",(order,))
	db.execute("SELECT rowid FROM orders WHERE list = ?",(order,))
	idx = str(db.fetchall()[0][0])
	db.execute("SELECT list FROM clients WHERE nif = ?",(user.getNif(),))
	lst = str(db.fetchall()[0][0])
	lst += (idx + ",")
	db.execute("UPDATE clients SET list = (?) WHERE nif = ?",(lst,user.getNif(),))

	dbase.commit()
	dbase.close()

def addToFavs(user,database,order):
	dbase = sql.connect(database)
	db = dbase.cursor()

	if user.isSupplier():
		return
	
	db.execute("INSERT INTO favorites VALUES(?,'')",(order,))
	db.execute("SELECT rowid FROM clients WHERE nif = ?",(user.getNif(),))
	idx = str(db.fetchall()[0][0])
	db.execute("SELECT users FROM favorites WHERE list = ?",(order,))
	lst = str(db.fetchall()[0][0])
	lst += (idx + ",")
	db.execute("UPDATE favorites SET users = (?) WHERE list = ?",(lst,order,))

	dbase.commit()
	dbase.close()

from user import User
import os

def main():	

	database = "db.sqlite3_test"
	if os.path.isfile(database):
		os.remove(database)

	clt1 = User("carlos","ashda@gmail.com","1234568","26-4-1998","rua da cena","1982131",False)
	clt2 = User("joao","aadsaf@gmail.com","12528","12-5-1958","rua de cima ","2131",False)
	clt3 = User("rui","asfagd@gmail.com","144314568","29-7-1968","rua quatro","1931",False)
	suppl1 = User("pedro","asafaa@gmail.com","145568","6-1-1988","rua carsa","19821",True)
	suppl2 = User("manel","aajaa@gmail.com","1298768","2-10-1978","rua arale","131",True)
	suppl3 = User("tiago","aLAKa@gmail.com","1564268","16-12-1948","rua porta","121131",True)
	createTable(database)
	addUser(clt1,database)
	addUser(clt2,database)
	addUser(clt3,database)
	addUser(suppl1,database)
	addUser(suppl2,database)
	addUser(suppl3,database)
	remUser(clt3,database)
	remUser(suppl3,database)
	addOrder(clt1,database,"{maça:5,pera:3,laranja:6,alface:2}")
	addOrder(clt1,database,"{maça:5,pera:3,laranja:6}")
	addOrder(clt1,database,"{maça:1,pera:4,laranja:2}")
	addToFavs(clt2,database,"{maça:1,pera:4,laranja:2}")
	addToFavs(clt1,database,"{maça:1,pera:4,laranja:2}")
	addToFavs(clt1,database,"{maça:5,pera:3,laranja:6}")

main()



	