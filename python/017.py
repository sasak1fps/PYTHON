"TRATAMENTO DE ERRORES EM PYTHON"

'''
try:
    # Código que pode gerar um erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:

    print("Erro: Você deve digitar um número válido.")
except ZeroDivisionError:

    print("Erro: Divisão por zero.")    

"EXEMPLO "
try:
    numero = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    resultado = numero / numero2
except (ValueError, ZeroDivisionError) as e:
    print(f"Ocorreu um erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e.__class__}")
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Fim do programa.")


"TRATANDO ERROS "


def lerinteiro():
    while True:
        try:
            inteiro = int(input("Digite um número inteiro: "))
            real = float(input("Digite um número real: "))
            
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números corretos.")
            continue    
        else:
            return inteiro, real
        finally:
            print("Programa finalizado.")
lerinteiro()
    
'''
"VERIFICAR SITE ONLINE  OU OFFLINE"
import site
import urllib
import urllib.error
import urllib.request 

def verificar_site(url):
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            return True
        else:
            return False
    except urllib.error.URLError:
        return False
url = input("Digite o URL do site (inclua http:// ou https://): ")
if verificar_site(url):
    print(f"O site {url} está online.")
    
else:
    print(f"O site {url} está offline.")

