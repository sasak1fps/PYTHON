"MANIPULAÇÃO DE TEXTOS" 
"""
frase = "Curso em Vídeo Python"
print (frase[3])
print (frase[2:13])
print (frase.upper())
print (frase.lower())
print (len(frase))
print (frase.replace("Python", "Android"))
print (frase.find("Vídeo"))
print (frase.split())
"analise de textos"
nome= str(input("digite seu nome completo: "))
print("anlisando seu nome")
print("seu nome em maiusculas é: {}".format(nome.upper()))
print("seu nome em minusculas é: {}".format(nome.lower()))
print("seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
separa= nome.split()
print("seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))
print("seu ultimo nome é {} e ele tem {} letras".format(separa[len(separa)-1], len(separa[len(separa)-1])))

"SEPARADOR DE DIGITOS"
num = int(input("digite um numero de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("analisando o numero ".format(num))
print("unidade: {}".format(u))
print("dezena: {}".format(d))
print("centena: {}".format(c))
print("milhar: {}".format(m))
"Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome 'SANTO' "
cidade = str(input("digite o nome da cidade: ")).strip()
print(cidade[:5].upper()=="SANTO")

"crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome"
nome = str(input("digite o nome completo: ")).strip()
#print("seu nome tem SILVA? {}".format("SILVA" in nome.upper()))
print("seu nome tem SILVA? {}".format(nome.upper().find("SILVA")!=-1))

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
letra = str(input('Digite a letra que quer análisar: ')).upper().strip()
print(f'A letra {letra} apareceu {frase.count(letra)} vezes')
print(f'A primeira aparição da letra {letra} foi na {frase.find(letra)+1}° posição ')
print(f' aultima vez que a letra {letra} apareceu foi na {frase.rfind(letra)+1}° posição')
"""
"primeiro e ultimo nome"
nome = str(input("digite seu nome completo: ")).strip().upper().split()
print("seu primeiro nome é: {}".format(nome[0]))
print("seu ultimo nome é: {}".format(nome[len(nome)-1]))