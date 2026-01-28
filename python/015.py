" APRENDENDO FUNCOES  DEF__"
'''

def linha():
    """Imprime uma linha de 30 caracteres"""
    print('-' * 30)

def titulo(msg):
    """Imprime um t tulo com uma linha acima e ap s"""
    linha()
    print(msg.upper())
    linha()

titulo(str(input('Digite um titulo: ')))

def soma  (a = int(input('Digite um valor: ')) , b = int(input('Digite outro valor: '))):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')
soma()
def CalcularVoto():
    import datetime
    ano = datetime.date.today().year
    idade = ano - nascimento # type: ignore
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif idade >=16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'
    
nascimento = int(input('Digite o ano de nascimento: '))
print(CalcularVoto())

"FUNCAO CALCULAR AREA"
def area(largura, comprimento):
    a = largura * comprimento 
    print(f'A area de um terreno {largura} x {comprimento} = {a}m²')
    return a
print(area(float(input('Largura (m): ')), float(input('Comprimento (m): '))))

"FUNCAO DE PRINT"
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam )
    print(f'  {txt}')
    print('~' * tam )
escreva(str(input('Difite um texto:')))


" funcao contador "
def contador(inicio , fim , passo):
    print(f'Contagem de 1 até 10 de 1 em 1: ')
    for c in range (inicio , fim + 1 , passo):
        print(c , end = ' ')
    print('FIM!')
    print('-' * 20)
    print(f'Contagem de 10 até 0 de 2 em 2: ')
    for c in range (fim , inicio -1 , -passo):
        print(c , end = ' ')
    print('FIM!')
    print('-' * 20)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        for c in range (i , f + 1 , p):
            print(c , end = ' ')
        print('FIM!')
    else:
        for c in range (i , f -1 , -p):
            print(c , end = ' ')
        print('FIM!')
contador(1 , 10 , 1)

"FUNCAO SABER MAIOR"
def maior(*num):
    maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-' * 30)

maior(2, 9, 4, 5, 7)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

"FUCAO PARA SORTEAR E SOMAR"
from random import randint , sample
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end = '')
    for c in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end = '' , flush = True)
    print('PRONTO!')
def somapar(lista):
    s = 0 
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {lista}, temos {s}')
numeros = list()
sorteia(numeros)
somapar(numeros)

'''










