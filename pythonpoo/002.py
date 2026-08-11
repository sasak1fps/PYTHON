"CONTA BANCARIA EM PYTHON"
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")
    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
# Exemplo de uso
"""
conta = ContaBancaria("João", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()
"""
def main():
    while True:
        dados = input("Digite o nome do titular e o saldo inicial (separados por vírgula): ")
        try:
            nome, saldo_inicial = dados.split(",")
            saldo_inicial = float(saldo_inicial.strip())
            conta = ContaBancaria(nome.strip(), saldo_inicial)
            while True:
                acao = input("Digite '1' para depositar, '2' para sacar ou '3' para exibir o saldo ou '4' para sair: ").strip().lower()
                if acao == "1":
                    valor = float(input("Digite o valor a depositar: "))
                    conta.depositar(valor)
                elif acao == "2":
                    valor = float(input("Digite o valor a sacar: "))
                    conta.sacar(valor)
                elif acao == "3":
                    conta.exibir_saldo()
                elif acao == "4":
                    print("Encerrando o programa.")
                    break
                else:
                    print("Operação inválida. Tente novamente.")
            break   
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar o nome e o saldo inicial corretamente.")
if __name__ == "__main__":    main()
