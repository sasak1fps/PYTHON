"LISTA 2.0  "
'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galerao = [['Joaquim', 19], ['Maria', 22] , ['Pedro', 25] , ['Ana', 19]]
print(galerao[0][0])
g = []
dado = []
for c in range(0, 3):
  dado.append(str(input('Digite o nome: ')))
  dado.append(int(input('Digite a idade: ')))
  g.append(dado[:])
  dado.clear()
print(g)
"LISTAS COMPOSTAS E ANALISE DE DADOS "
nome = []
lista = []
maispesada = menospesada = 0

while True:
  nome.append(str(input('Digite o nome: ')))
  nome.append(float(input('Digite o peso: ')))
  lista.append(nome[:])
  nome.clear()
  maispesada = max(lista, key=lambda x: x[1])
  menospesada = min(lista, key=lambda x: x[1])
  resp = ''
  resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
  if resp in 'Nn':
    break

print(f'Foram cadastrados {len(lista)} pessoas')
print(f'O maior peso foi de {maispesada[1]}kg. Peso de {maispesada[0]}\n')
for c in lista:
  if c[1] == maispesada[1]:
    print(f'{c[0]}')
print(f'O menor peso foi de {menospesada[1]}kg. Peso de {menospesada[0]}\n')
for c in lista:
  if c[1] == menospesada[1]:
    print(f'{c[0]}')
"LISTA COM PARES E IMPARES"
lista_pares = []
lista_impares = []
lista_pares_impares = []
for c in range(0, 7):
  n = int(input('Digite um valor: '))
  if n % 2 == 0:
    lista_pares.append(n)
  else:
    lista_impares.append(n)
  lista_pares_impares.append(n)
print(f'Os valores pares digitados foram: {sorted(lista_pares)}')
print(f'Os valores impares digitados foram: {sorted(lista_impares)}')
print(f'Os valores digitados foram: {sorted(lista_pares_impares)}')

numero = [ [] , [] ]
valor = 0
for c in range(1,8):
  valor = int(input(f'Digite o {c} valor: '))
  if valor % 2 == 0:
    numero[0].append(valor)
  else:
    numero[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(numero[0])}')
print(f'Os valores impares digitados foram: {sorted(numero[1])}')

"MATRIZ COM LISTA"
matriz = []
for c in range(0,9):
  n = int(input(f'Digite o {c} valor: '))
  if c % 3 == 0:
    matriz.append([n])
  else:
    matriz[c//3].append(n)
print(matriz)

matriz1 = []
for l in range(0,3):
  n1 = int (input(f'Digite o {l} valor: '))
  matriz1.append([n1])
  for c in range(1,3):
    n2 = int(input(f'Digite o {c} valor: '))
    matriz1[l].append(n2)
print(matriz1)


matriz2 = [ [] , [] , [] ]
for l in range(0,3):
  for c in range(0,3):
    n = int(input(f'Digite um valor para posicao [{l},{c}]: '))
    matriz2[l].append(n)
print(matriz2)
for l in range(0,3):
  for c in range(0,3):
    print(f'[{matriz2[l][c]:^5}]', end='')
  print()
"MATRIZ 2.0"
matriz = [ [ ] , [ ] , [ ] ]
spar = scol = 0
for l in range(0,3):
  for c in range(0,3):
    n = int(input(f'Digite um valor para posicao [{l},{c}]: '))
    matriz[l].append(n)
print(matriz)
for l in range(0,3):
  for c in range(0,3):
    print(f'[{matriz[l][c]:^5}]', end='')
    if matriz[l][c] % 2 == 0:
      spar += matriz[l][c]
  print()
print("A soma dos valores pares é: {}".format(spar))
for l in range(0,3):
  scol += matriz[l][2]
print("A soma dos valores da terceira coluna é: {}".format(scol))
for c in range(0,3):
  if c == 0:
    maior = matriz[1][c]
  elif matriz[1][c] > maior:
    maior = matriz[1][c]
print("O maior valor da segunda linha é: {}".format(maior))
"MEGA SENA"
from time import sleep
import random


jogos = [];
jogo = [];
quant = int(input('Quantos jogos voce quer que eu sorteie? \n'))
tot = 1
while tot <= quant:
  cont = 0
  while True:
    num = random.randint(1, 60)
    if num not in jogo:
      jogo.append(num)
      cont += 1
    if cont >= 6:
      break
  jogo.sort()
  jogos.append(jogo[:])
  jogo.clear()
  tot += 1
print(f'-=' * 3, f'SORTEANDO {quant} JOGOS', f'-=' * 3)
for i, l in enumerate(jogos):
  print(f'Jogo {i + 1}: {l}')
  sleep(2)
print(f'-=' * 5, '< BOA SORTE! >', f'-=' * 5)

'''
"Boletim composto"
ficha = list()
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = str(input('Quer continuar? [S/N]'))
  if resp in 'Nn':
    break
print('-=' * 30)
print(f'{"No.":<4} {"NOME":<10} {"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
  print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
  print('-' * 35)
  opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if opc == 999:
    break
  if opc <= len(ficha) - 1:
    print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')











































