#Inheritance
from abc import ABC,    abstractmethod
from math import e
"""class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def birthday(self):
        self.idade += 1


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso , turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma =  turma
    def matricula(self):
        print(f"Matriculado no curso {self.curso} na turma {self.turma}")
   
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, nivel):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.nivel = nivel
    def ensinar(self):
        print(f"Estou ensinando {self.disciplina} no nivel {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    def trabalhar(self):
        print(f"Estou trabalhando como {self.cargo} no setor {self.setor}")


a1 =Estudante("Alessandro", 22, "Engenharia da Computação", "2022")
a2 = Professor("Alessandro", 22, "Matematica", "Graduado")
a3 = Funcionario("Alessandro", 22, "Engenheiro", "TI")
print(a1.nome, a1.idade, a1.curso, a1.turma)
print(a2.nome, a2.idade, a2.disciplina, a2.nivel)
print(a3.nome, a3.idade, a3.cargo, a3.setor)

#EXCERSICE 1 
class Polygon(ABC):
    def __init__(self,sides):
        self.sides = sides

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.height + self.sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius




triangle = Triangle(3, 4)
rectangle = Rectangle(4, 4)
circle = Circle(4)

print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())
#EXCERSICE 2 STORE COFFEE
class HotDrinks(ABC):
    def prepare(self):
        print(f"--PREPARING --")
        self.boilwater()
        self.mix()
        self.serve()
        print("--DRINK HAS BEEN DONE--")
    def boilwater(self):
        print(f"BOWLING WATER AT 100 DEGREES CELSIUS")
    @abstractmethod
    def mix(self):
        print(self.mix)
    @abstractmethod
    def serve(self):
        print(self.serve)

class Coffee(HotDrinks):
    def mix(self):
        print(f"2. pouring the water into the coffee")
    def serve(self):
        print(f"3.serving the coffee")

class Tea(HotDrinks):
    def mix(self):
        print(f"2. pouring the water into the tea")
    def serve(self):
        print(f"3.serving the tea")

class Milk(HotDrinks):
    def mix(self):
        print(f"2. pouring the water into the milk")
    def serve(self):
        print(f"3.serving the milk")

number1 = Coffee()
number1.prepare()


#EXCERSICE 3 FRETE
class Vehicle(ABC):

    def __init__(self, distance: float):
        self.distance = distance
        self.freight = 0.0

    @abstractmethod
    def calculate_freight(self):
        pass


class Motorcycle(Vehicle):

    def __init__(self, distance: float):
        super().__init__(distance)

    def calculate_freight(self):
        rate = 0.5
        self.freight = self.distance * rate
        return self.freight


class Truck(Vehicle):

    def __init__(self, distance: float):
        super().__init__(distance)

    def calculate_freight(self):
        rate = 1.2
        if self.distance < 50:
            print("Freight is not available for this distance")
            self.freight = 0.0
        else:
            self.freight = self.distance * rate
        return self.freight


class Drone(Vehicle):

    def __init__(self, distance: float):
        super().__init__(distance)

    def calculate_freight(self):
        rate = 9.5
        self.freight = self.distance * rate
        return self.freight


# Instanciação dos objetos
motorcycle = Motorcycle(100)
truck = Truck(49)
drone = Drone(100)

# Cálculo e exibição
motorcycle.calculate_freight()
truck.calculate_freight()
drone.calculate_freight()

print(f"Frete Moto: R$ {motorcycle.freight:.2f}")
print(f"Frete Caminhão: R$ {truck.freight:.2f}")
print(f"Frete Drone: R$ {drone.freight:.2f}")

#EXCERSICE 4 EMPLOYEES INFORMATION
class Employee(ABC):
    def __init__(self, name, salary ,sal_min = 1612 , inss = 7.5):
        self.name = name
        self.salary = salary
        self.inss = inss
        self.sal_min = sal_min
    @abstractmethod
    def calculate_salary(self):
        pass

class Hours_employee(Employee):
    def __init__(self, name, salary, hours_worked):
        super().__init__(name, salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.salary * self.hours_worked - self.salary * self.inss
    
class Mouth_employee(Employee):
    def __init__(self, name, salary, hours_worked):
        super().__init__(name, salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.salary * self.hours_worked - self.salary * self.inss


name = input("Enter the name of the employee: ")
salary = float(input("Enter the salary of the employee: "))
hours_worked = float(input("Enter the number of hours worked by the employee: "))

employee = Hours_employee(name, salary, hours_worked)
print(f"The salary of the employee {employee.name} is R$ {employee.calculate_salary():.2f}")
"""