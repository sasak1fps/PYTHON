"PYTHON ORIENTACAO A OBJETOS"
# Orientacao a Objetos
# POO - Programacao Orientada a Objetos
# Classe - Molde para criar objetos
# Objeto - Instancia de uma classe
# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} esta falando.")
# Criando um objeto
pessoa1 = Pessoa("Joao", 30)
pessoa1.falar() 


class Calculador:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b


def main():
    calc = Calculador()   # Criando o objeto

    print("CALCULADORA")
    print("ESCOLHA UMA OPERACAO")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")

    opcao = int(input("Digite a opcao desejada: "))

    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))

    if opcao == 1:
        resultado = calc.somar(a, b)
    elif opcao == 2:
        resultado = calc.subtrair(a, b)
    elif opcao == 3:
        resultado = calc.multiplicar(a, b)
    elif opcao == 4:
        resultado = calc.dividir(a, b)
    else:
        print("Opcao invalida")
        return

    print(f"O resultado da operacao e: {resultado}")


main()
