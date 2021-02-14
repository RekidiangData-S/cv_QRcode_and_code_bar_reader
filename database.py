import sqlite3

def create_db():
	conn = sqlite3.connect('agent.db')
	#create table
	c = conn.cursor() #create a cursor
	# data type : NULL, INTEGER, REAL, TEXT, BLOB

	c.execute("""CREATE TABLE people (
	
		(ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL
		)""")

def show_all():
	"""
		Query the DB and return all records
	"""
	print("************ ALL RECORDS ************************")
	
	#create DB or Connect to DB
	conn = sqlite3.connect('agent.db')
	#create a cursor
	c = conn.cursor() 

	# Qeury the database
	c.execute("SELECT * FROM  people")
	items = c.fetchall()

	for i in items:
		print(i)

	# commit our command
	conn.commit()
	#close connection
	conn.close()

def add_one(ID, NAME, AGE):
	"""
		Add new record to the table
	"""
	#create DB or Connect to DB
	conn = sqlite3.connect('agent.db')
	#create a cursor
	c = conn.cursor()
	c.execute("INSERT INTO people VALUES(?,?,?)", (ID, NAME, AGE))
	# commit our command
	conn.commit()
	#close connection
	conn.close()

def add_record():
	print("Add New Record :")
	print("*************** :")
	id = input("Enter First ID : ")
	last_name = input("Enter Last NAME : ")
	age = input("Enter AGE : ")

	print("************************************")
	print("New Record Added Succesfully !!!")
	add_one(id, last_name, age, )

def delete_one(id):
	"""
		delete record from the table
	"""
	#create DB or Connect to DB
	conn = sqlite3.connect('agent.db')
	#create a cursor
	c = conn.cursor()
	print("DELETE RECORD")
	print("*************")
	print("Which Record do you want to delete () : ")
	id = input("Enter Record Id : ")
	
	mem = input("Do you want to delete this record(Yes/No) :")
	if mem == 'Yes':
		c.execute("DELETE FROM customers WHERE rowid = (?)",id)
		print("Record deleted succesfully!!")
	else:
		print("Delete operation canceled !!")
	# commit our command
	conn.commit()
	#close connection
	conn.close()

def selection(attribut, cle):
	"""
		Select record using WHERE
	"""

	#create DB or Connect to DB
	conn = sqlite3.connect('agent.db')
	#create a cursor
	c = conn.cursor()

	c.execute("SELECT rowid, * from customers WHERE attribut = (?)", (cle,))

	for i in items:
		print(i)
	# commit our command
	conn.commit()
	#close connection
	conn.close()
def select():
	attribut = input("Enter Attribut :")
	cle = input("Enter Cle :")
	selection(attribut, cle)