
"modulos"
"""

import 016.py # type: ignore

    def aumentar(valor, porcentagem):
        return valor + (valor * porcentagem / 100)
    def diminuir(valor , porcentagem):
        return valor - (valor * porcentagem / 100)
        
    def dobro(valor):
        return valor * 2

    def metade(valor):
        return valor / 2

    print(aumentar(100, 10))
    print(diminuir(100, 10))
    print(dobro(100))   
    print(metade(100))

    numero = int(input("Digite um valor: "))
    porcentagem = int(input("Digite a porcentagem: "))
    print("O valor aumentado em {}% é: {}".format(porcentagem, aumentar(numero, porcentagem)))
    print("O valor diminuído em {}% é: {}".format(porcentagem, diminuir(numero, porcentagem)))
    print("O dobro do valor é: {}".format(dobro(numero)))
    print("A metade do valor é: {}".format(metade(numero)))
"FORMATANDO MOEDAS "

def aumentar(valor, porcentagem):
    return valor + (valor * porcentagem / 100)
def diminuir(valor , porcentagem):
    return valor - (valor * porcentagem / 100)
    
def dobro(valor):
    return valor * 2

def metade(valor):
    return valor / 2

def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')

print(aumentar(100, 10))
print(diminuir(100, 10))
print(dobro(100))   
print(metade(100))

numero = int(input("Digite um valor: "))
porcentagem = int(input("Digite a porcentagem: "))
print("O valor aumentado em {}% é: {}".format(porcentagem, moeda(aumentar(numero, porcentagem))))
print("O valor diminuído em {}% é: {}".format(porcentagem, moeda(diminuir(numero, porcentagem))))
print("O dobro do valor é: {}".format(moeda(dobro(numero))))
print("A metade do valor é: {}".format(moeda(metade(numero))))

"""


