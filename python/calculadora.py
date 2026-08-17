class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b == 0:
            return "Erro: Divisão por zero não é permitida."
        return self.a / self.b

    def calcular(self, operacao):
        if operacao == "+":
            return self.somar()
        elif operacao == "-":
            return self.subtrair()
        elif operacao == "*":
            return self.multiplicar()
        elif operacao == "/":
            return self.dividir()
        else:
            return "Operação inválida"

# A função main deve ficar FORA da classe Calculadora
def main():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, /): ")
        
        calculadora = Calculadora(a, b)
        resultado = calculadora.calcular(operacao)
        print(f"O resultado da operação é: {resultado}")
    except ValueError:
        print("Erro: Digite apenas números válidos.")

if __name__ == "__main__":
    main()