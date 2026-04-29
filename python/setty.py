import os
import subprocess
import keyboard

# Dicionário de atalhos: Nome que você fala/digita -> Caminho do arquivo ou programa
# DICA: Use o 'r' antes das aspas para o Python ler as barras invertidas do Windows corretamente
MEUS_ATALHOS = {
    "estudar": r"C:\Caminho\Para\Seu\Edital_Cesgranrio.pdf",
    "questoes": r"https://www.qconcursos.com",
    "simulado": r"C:\Caminho\Para\Sua\Planilha_Desempenho.xlsx",
    "terminal": "cmd.exe",
    "obs": r"C:\Caminho\Para\O\OBS64.exe"
}

def executar_acao(comando):
    comando = comando.lower().strip()
    
    if comando in MEUS_ATALHOS:
        item = MEUS_ATALHOS[comando]
        print(f"Jarvis: Executando '{comando}'...")
        
        # Se for um link, abre no navegador padrão
        if item.startswith("http"):
            os.startfile(item)
        # Se for um arquivo ou programa, usa o sistema
        else:
            try:
                os.startfile(item)
            except Exception as e:
                print(f"Erro ao abrir {comando}: {e}")
    else:
        print("Jarvis: Comando não reconhecido nos atalhos locais.")

# Função para ativar o Jarvis via teclado (ex: Ctrl + Alt + J)
def ativar_jarvis():
    print("\n--- Jarvis Ativo: Digite o comando ---")
    comando = input(">> ")
    executar_acao(comando)

print("Jarvis em standby. Pressione Ctrl+Alt+J para comandar.")
keyboard.add_hotkey('ctrl+alt+j', ativar_jarvis)

keyboard.wait() # Mantém o programa rodando

if comando == "iniciar turno": # type: ignore
    os.startfile(r"C:\Estudos\Cronometro.exe")
    os.startfile(r"C:\Estudos\Material_TI_Cesgranrio.pdf")
    subprocess.Popen(["notepad.exe", "anotacoes_hoje.txt"])
