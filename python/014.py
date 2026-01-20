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

'''

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
