import sys

class User():
	def __init__(self,name,email,nif,birth,address,bank = None,supplier = False):
		self.name = name
		self.email = email
		self.nif = nif
		self.birth = birth
		self.address = address
		self.bank = bank
		self.supplier = supplier

	def getName(self):
		return self.name

	def getEmail(self):
		return self.email

	def setEmail(self,newEmail):
		self.email = newEmail

	def getNif(self):
		return self.nif

	def getBirth(self):
		return self.birth

	def getAddress(self):
		return self.address

	def getBank(self):
		return self.bank

	def setAddress(self,newAddress):
		self.address = newAddress

	def isSupplier(self):
		return self.supplier