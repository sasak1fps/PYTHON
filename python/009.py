"ESTRUTURA DE REPETIÇÃO - WHILE"
""" 
c = 1
while c <= 10:
    print(c)
    c += 1
    if c == 11:
        print("FIM")
   


"VALIDACAO DE DADOS"
sexo = 'A'.strip().upper() 
while sexo not in 'MF':
    sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input("Dados inválidos! Por favor, informe seu sexo [M/F]: ")).strip().upper()[0]
    else:
        break
print("Sexo {} registrado com sucesso!".format(sexo))

"JOGO DA ADIVINHAÇÃO"
from random import randint
sorteado = randint(0, 10)
palpite = 0
numeroescolhido = int(input("Digite um número aleatório de 0 a 10: "))
while numeroescolhido != sorteado:
    if sorteado < numeroescolhido:
        print("O número sorteado é menor que o seu palpite.")
    elif sorteado > numeroescolhido:
        print("O número sorteado é maior que o seu palpite.")
    numeroescolhido = int(input("Número incorreto! Tente novamente: "))
    palpite += 1

print("Parabéns! Você acertou o número sorteado em {} tentativas:".format(sorteado, palpite))


"MENU DE OPÇÕES"
from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
while True:
    print('-'*20)
    print('MENU PRINCIPAL')
    print('-'*20)
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos Números')
    print('5 - Sair do Programa')
    print('-'*20)
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print('Você escolheu somar!')
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print('Você escolheu multiplicar!')
        print(f'{num1} * {num2} = {num1 * num2}')
    elif opcao == 3:
        print('Você escolheu maior!')
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}')
        else:
            print(f'{num1} e {num2} são iguais')
    elif opcao == 4:
        print('Você escolheu novos números!')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        break
    else:
        print('Opção inválida! Tente novamente.')    
    print('-'*20)   

"CALCULO DE FATORIAL"
while True:
    numero = int(input("Digite um número para calcular seu fatorial (ou digite -1 para sair): "))
    if numero == -1:
        print("Programa encerrado.")
        break
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i   
    print(f"O fatorial de {numero} é {fatorial}")

# Usando While
n1 = int(input('Digite um número para saber o fatorial: '))
f1 = 1
c1 = n1
while c1 > 1:
    f1 *= c1
    c1 -= 1
print(f'O resultado de {n1}! é  {f1}')

# Usando for
n2 = int(input('Digite um número para saber o fatorial: '))
f2 = 1
for i in range(1, n2 + 1):
    f2 *= i
print(f'O resultado de {n2}! é {f2}')

# Usando math
from math import factorial
n3 = int(input('Digite um número para saber o fatorial: '))
print(f'O resultado de {n3}! é {factorial(n3)}')



"PROGRESSÃO ARITMÉTICA USANDO WHILE"
print("Gerador de PA")
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razao
    cont += 1
print("FIM")    



"PROGRESSÃO ARITMÉTICA USANDO WHILE"
print("Gerador de PA")
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print("FIM") 
print("Progressão finalizada com {} termos mostrados.".format(total))


"SEQUENCIA DE FIBONACCI"
print("Sequência de Fibonacci")
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(" -> FIM")    

print("Sequência de Fibonacci")
n = int(input("Quantos termos você quer mostrar? "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    proximo = a + b
    a = b
    b = proximo
print("\nFIM")



"SOMADOR DE VALORES COM FLAG"
soma = 0
contador = 0
while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    soma += num
    contador += 1
print(f"A soma dos {contador} valores a soma  deles foi {soma}")
"""

"MAIOR E MENOR VALORES COM WHILE"
maior = 0
menor = 0
soma = quantidade =  media = 0
while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    if quantidade == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    quantidade += 1
media = soma / quantidade
    
print(f"O maior valor foi {maior} e o menor foi {menor}")
print(f"A soma dos valores foi {soma} e a média foi {media}")

