"ESTRUTURA DE LACOS DE REPETICAO"
"""
valorinicial = int(input("digite o valor INICIAL: "))
valorfinal = int(input("Digite o valor FINAL: " ))
valordepassos = int(input("digite o valor dos passos: "))
for i in range(valorinicial,valorfinal + 1 , valordepassos ):
    print(i)
n = int(input("digite um numero"))
for c in range(0, n + 1):
    print(c)    
s = 0 
for c in range(0,3):
    n = int(input("digite um numero:"))
    s += n
print("a soma de todos os valores é {}".format(s),end='')

"CONTAGEM REGRESSIVA"
from time import sleep
for c in range (10,0,-1):
    print(c)
    sleep(1)
print("Feliz ano novo!")    

"CONTAGEM DE PARES"
for contador in range(2, 51, 2):
    print(contador, end=' ')
print("Fim da contagem de pares")

"NUMEROS IMPARES"
for contador in range(1, 51, 2):
    print(contador, end=' ')
print("Fim da contagem de impares")

"CALCULAR A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 A 500"
soma = 0
for contador in range (1, 501 , 2):
    if contador % 3 == 0:
        soma += contador 
        print(contador , end=' ')
print(" A SOMA DE TODOS OS VALORES É: {}".format(soma))
print("Fim da contagem")

"TABUADA"
numero = int(input("digite um numero: "))
for contador in range(1, 11):
    print("{} x {} = {}".format(numero, contador, numero * contador, end=' ')) 

"SOMA DOS NUMEROS PARES"
soma = 0 
cont = 0
for Contador in range (1, 7):
    numero = int(input("digite um numero: "))
    if numero % 2 == 0:
        soma += numero 
        cont += 1
print("A soma dos numeros pares é: {}".format(soma))
print("Foram encontrados {} numeros pares".format(cont))

"10 TERMOS DE UMA PA"
primeiro =int(input("digite o primeiro termo: "))
razao = int(input("digite a razao: "))
decimo = primeiro + (10 - 1) * razao
for contador in range (primeiro, decimo + 1, razao):
    print(contador, end=' -> ')
print("ACABOU")

"NUMERO PRIMO"
numero = int(input("digite um numero:"))
total = 0
for contador in range (1, numero + 1 , 1 ):
    if numero % contador == 0:
        print("\033[33m \033[m",end=' -> ')
        total += 1
    else:
        print("\033[31m  \033[m",end=' -> ')
    print("{}" .format(contador),end=' ')
print("Fim da contagem")
print("O numero {} foi dividido {} vezes".format(numero, total))
if total == 2:
    print("O numero {} é primo".format(numero))
else:
    print("O numero {} não é primo".format(numero))

"DETECTOR DE PALINDROMO"
frase = input("digite uma frase: ").strip().upper().split()
junto = ''.join(frase)
inverso = ''
'inverso = junto[::-1]' # tambem pode fazer so com isso 

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

"GRUPO DE MAIORIDADE"
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1 , 8):
    ano = int(input("digite o ano de nascimento: "))
    idade = atual - ano 
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))


"maior e menor da sequencia"
maior = 0
menor = 0
for pessoa in range (1, 6):
    peso = float(input("digite o peso da {} pessoa: ".format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso 
        if peso < menor:
            menor = peso 
print("O maior peso é {}".format(maior))
print("O menor peso é {}".format(menor))


"""

"ANALISADOR DE PESSOAS"
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for contador in range (1, 5):
    nome = input("digite seu nome: ").strip().upper()   
    idade = int(input("digite sua idade: "))
    sexo = input("digite seu sexo [M/F]: ").strip().upper()[0]  
    somaidade += idade
    if contador == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4

print("A media de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho é {} com {} anos".format(nomevelho, maioridadehomem))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))   
