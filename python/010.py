"APRENDENDO WHILE TRUE"
"""
while True:
    try:
        n = int(input("Digite um número: "))
        if n == 999:
            break 
    except ValueError:
        print("ERRO! Por favor, digite um número inteiro.")  
print(f'o número digitado foi {n}')
print('FIM')

"F strings"
nome = 'Gustavo'
idade = 22
print(f'o {nome} tem {idade} anos')#python 3.6
print("o {} tem {} anos".format(nome, idade))#python 3
print(" o %s tem %d anos" % (nome, idade))#python 2

"NUMEROS COM FLAGS"
quantidade = 0
soma = 0
while True:
    try:
        n = int(input("Digite um número: ([ 999 para parar! ]) "))
        if n == 999:
            break 
    
        quantidade += 1
        soma += n
    except ValueError:
        print("ERRO! Por favor, digite um número inteiro.")                 
print(f'o número digitado foi {n}')
print(f'Foram digitados {quantidade} números e a soma entre eles é {soma}') 

"TABUADO USANDO WHILE TRUE"
n = 0 
while True: 
  n = int(input("Quer ver a tabuada de qual valor? "))
  print("digite 999 para parar.")
  if n == 999:
    break
  for c in range(1, 11):
    print("{} x {:2} = {}\n".format(n, c, n*c))
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")

"PAR OU IMPAR USANDO  WHILE TRUE"
while True:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print("O número {} é PAR".format(n))
    else:
        print("O número {} é IMPAR".format(n))
    resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0];
    if resp in 'N' or 'n':
        break
    else:
     print("ERRO! Por favor, digite um número inteiro.")
print("FIM")


"ANALISANDO DADOS  DE UM GRUPO"
totmaior = 0
totmasc = 0
totfem = 0
while True:
    sexo = ''
    idade = int(input("Digite a idade: "))
    while sexo not in 'MF':
        sexo = input("Digite o sexo [M/F]: ").strip().upper()[0]

    if idade >= 18:
        totmaior += 1
    if sexo == 'M':
        totmasc += 1
    if sexo == 'F' and idade < 20:
        totfem += 1

    resp = ''

    while resp not in 'SN':
        resp = input("Deseja continuar? [S/N]: ").strip().upper()[0]

    if resp == 'N':
        break

print(f"Ao todo tivemos {totmaior} pessoas maiores de idade")
print(f"E também tivemos {totmasc} homens")
print(f"E também tivemos {totfem} mulheres com menos de 20 anos")
print("FIM")

"ESTATISTICAS DO PRODUTO"
print("{:=^40}".format("SUPERLOJA"))
total = mais_1000 = total_produtos = menor = 0
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: R$"))
    total += preco
    total_produtos += 1
    if preco > 1000:
        mais_1000 += 1
    if total_produtos == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print("{:=^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {mais_1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")

"""

"SIMULADOR DE CAIXA ELETRONICO"
print("{:=^40}".format("CAIXA ELETRONICO"))
print ("O CAIXA POSSUI SOMENTE NOTAS DE R$50, R$20, R$10 E R$1")
valor_saque = int(input("digite o valor que deseja sacar: "))
total = valor_saque
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f"total de {total_cedula} cedula(s) de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print("VOLTE SEMPRE!")

print("CAIXA ELETRÔNICO")

valor = int(input("Digite o valor do saque: "))

notas = [50, 20, 10, 1]

for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${nota}")
        valor = valor % nota

print("VOLTE SEMPRE!")


