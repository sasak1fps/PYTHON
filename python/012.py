"APRENDENDO LISTAS EM PYTHON "
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(0)
num.remove(1)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
for c,v in enumerate(num):
  print(f'Na posição {c} encontrei o valor {v}!')
valores = list()
for valor in range(0,5):
  valores.append(int(input('Digite um valor: ')))
a = [1 , 2 ,3 ,4 ,5]
b = [1 , 2 ,3 ,4 ,5]
b = a #b e a apontam para o mesmo local na memória
b = a[:] #b uma cópia da a 
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


"MAIOR E MENOR VALOR NA LISTA  "
lista = []
for c, v in enumerate(range(0, 5)):
  n = int(input("Digite um valor: "))
  if c == 0 or n > lista[-1]:
    lista.append(n)
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        break
      pos += 1
print(f"Os valores digitados foram: {lista}")
print(f"O maior valor digitado foi: {max(lista)} na posicao {lista.index(max(lista))}")
print(f"O menor valor digitado foi: {min(lista)} na posicao {lista.index(min(lista))}")

lista = []

for i in range(5):
    n = int(input("Digite um valor: "))

    lista.append(n)      # adiciona o número na lista
    lista.sort()         # organiza a lista em ordem crescente

print("Os valores digitados foram:", lista)
print("O maior valor digitado foi:", max(lista), "na posição", lista.index(max(lista)))
print("O menor valor digitado foi:", min(lista), "na posição", lista.index(min(lista)))

"VALORES UNICOS EM UMA LISTA "
lista = []
while True:
  n = int(input("Digite um valor: \n"))
  if n not in lista:
    lista.append(n)
  else:
    print("Valor duplicado! Não vou adicionar...")
  print("QUER CONTINUAR [S/N]?")
  resp = str(input()).strip().upper()[0]
  if resp in 'N':
    break
print(f"Os valores digitados foram: {sorted(lista)}")

"LISTA ORDENADA SEM REPETICAO "

lista = []
maior =  menor = 0
while True:
  n = int(input("Digite um valor: \n"))
  if n not in lista:
    lista.append(n)
    if len(lista )== 1:
      maior = menor = n
    elif len(lista) > 1:
      if n > maior:
        maior = n
        print(f'adicionado ao final da lista')
      if n < menor:
        menor = n
        print(f'adicionado na posição{lista.index(n)} da lista')
  else:
    print("Valor duplicado! Não vou adicionar...")
  print("QUER CONTINUAR [S/N]?")
  resp = str(input()).strip().upper()[0]
  if resp in 'N':
    break
print(f"Os valores digitados foram: {sorted(lista)}")

list = []
for c in range(0,5):
  n = int(input("Digite um valor: "))
  if c == 0 or list[-1] < n:
    list.append(n)
  else:
    pos = 0
    while pos < len(list):
      if n <= list[pos]:
        list.insert(pos, n)
        break
      pos += 1
print(f"Os valores digitados foram: {list}")


"ANALISANDO VALORES NA LISTA"
lista = []
while True:
  n = int(input("Digite um valor: \n"))
  if n not in lista:
    lista.append(n)
  else:
    print("Valor duplicado! Não vou adicionar...")
  print("QUER CONTINUAR [S/N]?")
  resp = str(input()).strip().upper()[0]
  if resp in 'N':
    break
print(f'Voce digitou {len(lista)} elementos')
print(f"Os valores digitados em ordem decrescente foram: {sorted(lista, reverse=True)}")
print(f'O valor 5  parte da lista' if 5 in lista else 'O valor 5 nao parte da lista')
print(f"O maior valor digitado foi: {max(lista)}")
print(f"O menor valor digitado foi: {min(lista)}")


"DIVIDINDO VALORES EM LISTA "
lista = []
pares = []
impares = []
while True:
  n = int(input("Digite um valor: \n"))
  if n not in lista:
    lista.append(n)
  else:
    print("Valor duplicado! Não vou adicionar...")
  print("QUER CONTINUAR [S/N]?")
  resp = str(input()).strip().upper()[0]
  if resp in 'N':
    break
for i, v in enumerate(lista):
  if v % 2 == 0:
    pares.append(v)
  else:
    impares.append(v)

print(f"Os valores digitados foram: {sorted(lista)}")
print(f'os valores pares digitados foram: {sorted(pares)}')
print(f'os valores impares digitados foram: {sorted(impares)}')

'''
"VALIDANDO EXPRESSOES MATEMATICAS"
lista = []
while True:
  expressao = str(input("Digite uma expressão: "))
  if expressao == 'fim':
    break
  else:
    lista.append(expressao)
  print(f'DIGITE  FIM PARA PARAR')

for expressao in lista:
  if expressao.count('(') == expressao.count(')'):
    print('Sua expressao esta correta')
  else:
    print('Sua expressao esta errada')
  















