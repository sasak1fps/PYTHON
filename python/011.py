"APRENDENDO SOBRE TUPLAS "
"TUPLAS SÃO IMUTÁVEIS -> NÃO PODEM SER ALTERADAS -> ()"
"""
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche),print(type(lanche)),print(lanche[1]),print(lanche[1:3])
for comida in lanche:
  print(f'Eu vou comer {comida}')
for comida in range(0, len(lanche)):
  print(f'Eu viu comer {lanche[comida]}')
for pos, comida in enumerate(lanche):
  print(f'Eu viu comer {comida} na posição {pos}')

  print(lanche)
  print(sorted(lanche))

  a = (2, 5, 4)
  b = (5, 8, 1, 2)
  c = a + b
  print(c)
  print(c.count(5)) #quantas vezes aparece o 5
  print(c.index(8)) #qual a primeira vez que aparece o 8


"LEITOR POR EXTENSO - TUPLAS "
extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte'
)
while True:
  num = int(input('Digite um número entre 0 e 20: '))
  print (f'Voce digitou o número {extenso[num]}')
  resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
  if resp in 'N':
    break

"TIMES DE FUTEBOL"
print("{:=^40}".format("BRASILEIRÂO"))
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'Sao Paulo',
         'Internacional', 'Fluminense', 'Botafogo', 'Atletico-MG', 'Goias', 'Bahia',
         'Cruzeiro', 'Ceara', 'Corinthians', 'Chapecoense', 'Vasco', 'Paranaense',
         'Sport', 'Avai')
for time in times:
  print(time)
print(sorted(times[0:5]))
print(sorted(times[-4:]))
print(f'Ordem alfabetica: {sorted(times)}')
print(f"Chapecoense está na {times.index('Chapecoense')+1 }ªposição")

"MAIOR E MENOR VALOR NA TUPLA"
import random

num = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
       random.randint(1, 10), random.randint(1, 10))
for n in num:
  print(f"{n}", end=" ")
print(f"\nO maior valor sorteado foi: {max(num)}")
print(f"O menor valor sorteado foi: {min(num)}")

"ARMAZENAR VALORES EM UMA TUPLAS"
tupla = ()
pares = 0
for contagem in range(0, 5):
  numero = (int(input("Digite um valor: ")))
  tupla += (numero,)
  if numero % 2 == 0:
    pares += 1
    pares == tupla.index(numero)

print(f"Os valores digitados foram: {tupla}")
print(f"O maior valor digitado foi: {max(tupla)}")
print(f"O menor valor digitado foi: {min(tupla)}")
print(f"O numero 9 apareceu {tupla.count(9)} vezes")
print(f"O primeiro valor 3 apareceu na posição {tupla.index(3)+1}")
print(f'Os numeros pares digitados foram: {pares}')
print("*" * 40)
"LISTA DE PRECOS COM TUPLAS"
print("{:=^40}".format("LISTA DE PREÇOS"))
print("*" * 40)
produtos = ('lapis ' , 'caneta', 'borracha', 'caderno', 'livro', 'mochila', 'computador', 'mouse', 'teclado', 'monitor')
precos = (1.75, 2.00, 4.00, 15.00, 20.00, 120.00, 1800.00, 100.00, 80.00, 800.00)
for posicao in range(0, len(produtos)):
  print(f"{produtos[posicao]}: R${precos[posicao]:.2f}")

print("*" * 40)
print ("{:=^40}".format("LISTA DE PREÇOS 2.0 COM TUPLAS"))
print("*" * 40)
mercadoria = ('lapis ' , 1.75, 'caneta', 22, 'borracha',2 , 'caderno', 33 ,'livro', 56 ,'mochila', 500 ,'computador', 1500, 'mouse', 15 , 'teclado', 25 ,'monitor' , 200)
for position in range(0 , len(mercadoria)):
  if position % 2 == 0:
    print(f"{mercadoria[position]:-<30}", end = '')
  else:
    print(f"R${mercadoria[position]:>7.2f}")
  """

"CONTAGEM DE VOGAIS COM TUPLA"
palavras =('aprender' , 'programsr', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for posicao in range(0, len(palavras)):
  print(f"\n Na palavra {palavras[posicao]} temos" , end=' ')
  for letra in palavras[posicao]:
    if letra.lower() in 'aeiou':
      print(letra, end='')













