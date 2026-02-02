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

"FUNCAO FATORIAL"
def fatorial(num = int(input('Digite um numero para calcular o fatorial: ')), show = False):
    f = 1
    for c in range (num , 0 , -1):
        if show:
            print(c , end = '')
            if c > 1:
                print(' x ' , end = '')
            else:
                print(' = ' , end = '')
        f *= c
    return f
print(fatorial(5 , show = True))

"FICHA DEE JOGADOR"

def ficha(nome = str(input('Nome do jogador: ')), gols = str(input('Número de gols: '))):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.strip() == '' or not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato')
ficha()


"LEIA NUMEROS "
from calendar import c


def leiaInt(msg):
    try:
        while True:
            n = input(msg)
            if n.isnumeric():
                return int(n)
            else:
                print('ERRO! Digite um número inteiro válido.')
                continue
    except (ValueError, TypeError):
        print('ERRO! Digite um número inteiro válido.  1')
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')

"ANALISANDO   e GERANDO DICIONARIOS"
def notas(*n , sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict ()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['media'] = sum(n) / len(n)
    if sit:
        if r ['media'] >= 7:
            r ['situação'] = 'BOA'
        elif r ['media'] >= 5:
            r ['situação'] = 'RAZOÁVEL'
        else:
            r ['situação'] = 'RUIM'
    return r
resp = notas(5.5, 2.5, 9.5, sit = True)
print(resp)
'''

"INTERARIVE HELPING IN PYTHON "
def ajuda(com):
   while True:
        if com.upper() == 'FIM':
            print('Até logo!')
            break
        else:
            help(com)
        com = str(input('Digite a função ou biblioteca que deseja ajuda: '))
ajuda(str(input('Digite a função ou biblioteca que deseja ajuda: ')))
