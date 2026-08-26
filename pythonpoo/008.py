class Diary:
    def __init__(self, password= "ALE"):
        self.secret = []
        self.__password = password

    def write(self, text):
        if isinstance(text, str) and len(text) > 0:
            self.secret.append(text.strip())

    def read(self, password):
        # Compara o parâmetro 'password' recebido com o atributo privado '__password'
        if password != self.__password:
            raise PermissionError('You do not have permission')
        else:
            print("THE DIARY WAS OPENED")
            for i in self.secret:
                print(i)

    @property
    def password(self):
        # Impede a leitura direta de t1.password
        raise PermissionError('You do not have permission to read password directly')

    @password.setter
    def password(self, value):
        self.__password = value

    def change_password(self, old_password, new_password):
        """Valida a senha antiga antes de definir a nova."""
        if old_password != self.__password:
            raise PermissionError('Senha atual incorreta. Troca não permitida.')
        self.__password = new_password
        print("Senha alterada com sucesso!")

# Testando a classe
t1 = Diary('ALE')
t1.change_password('ALE', '123')
t1.write('I am a secret 111111111111')
t1.write('I am a secret 2222222222222222')

# Tentativa com a senha correta:
t1.read('123')