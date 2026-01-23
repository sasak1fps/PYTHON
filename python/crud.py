from calendar import c
from unittest import result
import mysql.connector

connection = mysql.connector.connect(host='localhost', database='bdyoutube', user='root', password='0000')
cursor = connection.cursor()

#CRUD  


#CREATE

nome_produto = input('Digite o nome do produto: ')
valor = int(input('Digite o valor do produto: '))
comand = f'INSERT INTO vendas (nome_produto,valor) VALUES ("{nome_produto}",{valor})'
try:
    cursor.execute(comand)
    connection.commit()
except mysql.connector.Error as err:
    print(f"Erro ao executar comando: {err}")

try:
    cursor.execute('SELECT * FROM vendas')
    result = cursor.fetchall()
    for row in result:
        print(row)
except mysql.connector.Error as err:
    print(f"Erro ao executar comando: {err}")
#READ 
try:
    cursor.execute('SELECT * FROM vendas')
    result = cursor.fetchall()
    for row in result:
        print(row)
except mysql.connector.Error as err:
    print(f"Erro ao executar comando: {err}")

#UPDATE
print('Digite o nome do produto que deseja alterar o valor: ')
nome_produto = input('Digite o nome do produto: ')
valor = int(input('Digite o valor do produto: '))
comand = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

try:
    cursor.execute(comand)
    connection.commit()
except mysql.connector.Error as err:
    print(f"Erro ao executar comando: {err}")



#DELETE
print('Digite o nome do produto que deseja excluir: ')
nome_produto = input('Digite o nome do produto: ')
comand = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

try:
    cursor.execute(comand)
    connection.commit()
except mysql.connector.Error as err:
    print(f"Erro ao executar comando: {err}")






cursor.close()
connection.close()
