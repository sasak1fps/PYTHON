"TIPOS PRIMITIVOS EM PYTHON"
""" int = 5
float = 5.0
bool = True
str = "ola" """
print(type(int))
print(type(float))  
print(type(bool))
print(type(str))
"""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))    
soma = n1 + n2
print("A soma entre", n1, "e", n2, "é igual a", soma)

n3 = float(input("Digite um numero: "))
n4 = float(input("Digite outro numero: "))      
soma2 = n3 + n4
print("A soma entre", n3, "e", n4, "é igual a", soma2)
"""
booleana1 = input("Digite um valor: ")
print("O valor digitado é", booleana1)
print(type(booleana1))
print(booleana1.isalpha())
print(booleana1.isalnum())
print(booleana1.isspace())
print(booleana1.isupper())
print(booleana1.islower())
print(booleana1.istitle())
print(booleana1.capitalize())
