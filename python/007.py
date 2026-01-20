"CONDICOES E LOGICA DE PROGRAMAÇÃO"
"""
nome = str(input("qual é o seu nome? "))
if nome == "Gustavo":
        print("que nome lindo você tem!")
else:
        print("seu nome é tão normal!")
print("bom dia, {}!".format(nome))  

n1 = float(input("digite a primeira nota: "))
n2  = float(input("digite a segunda nota: "))
media = (n1+n2)/2
if media >= 6.0:
        print("sua média foi boa! parabéns!")
else:
        print("sua média foi ruim! estude mais!")   
print("sua média foi {:.1f}".format(media))

"ADIVINHAÇÃO DE NÚMERO"
print("-=-"*20)
numero = int(input("digite um número de 0 a 5: "))
import random
n = random.randint(0,5)
if numero == n :
    print("parabéns! você conseguiu me vencer!")
elif numero >5 or numero <0:
    print("ERRO numero muito alto! eu pensei no número {} e não no {}".format(n, numero))
else:100
    print("Perdeu! eu pensei no número {} e não no {}".format(n, numero))
print("-=-"*20)
"MULTA DE TRANSITO"

print("-x-"*20)
velocidade = float(input("qual é a velocidade atual do carro? "))
if velocidade >80:
    print("você foi multado! você excedeu o limite de velocidade que é de 80km/h")
    multa = (velocidade - 80) *7
    print("você deve pagar uma multa de R$ {:.2f}".format(multa))
else:
    print("tenha um bom dia! dirija com segurança!")
print("-x-"*20)
"PAR OU ÍMPAR"

print("=w="*20)
num = int(input("digite um número inteiro: "))
if num % 2 == 0:
    print("o numero {} É par ".format(num) )
else:
    print("o numero {} é impar ".format(num) )
print("=w="*20)

"VIAGEM PRECO "
distancia = float(input("qual é a distância da sua viagem em km? "))
print("você está prestes a começar uma viagem de {} km".format(distancia))
if distancia <= 200:
    preco= distancia * 0.50
else:
    preco= distancia * 0.45
print("o preço da sua passagem será de R$ {:.2f}".format(preco))
"ano bissexto"
ano  = int(input("digite um ano qualquer ou digite 0 para analisar o ano atual: "))
if ano == 0:
    from datetime import date
    ano = date.today().year
if ano % 4 ==0 and ano % 100 !=0 or ano % 400 ==0:
    print("o ano de {} é bissexto!".format(ano))
else:
    print("o ano de {} não é bissexto!".format(ano))
"MAIOR E MENOR VALOR"
n1 = float(input("digite o primeiro valor: "))
n2 = float(input("digite o segundo valor: "))
if n1 > n2:
    print("o maior valor é {}".format(n1))
elif n2 > n1:
    print("o maior valor é {}".format(n2))
else:
    print("os dois valores são iguais: {}".format(n1))
"AUMENTO SALARIAL"
salario = float(input("qual é o salário do funcionário? R$ "))
if salario >= 1500:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print("o funcionário que ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}".format(salario, novo))

"FORMA UM TRINGULO"
segmento1 = float(input("digite o comprimento do primeiro segmento: "))
segmento2 = float(input("digite o comprimento do segundo segmento: "))  
segmento3 = float(input("digite o comprimento do terceiro segmento: "))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print("os segmentos acima PODEM FORMAR um triângulo!")
else:
    print("os segmentos acima NÃO PODEM FORMAR um triângulo!")

    "COVERTER BASE NUMERICA"
print("=-="*20)
num = int(input("digite um numero inteiro: "))
print("escolha uma das bases para conversão: ")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")
opcao = int(input("sua opcão: "))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opcao ==  3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("opção inválida! tente novamente.")
print("=-="*20)

"COMPARANDO NUMERIOS "
print("<->"*20)
numero1 = int(input("digite o primeiro numero inteiro:"))
numero2 = int(input("digite o segundo numero inteiro:"))
if numero1 > numero2:
    print("o primeiro numero {} é maior que o segundo numero {}".format(numero1, numero2))
elif numero2 > numero1:
    print("o segundo numero {} é maior que o primeiro numero {}".format(numero2, numero1))
else:
    print("os dois numeros são iguais: {}".format(numero1))
print("<->"*20)

"ALISTAMENTO MILITAR"
from datetime import date
print("==="*20)
nascimento = int(input("ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - nascimento
print("quem nasceu em {} tem {} anos em {}".format(nascimento, idade, anoatual))
if idade < 18:
    saldo = 18 - idade
    print("ainda faltam {} anos para o alistamento".format(saldo))
    anoalistamento = anoatual + saldo
    print("seu alistamento será em {}".format(anoalistamento))
elif idade > 18:
    saldo = idade - 18
    print("você já deveria ter se alistado há {} anos".format(saldo))
    anoalistamento = anoatual - saldo
    print("seu alistamento foi em {}".format(anoalistamento))
else:
    print("você deve se alistar IMEDIATAMENTE!")
print("==="*20)
"CLASSIFICANDO MEDIAS"
print("O-O"*20)
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2 )/2
if media < 5.0:
    print("sua média foi {:.1f}. você está REPROVADO.".format(media))
elif media >= 5.0 and media < 7.0:
    print("sua média foi {:.1f}. você está de RECUPERAÇÃO.".format(media))
else:
    print("sua média foi {:.1f}. você está APROVADO.".format(media))
print("O-O"*20)

" CLASSIFICANDO ATLETAS"
from datetime import date
print("###"*20)
anoatual = date.today().year
nascimento = int(input("ano de nascimento do atleta: "))
idade = anoatual - nascimento
print("o atleta tem {} anos.".format(idade))
if idade <= 9:
    print("classificação: MIRIM")
elif idade <= 14:
    print("classificação: INFANTIL")
elif idade <= 19:
    print("classificação: JUNIOR")
elif idade <= 25:
    print("classificação: SÊNIOR")
else:
    print("classificação: MASTER")

"FORMA UM TRINGULO v2 "
segmento1 = float(input("digite o comprimento do primeiro segmento: "))
segmento2 = float(input("digite o comprimento do segundo segmento: "))  
segmento3 = float(input("digite o comprimento do terceiro segmento: "))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print("os segmentos acima PODEM FORMAR um triângulo!", end=' ')
    if segmento1 == segmento2 and segmento2 == segmento3:
        print("os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!")
    elif segmento1 != segmento2 and segmento1 != segmento3 and segmento2 != segmento3:
        print("os segmentos acima PODEM FORMAR um triângulo ESCALENO!")
    else: 
        print("os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!")
else:
    print("os segmentos acima NÃO PODEM FORMAR um triângulo!", end=' ')
"INIDICE DE MASSA CORPORAL IMC"
print("%%"*50)
peso = float(input("qual é o seu peso em kg? "))
altura = float(input("qual é a sua altura em metros? "))
imc= peso / (altura **2)
print("o seu índice de massa corporal é de {:.1f}".format(imc))
if imc <18.5:
    print("voce esta abaixo do peso" , end="")
elif 18.5 <= imc <25:
    print("voce esta com o peso ideal" , end="")
elif 25 <= imc <30:
    print("voce esta com sobrepeso" , end="")
elif 30 <= imc <40:
    print("voce esta com obesidade" , end="")
else:
    print("voce esta com obesidade mórbida" , end="")
print("%%"*50)

"SUPERMERCADO PROMOCAO"
print('{:^40}'.format("=====GUANABARA SUPERMERCADO====="))
preco = float(input("qual é o preço da compra? R$ "))
print("FORMAS DE PAGAMENTO")
print("[1] á vista dinheiro/cheque")
print("[2] á vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
opcao = int(input("qual é a opcao de pagamento?"))
if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print("o preço da compra com 10% de desconto é R$ {:.2f}".format(desconto))
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print("o preço da compra com 5% de desconto é R$ {:.2f}".format(desconto))
elif opcao == 3:
    parcela = preco / 2
    print("o preço da compra será parcelado em 2x de R$ {:.2f} SEM JUROS".format(parcela))
    print("o preço total da compra é R$ {:.2f}".format(preco))
elif opcao == 4:

    juros = preco + (preco * 20 / 100)
    parcela = int(input("quantas parcelas? "))
    valor = juros / parcela
    print("o preço da compra com 20% de juros é R$ {:.2f}".format(valor))
    print("o preço total da compra é R$ {:.2f}".format(juros))
else:
    print("opção inválida de pagamento. tente novamente.")

print('{:^40}'.format("=====GUANABARA SUPERMERCADO====="))

"""