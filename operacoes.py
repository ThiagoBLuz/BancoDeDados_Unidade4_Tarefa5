import mysql.connector
from mysql.connector import errorcode
import conexao

#instalação do mysql connector
#pip install mysql-connector-python

#capturando a conexao
cursor = conexao.db_connection.cursor()

def consulta_dados():
  sql = ("SELECT ID_Agencia, Nome, Cidade FROM Agencia")
  cursor.execute(sql)
  for (ID_Agencia, Nome, Cidade) in cursor:
    print(ID_Agencia, Nome, Cidade)
  print("\n")

def insere_dados():
  print("-------INSERINDO DADOS-------")
  sql = "INSERT INTO Agencia (ID_Agencia, Nome, Cidade) VALUES (%s , %s, %s)"
  values = (4, "Agência Leste", "Baturité")
  cursor.execute(sql, values)
  print(cursor.rowcount, "Registro Inserido")

def atualiza_dados():
  sql = ("UPDATE Agencia SET Nome = 'Agência Oeste' WHERE ID_Agencia=4")
  cursor.execute(sql)
  print(cursor.rowcount, "Registro Atualizado")
  print("\n")

def deleta_dados():
  sql = ("DELETE FROM Agencia WHERE ID_Agencia=3")
  cursor.execute(sql)
  print(cursor.rowcount, "Registro Deletado")
  print("\n")


consulta_dados()



cursor.close()
conexao.db_connection.commit()
conexao.db_connection.close()

