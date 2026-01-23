import customtkinter as ctk 

#APERENCE
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


def criar_label(root, texto, fonte=('Arial', 15), cor='white', justify='center'):
    label = ctk.CTkLabel(root, text=texto, font=fonte, text_color=cor, justify=justify)
    label.pack(padx=10, pady=10)
    return label


def criar_entrada(root, placeholder_text, show=''):
    entrada = ctk.CTkEntry(root, placeholder_text=placeholder_text, show=show)
    entrada.pack(padx=10, pady=10)
    return entrada


def criar_botao(root, texto, command):
    botao = ctk.CTkButton(root, text=texto, command=command)
    botao.pack(padx=10, pady=10)
    return botao


def criar_label_resultado(root, texto=''):
    label = ctk.CTkLabel(root, text=texto)
    label.pack(padx=10, pady=10)
    return label


def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if usuario == 'admin' and senha == 'admin':
        resultado_login.configure(text= 'Login realizado com sucesso' , text_color='green')
    else:
        resultado_login.configure(text= 'Login inválido' , text_color='red')


#criacao da janela
app = ctk.CTk()  # pyright: ignore[reportAttributeAccessIssue]
app.title("Sistema de cadastro")
app.geometry("400x400")


#criacao dos campos
label_usuario = criar_label(app, texto='Usuário')
campo_usuario = criar_entrada(app, placeholder_text='Digite o usuario')


label_senha = criar_label(app, texto='Senha')
campo_senha = criar_entrada(app, placeholder_text='Digite sua senha', show='*')


botao_entrar = criar_botao(app, texto='Entrar', command=validar_login)


resultado_login = criar_label_resultado(app, texto='')

app.mainloop()
