"""
Docstring for jokenpo
"JOKENPO"
print('{:=^50}'.format("=JOKENPO="))
import random
itens = ('Pedra','Papel','Tesoura')
computador = random.randint(0,2)
print("ESCOLHA SUA OPCAO")
print("[0]Pedra")
print("[1]Papel")
print("[2]Tesoura")
opcao = int()
if opcao == 0 and computador == 0 :
    print("empate")
elif opcao == 0 and computador ==1 : 
    print("PERDEU") 
elif opcao == 0 and computador == 2:
    print("GANHo")   
if opcao == 1 and computador == 1 :
    print("empate")
elif opcao == 1 and computador ==2 : 
    print("PERDEU") 
elif opcao == 1 and computador == 0:
    print("GANHo")   
if opcao == 2 and computador == 2 :
    print("empate")
elif opcao == 2 and computador ==0 : 
    print("PERDEU") 
elif opcao == 2 and computador == 1:
    print("GANHo")   
else:
    print("opcao invalida")

print('{:=^50}'.format("JOKENPO"))

import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randrange(3)

print("ESCOLHA SUA OPÇÃO")
for i, item in enumerate(itens):
    print(f"[{i}] {item}")

opcao = int(input("Digite sua escolha: "))

if opcao not in range(3):
    print("Opção inválida.")
else:
    print(f"Você escolheu {itens[opcao]}")
    print(f"O computador escolheu {itens[computador]}")

    if opcao == computador:
        print("Empate")
    elif (opcao - computador) % 3 == 1:
        print("Você ganhou")
    else:
        print("Você perdeu")

"""
import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randrange(3)

print("ESCOLHA SUA OPÇÃO")
for i, item in enumerate(itens):
    print(f"[{i}] {item}")

opcao = int(input("Digite sua escolha: "))

if opcao not in range(3):
    print("Opção inválida.")
else:
    print(f"Você escolheu {itens[opcao]}")
    print(f"O computador escolheu {itens[computador]}")

    if opcao == computador:
        print("Empate")
    elif (opcao - computador) % 3 == 1:
        print("Você ganhou")
    else:
        print("Você perdeu")
