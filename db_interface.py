import database

#database.create_db()
def main():

	print(""" 
		WELCOME TO STUDENTS DATABASE
		############################
		Select Operation :
		(1) for Add Record
		(2) for Show Records
		(3) for Delete Records
		""")
	operation = input("Enter your Choice : ")
	if operation == "1":
		database.add_record()
	elif operation == "2":
		database.show_all()
	elif operation == "3":
		#database.delete_one(id)
		print("Please Contact DataBase Admonistrator for this Operation")
	elif operation == "5":
		#database.select()
		print("Please Contact DataBase Admonistrator for this Operation")
	elif operation == "1":
		print("Please Contact DataBase Admonistrator for this Operation")
	else:
		print("Please Select the correct Option, Try again !!")




	



main()
#database.add_record()
#database.show_all()
#database.delete_one(id)