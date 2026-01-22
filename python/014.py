"DICTIONARIES"
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)
print(thisdict1.keys())
print(thisdict1.values())

brazil=[]
state = {"SP": "Sao Paulo"}
state1 ={"RJ": "Rio de Janeiro"}
brazil.append(state)
brazil.append(state1)
print(brazil)
print(brazil[1]["RJ"])

State = []
brasil = list()
for c in range(0, 3):
  state = {}
  state["uf"] = str(input("Unidade Federativa: "))
  state["sigla"] = str(input("Sigla do Estado: "))
  brasil.append(state.copy())
for c in range(0, 3):
  for k, v in brasil[c].items():
    print(f'{k} = {v}')


"BOLETIM"
aluno = {}
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f'Media de {aluno["nome"]}: '))
if aluno["media"] >= 7.0 and aluno["media"] <= 10.0:
  aluno["situacao"] = "Aprovado"
elif 5.0 <= aluno["media"] < 7.0:
  aluno["situacao"] = "Recuperacao"
elif aluno["media"] > 10.0:
  aluno["situacao"] = "Nota inválida" 
else:
  aluno["situacao"] = "Reprovado"
print('-=' * 30)
for k, v in aluno.items():
  print(f' - {k} é igual a {v}')

"JOGO DE DADO"
resultado = []
from operator import itemgetter
import random

jogo = {
  'jogador1': random.randint(1, 6),
  'jogador2': random.randint(1, 6),
  'jogador3': random.randint(1, 6),
  'jogador4': random.randint(1, 6)}

for k, v in jogo.items():
  print(f'{k} tirou {v}')



raking = dict()
raking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(raking):
  print(f'{i+1} lugar: {v[0]} com {v[1]}')
  
"CADASTRO DE TRABLHO"
from datetime import date


trabalhador = {}
trabalhador["nome"] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
trabalhador["idade"] = date.today().year - nascimento
trabalhador["ctps"] = int(input("Carteira de trabalho: (0 nao tem)"))
if trabalhador["ctps"] != 0:
  trabalhador["contratacao"] = int(input("Ano de contratação: "))
  trabalhador["salario"] = float(input("Salário: "))
  trabalhador["aposentadoria"] = (trabalhador["contratacao"] + 35) - nascimento
print('-=' * 30)
for k, v in trabalhador.items():
  print(f' - {k} é igual a {v}')


"CADASTRAR JOGADOR DE FUTEBOL"

jogador = dict()
partidas = list()
jogador["nome"] = str(input("Nome do jogador: "))
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for c in range(0 , total):
    partidas.append(int(input("QUANTIDADE DE GOLS NA PARTIDA {} : ".format(c+1))))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i ,v in enumerate(jogador["gols"]):
    print(f"Na partida {i+1}, fez {v} gols.")
print(f"O jogador {jogador['nome']} fez um total de {jogador['total']} gols.")

"UNINDO DICIONARIO E LISTA"

while True:
  nome = str(input('Digite seu nome: '))
  idade = int(input('Digite sua idade: '))
  sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
  

  if sexo not in ['M', 'F']:
    print('Sexo inválido! Por favor, digite novamente!')
  else:
    cadastro = {'nome': [nome], 'idade': [idade], 'sexo': [sexo]}
    


  resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
  if resp in 'Nn':
    break
  elif resp not in 'Ss':
    print('Resposta inválida! Por favor, digite novamente!')
  else:
    continue


for k, v in cadastro.items():
  print(f'{k}: {v}')
  print('-=' * 30)

print('<< ENCERRADO >>')
galera = list()
pessoa = dict()
soma = media = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('ERRO! Por favor, digite apenas M ou F.')
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())  
  while True:
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'SN':
      break
    print('ERRO! Resposta inválida.')
  if resp in 'N':
    break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.', end='')
media = soma / len(galera)
print(f'A media de idade e de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
  if p['sexo'] in 'Ff':
    print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estao acima da media: ')
for p in galera:
  if p['idade'] >= media:
    print('    ', end='')
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')
  '''
"APRIMORANDO DICIONARIOS"
time = list()
jogador = {}
partidas = []

while True:
  jogador.clear()
  jogador["nome"] = str(input("Nome do jogador: "))
  total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
  partidas.clear()
  for c in range(0 , total):
      partidas.append(int(input(f"Quantidade de gols na partida {c+1}: ")))
  jogador["gols"] = partidas[:]
  jogador["total"] = sum(partidas)
  time.append(jogador.copy())
  while True:
      resp = str(input("Quer continuar? [S/N] ")).upper()[0]
      if resp in "SN":
          break
      print("ERRO! Resposta inválida.")
  if resp == "N":
      break

  print("-=" * 30)
for k , v in enumerate(time):
  print(f'{k:>3}', end = " ")
for d, i in v.items():
  print(f"{str(i):<15}", end = " ")
  print()
print("-=" * 30)
  
  
  
for i, v in enumerate(jogador["gols"]):
  print(f"    => Na partida {i+1}, fez {v} gols.")
  print(f"Foi um total de {jogador['total']} gols.")
while True:
   busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
   if busca == 999:
       break
   if busca >= len(time):
       print(f"ERRO! Jogador {busca} não cadastrado.")
   else:
       print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
       for i, v in enumerate(time[busca]["gols"]):
           print(f"    => Na partida {i+1}, fez {v} gols.")
           print(f"Foi um total de {time[busca]['total']} gols.")
