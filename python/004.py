"OPERAÇÕES ARITMÉTICAS"
"""
soma = 10 + 5;  
subtracao = 10 - 5;
multiplicacao = 10 * 5;
divisao = 10 / 5;   
expoente = 10 ** 2;  
modulo = 10 % 3;

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)  
print("Exponenciação:", expoente)
print("Módulo:\n", modulo)    

n1= int(input("Digite um numero: "))
n2= int(input("Digite outro numero: "))
print("A soma é:", n1 + n2)
print("A subtração é:", n1 - n2)    
print("A multiplicação é:", n1 * n2)
print("A divisão é:", n1 / n2)              
print("A exponenciação é:", n1 ** n2)
print("A módulo é:\n\n", n1 % n2)

n = int(input("Digite um numero : "))
antecessor = n - 1
sucessor = n + 1
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print("O antecessor de", n, "é\n", antecessor)
print("O sucessor de", n, "é\n", sucessor)    
print("O dobro de", n, "é\n", dobro)
print("O triplo de", n, "é\n", triplo)  
print("A raiz quadrada de", n, "é\n", raiz)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média entre {}, e {} é igual a {:.2f}\n".format(nota1, nota2, media))

"conversor_de_medidas"
metros= float(input("Digite um valor em metros: "))
print("O valor em quilômetros é:", metros / 1000)
print("O valor em hectômetros é:", metros / 100)
print("O valor em decâmetros é:", metros / 10)
print("O valor em metros é:", metros)
print("O valor em decímetros é:", metros * 10)
print("O valor em centímetros é:", metros * 100)
print("O valor em milímetros é:", metros * 1000)

"tabuada"
x = int(input("Digite um numero para ver sua tabuada: "))
print("-" * 12)
print("{} x {:2} = {}".format(x, 1, x * 1))     
print("{} x {:2} = {}".format(x, 2, x * 2))
print("{} x {:2} = {}".format(x, 3, x * 3)) 
print("{} x {:2} = {}".format(x, 4, x * 4))
print("{} x {:2} = {}".format(x, 5, x * 5))
print("{} x {:2} = {}".format(x, 6, x * 6))
print("{} x {:2} = {}".format(x, 7, x * 7))
print("{} x {:2} = {}".format(x, 8, x * 8))
print("{} x {:2} = {}".format(x, 9, x * 9))
print("{} x {:2} = {}".format(x, 10, x * 10))
print("-" * 12)

"CONVERSAO DE VALORES"
real = float(input("Digite um valor em reais: R$"))
dolar = real / 5.25 
print("O valor de R${:.2f} em dolares é: U${:.2f}".format(real, dolar))

"pintor de paredes"
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))  
area = largura * altura
tinta = area / 2    
print("A área da parede é de {:.2f} metros quadrados.".format(area))
print("A quantidade de tinta necessária para pintar a parede é de {:.2f} litros.".format(tinta))

"CALCULADORA DE DESCONTOS E JUROS"
preco = float(input("Digite o preço do produto: R$"))
desconto = preco * float(input("Digite a porcentagem de desconto (ex: 0.10 para 10%): "))
juros = preco * float(input("Digite a porcentagem de juros (ex: 0.10 para 10%): "))
print("O preço do produto com desconto é: R${:.2f}".format(desconto))
print("O preço do produto com juros é: R${:.2f}".format(juros))

"AUMENTO SALARIAL"
salario = float(input("Digite o salário atual: R$"))
aumento = salario * float(input("Digite a porcentagem de aumento (ex: 0.10 para 10%): "))
novo_salario = salario + aumento
print("O novo salário com aumento é: R${:.2f}".format(novo_salario))

"TEMPERATURA EM CELSIUS PARA FAHRENHEIT"
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32   
print("A temperatura em Fahrenheit é: {:.2f}°F".format(fahrenheit))
"""
"ALUGUEL DE CARROS"
dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))   
preco_total = (dias * 60) + (km * 0.15)
print("O preço total do aluguel do carro é: R${:.2f}".format(preco_total))