"MODULOS"
import math
"""
numero = float(input("dgite um numero: "))
numero2= math.sqrt(numero)
numero3= math.ceil(numero)
numero4= math.floor(numero)
numero5= math.hypot(numero)
numero6= math.pow(numero,2)
numero7= math.sin(numero)
numero8= math.cos(numero)
numero9= math.tan(numero)
print (f"Raiz quadrada: {numero2}\nArredondamento para cima: {numero3}\nArredondamento para baixo: {numero4}\nHipotenusa: {numero5}\nNumero elevado ao quadrado: {numero6}\nSeno: {numero7}\nCosseno: {numero8}\nTangente: {numero9}")
import random
numero10= random.randint(1,10)
print(f"Numero aleatorio entre 1 e 10: {numero10}")
"quebrar um numero"
numero = float(input("digite um numero: "))
print (f"A parte inteira do numero {numero} é {math.trunc(numero)}")
"CATETOS E HIPOTENUSA"
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"O valor da hipotenusa é: {hipotenusa}")

"SENO COSSENO E TANGENTE"
angulo = float(input("Digite o valor do angulo: "))
print(f"O seno do angulo {angulo:2f} é: {math.sin(math.radians(angulo))}")
print(f"O cosseno do angulo {angulo:2f} é: {math.cos(math.radians(angulo))}")
print(f"A tangente do angulo {angulo:2f} é: {math.tan(math.radians(angulo))}")
"SORTEIO DE NOMES"
import random
aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))  
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista) 
print(f"O aluno sorteado foi: {sorteado}")
"EMBARALHAR NOMES"
import random
nome1 = str(input("Digite o nome do primeiro aluno: "))
nome2 = str(input("Digite o nome do segundo aluno: "))      
nome3 = str(input("Digite o nome do terceiro aluno: "))
nome4 = str(input("Digite o nome do quarto aluno: "))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print("A ordem de apresentação será:", lista)
"""
