import sqlite3 as sql
import sys

def createTable(database,tableName):
	db = sql.connect(database)
	db.execute("CREATE TABLE " + tableName + " (name, email, nif, birth, address, bank)")
	db.close()

def addUser(user,database):
	db = sql.connect(database)
	
	if user.isSupplies():
		db.execute("INSERT INTO suppliers VALUES('" + user.getName() + "', '" + user.getEmail() + "', '" + user.getNif() + "', '" + user.getBirth() + "', '" user.getAddress() + "', '" + user.getBank() + "')")
	else:
		db.execute("INSERT INTO clients VALUES('" + user.getName() + "', '" + user.getEmail() + "', '" + user.getNif() + "', '" + user.getBirth() + "', '" user.getAddress() + "', '" + user.getBank() + "')")		

	db.close()

def remUser(user,database):
	pass

def resetPswd(user,database,newPass):
	pass

def addOrder(user,database,order):
	pass

def addToFavs(user,database,order):
	pass