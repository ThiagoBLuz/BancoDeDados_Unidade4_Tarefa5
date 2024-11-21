import mysql.connector
from mysql.connector import errorcode

try:
	db_connection = mysql.connector.connect(
		host='localhost', 
		user='root', 
		password= '0102', 
		database='Banco'
		)
	print("Banco de Dados conectado com sucesso!")
	
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Nome de usuário ou senha errado")
	else:
		print(error)
