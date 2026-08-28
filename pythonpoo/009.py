#HASH 
import hashlib

# SHA  SECURITY HASH ALGORITHM
hash = hashlib.sha256()
hash.update(b'Hello World')

print(hash.hexdigest())

class Identify:
    def __init__(self, name, age , password ):
        self.name = name
        self.age = age
        self.__password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 0:
            raise ValueError('Senha muito curta')
        elif len(value) > 8:
            raise ValueError('Senha muito longa')
        else:
            self._password = hashlib.sha256(value.encode()).hexdigest()

    def validation(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()
    
if __name__ == "__main__":
    user = Identify('John', 20, '12345678')
    user.password = '12345678'
    print(user.password)
    print(user.validation('12345678'))