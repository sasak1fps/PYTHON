
from rich import print
from rich.panel import Panel

'''
class Employee:
    def __init__(self, name, job ):
        self.name = name
        self.job = job

    def list_employees(self):
        print(f"Employee Name: {self.name}, Job: {self.job}")

    def main():
        while True:
            name = input("Enter employee name (or '0' to exit ): " ).strip().lower()
            if name == '0':
                break
            job = input("Enter employee job: ")
            employee = Employee(name, job)
            employee.list_employees()


print("Welcome to the Employee Management System")
print("Please enter employee details below:")
Employee.main()

print("---------------------------------------------------------------------------------------------------------------------------------------------------")
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def main():
        while True:
            name = input("Enter product name (or '0' to exit): ").strip().lower()
            if name == '0':
                break
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            box = Panel(f"Product Name: {name}\nPrice: ${price:.2f}\nQuantity: {quantity}", title="Product Information", style="bold green")
            print(box)

print("Welcome to the Product Management System")
print("Please enter product details below:")
Product.main()

print("---------------------------------------------------------------------------------------------------------------------------------------------------")


class Churras:
    consumption = 0.5 # each people eat  500g of meat
    kilograms = 80.00 # 1 kg of meat costs 80.00

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_consumption(self):
        return self.quantity * Churras.consumption
    def calculate_total_cost(self):
        return self.price * self.quantity
    
    def display_info(self):
        content = f"Name: [green]{self.name}[/]\nPrice: [blue]${self.price:.2f}[/]\nQuantity: [yellow]{self.quantity}[/]\nConsumption: [red]{self.calculate_consumption()} kg per person[/]\nTotal Cost: [magenta]${self.calculate_total_cost():.2f}[/]"
        box = Panel(content, title="CHURRAS OF FRIENDS", style="bold red")
        print(box)

   
Churras.display_info(Churras("CHAPIONS LEAGUE ", Churras.kilograms, 33))

print('*****************************************************************************************************************************************************************************')
class validationBookPages:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def validate_pages(self):
        if self.pages < 1:
            raise ValueError("The number of pages must be greater than zero.")
        else:
            print(f"The book '{self.title}' by {self.author} has {self.pages} pages.")
    def skipPages(self, pages_to_skip):
        if pages_to_skip < 1:
            raise ValueError("The number of pages to skip must be greater than zero.")
        elif pages_to_skip > self.pages:
            raise ValueError("Cannot skip more pages than the total number of pages in the book.")
        else:
            self.pages -= pages_to_skip
            print(f"Skipped {pages_to_skip} pages. Remaining pages: {self.pages}")


book1 = validationBookPages("The Great Gatsby", "F. Scott Fitzgerald", 180)
book1.validate_pages()
book1.skipPages(67)
('*****************************************************************************************************************************************************************************')

class Games:
    def __init__(self, name, nickname, games_list):
        self.name = name
        self.nickname = nickname
        self.games_list = games_list  # Agora recebe uma lista de jogos

    def display_info(self):
        # Transforma a lista de jogos em uma string formatada com quebra de linha
        formatted_games = "\n".join([f" - [blue]{game}[/]" for game in self.games_list])
        
        content = (
            f"Name: [green]{self.name}[/]\n"
            f"Nickname: [blue]{self.nickname}[/]\n"
            f"Games:\n{formatted_games}"
        )
        box = Panel(content, title="GAMES", style="bold yellow")
        print(box)

def main():
    while True:
        name = input("Enter your name (or '0' to exit): ").strip()
        if name == '0':
            break
            
        nickname = input("Enter your nickname: ").strip()
        user_games = []  # Lista para armazenar todos os jogos deste usuário

        while True:
            game_name = input("Enter your favorite game (or '0' to stop adding games): ").strip()
            if game_name == '0':
                break
            user_games.append(game_name)  # Adiciona o jogo na lista

        
        player = Games(name, nickname, user_games)
        player.display_info()

if __name__ == "__main__":
    main()

class Pen:
    def __init__(self, color="blue"):
        # Trata o texto recebido para evitar problemas com maiúsculas/espaços
        color_clean = color.strip().lower()
        
        match color_clean:
            case "red":
                self.color_tag = "red"
            case "blue":
                self.color_tag = "blue"
            case "green":
                self.color_tag = "green"
            case _:
                self.color_tag = "white"  # Cor padrão se a entrada não for reconhecida

    def write(self, text):
        # Aplica a tag da cor diretamente no texto que será escrito
        print(f"Writing in {self.color_tag} color: [{self.color_tag}]{text}[/]")

def main():
    while True:
        color = input("Enter pen color (red, blue, green, or '0' to exit): ").strip().lower()
        if color == '0':
            break
        
        text = input("Enter text to write: ")
        
        # 1. Cria o objeto Caneta com a cor escolhida
        pen = Pen(color)
        
        # 2. Chama o método de escrita na instância
        pen.write(text)

if __name__ == "__main__":
    main()
'''
