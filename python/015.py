" APRENDENDO FUNCOES  DEF__"
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