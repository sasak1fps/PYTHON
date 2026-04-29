import os
from google import genai
import pyttsx3
import sys

# 1. Configurar a Voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 180)

def falar(texto):
    print(f"Diana: {texto}")
    engine.say(texto)
    engine.runAndWait()

# 2. Configurar o Cliente Novo (Substitua pela sua chave)
client = genai.Client(api_key="AIzaSyDSg1j28jBs9gxB703r-pUuymfcBIvgh1Y",
                      http_options={'api_version': 'v1'}
)

def processar_comando(comando):
    comando = comando.lower().strip()
    if not comando: return

    # Comandos de Sistema
    if "abrir simulado" in comando:
        falar("Localizando seus arquivos de estudo.")
        os.startfile(r"C:\Estudos\Simulados")
        return

    if "bloco de notas" in comando:
        os.system("start notepad.exe")
        return

    if comando in ["sair", "exit", "desligar"]:
        falar("Desligando sistema.")
        sys.exit()

    # Pesquisa via IA (Lógica Nova e Estável)
    # Pesquisa via IA
    try:
        # Usamos o nome simplificado. A v1 reconhece esse modelo direto.
        response = client.models.generate_content(
            model='gemini-1.5-flash', 
            contents=comando
        )
        
        if response.text:
            falar(response.text)
            
    except Exception as e:
        # Se ainda der erro, o print abaixo vai nos dizer se é cota ou autenticação
        print(f"Erro na Diana: {e}")
        falar("Ainda estou com um bloqueio no meu acesso central.")

# --- INICIALIZAÇÃO ---
print("\nDIANA SYSTEM 2.0 - ONLINE")
falar("Sistema iniciado.")

while True:
    user_input = input("\nVocê: ")
    processar_comando(user_input)