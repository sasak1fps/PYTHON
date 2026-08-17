#***************PYTHON****************
'''
#EXERCISE 1 CALC RECTANGLE AREA 
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)

#EXERCISE 2 SHOPPING CART
item = input("Enter the name of items you want to buy: ")
price= float(input("Enter the price of each item: "))
quantity = int(input("Enter the quantity of each item: "))
total = price * quantity
print(f"You bought {quantity} {item}(s) at ${price} each.")
print("The total cost of the shopping cart is:", total)

#EXERCISE 3 CALCULETE AREA OF CIRCLE
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)

#EXERCISE 4 CALCULATE HYPOTENUSE OF A RIGHT TRIANGLE
import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.hypot(a, b)   # c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c)

#EXERCISE 5 IF VALIDATION
age = int(input("Enter your age: "))
if age >=100:
    print("You are a centenarian!")
elif age <= 0:
    print("You are not born yet!")
elif age < 18 and age > 0:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior citizen.")
else:
    print("Invalid age entered.")

#EXERCISE 6 CALCULATOR
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Enter your choice (1-4): "))
if operation == 1:
    result = number1 + number2
    print("The result of addition is:", result)
elif operation == 2:
    result = number1 - number2
    print("The result of subtraction is:", result)
elif operation == 3:
    result = number1 * number2
    print("The result of multiplication is:", result)
elif operation == 4:
    if number2 != 0:
        result = number1 / number2
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")

#EXERCISE 7 WEIGHT CONVERTER
weight = float(input("Enter your weight in :"))
unit = input("Enter the unit (kg or lb): ").lower()
if unit == "kg":
    converted_weight = weight * 2.20462
    print(f"Your weight in pounds is: {converted_weight:.2f} lb")
elif unit == "lb":
    converted_weight = weight / 2.20462
    print(f"Your weight in kilograms is: {converted_weight:.2f} kg")
else:
    print("SORRY! Invalid unit entered. Please enter 'kg' or 'lb'.")

#EXERCIASE 8 TEMPERATURE CONVERTER
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius or F for Fahrenheit): ").upper()
if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {converted_temperature:.2f} °F")
elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    print(f"The temperature in Celsius is: {converted_temperature:.2f} °C")
else:
    print("SORRY! Invalid unit entered. Please enter 'C' or 'F'.")


#EXERCISE 9 VALIDATION USER NAME
name = input("Enter your name: ").capitalize()
if len(name) < 3:
    print("SORRY! Your name is too short. It must be at least 3 characters long.")
elif len(name) > 13:
    print("SORRY! Your name is too long. It must be at most 13 characters long.")
elif not name.isalpha():
    print("SORRY! Your name must contain only letters.")
elif not name.find(" "):
    print("SORRY! Your name must not contain spaces.")
else:
    print(f"Hello, {name}!")

#EXERCISE 10  COMPOUND INTEREST CALCULATOR
principal = 0 
rate = 0
time = 0
while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("SORRY! Principal amount must be greater than 0.")
while rate <= 0:
    rate = float(input("Enter the annual interest rate (greater than 0): "))
    if rate <= 0:
        print("SORRY! Interest rate must be greater than 0.")
while time <= 0:
    time = float(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("SORRY! Time must be greater than 0.")
total = principal * pow(1 + rate / 100, time)
print(f"The total amount after {time} years is: {total:.2f}")


#EXECRCISE 11  FOR LOOP CLOCK
import time

mytime = int(input("Enter the time in seconds: "))

for temporizer in range(mytime, 0, -1):
    hours = temporizer // 3600
    minutes = (temporizer // 60) % 60
    seconds = temporizer % 60
    
    # Imprime no formato HH:MM:SS
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
    time.sleep(1) # Aguarda 1 segundo entre cada contagem

print("00:00:00 - Tempo esgotado!")


#EXERCISE 12  LIST AND DIC
foods = []
prices =[]
total = 0 
while True:
    food = input("Enter the name of food item(q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

for i in range(len(foods)):
    total += prices[i]


print(f"Total amount: ${total:.2f}")

#EXERCISE 13 MATRIX
fruits = ["Apple", "Banana", "Cherry"]
vegetables = ["Carrot", "Broccoli", "Spinach"]
meats = ["Chicken", "Beef", "Pork"]

grocery_list = fruits, vegetables, meats

print(grocery_list )
#EXERCISE 14  NUMPAD
numpad = ((1, 2, 3),
          (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))
for row in numpad:
    for item in row:
        print(item, end=" ")
    print()  # Move to the next line after each row
    
#EXERCISE 15  QUIZ GAME 
questions = ("How many continents are there on Earth?",
             "What is the capital of France?",
             "How many planets are in our solar system?",
             "What is the largest mammal?",
             "In which year did World War II end?")

options = (("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
           ("A. 7", "B. 8", "C. 9", "D. 10"),
           ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"),
           ("A. 1944", "B. 1945", "C. 1946", "D. 1947"))

answers = ("C", "C", "B", "B", "B")

guesses = []
score = 0
questions_num = 0

for question in questions:
    print("-------------")
    print(question)
    
    # Imprime cada alternativa individualmente
    for option in options[questions_num]:
        print(option)
        
    guess = input("ENTER: A B C D ").upper()
    guesses.append(guess)
    
    # Compara o palpite atual (guess) com a resposta certa
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[questions_num]} is the correct answer")  
        
    questions_num += 1

print("-------------")
print(f"Fim do quiz! Você acertou {score} de {len(questions)} perguntas.")


#EXERCISE 16 CONCESSION STAND PROGAM
# Todas as chaves em minúsculas
menu = {
    "burger": 5.99,
    "fries": 2.99,
    "shake": 1.99,
    "pizza": 8.99,
    "pasta": 6.99,
    "salad": 3.99,
    "soda": 1.99
}

cart = []
total = 0

print("--- MENU ---")
for key, value in menu.items():
    # .capitalize() deixa a primeira letra maiúscula só na impressão
    print(f"{key.capitalize():10} - ${value:.2f}")
print("------------")

while True:
    item = input("Digite o nome do produto (ou 'done' para encerrar): ").strip().lower()
    
    if item == "done":
        break
    elif item in menu:
        cart.append(item)
        print(f"-> {item.capitalize()} adicionado ao carrinho!")
    else:
        print("Item not found in the menu.")

print("\n------------")
for item in cart:
    total += menu[item]

# Exibe os itens do carrinho bonitinho com a primeira letra maiúscula
cart_formatted = [i.capitalize() for i in cart]
print(f"Your cart: {', '.join(cart_formatted)}")
print(f"Total: ${total:.2f}")


#EXERCISE 17 GUESSING GAME
import random
num = random.randint(1, 100)

while True:
    guess = input("Guess a number between 1 and 100: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid input. Please enter a number.")
        continue
    if guess == num:
        print("Congratulations! You guessed the number!")
        break
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

        
#EXERCISE 18  ROCK PAPER SCISSORS
import random

options = ["rock", "paper", "scissors"]


menu_map = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}

score = 0

print("--- JOKENPÔ ---")
print("1. ROCK")
print("2. PAPER")
print("3. SCISSORS\n")

while True:
    computer = random.choice(options)
    
   
    user_input = input("Escolha (1, 2, 3 ou rock, paper, scissors): ").strip().lower()

   
    player = menu_map.get(user_input, user_input)


    if player not in options:
        print("❌ Opção inválida! Digite 1, 2, 3 ou rock, paper, scissors.\n")
        continue

    print(f"Você escolheu: {player.upper()}")
    print(f"Computador escolheu: {computer.upper()}")


    if player == computer:
        print("🤝 It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        score += 1
        print("🎉 You win!\n")
    else:
        print("💥 You lose!")
        break
print("----------------")
print(f"Game Over! Seu score final foi: {score}")

#EXERCISE 19  MACTH CASE
def weekday(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

day = int(input("Enter a number between 1 and 7: "))
print(weekday())

#EXERCISE 20  SLOT MACHINE
import random

def spin_row():
    symbols = ["🍒", "🍇", "🍐", "🍊", "🍋"]
    result = []
    for _ in range(3):
        result.append(random.choice(symbols))
    return result

def main():
    balance = 100
    print("Welcome to the Slot Machine!")
    print("Symbols🍒🍇🍐🍊🍋")

    while balance > 0:
        bet = int(input("Enter your bet: "))
        if bet <= 0 or bet > balance:
            print("Invalid bet. Please enter a valid amount.")
            continue

        spin_row_result = spin_row()
        print(f"Symbol 1: {spin_row_result[0]}")
        print(f"Symbol 2: {spin_row_result[1]}")
        print(f"Symbol 3: {spin_row_result[2]}")

        if spin_row_result[0] == spin_row_result[1] == spin_row_result[2]:
            balance += bet
            print(f"You won! Your balance is now: ${balance}")
        else:
            balance -= bet
            print(f"You lost! Your balance is now: ${balance}")

        if balance <= 0:
            print("You're out of money! Game over.")
            break

if __name__ == "__main__":
    main()

#exercise 21  INCRYPTING TEXT

def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = chr(ord(char) + 1)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

text = input("Enter the text to encrypt: ")
encrypted_text = encrypt(text)
print("Encrypted text:", encrypted_text)
#EXERCISE 22 INCRYPTING TEXT 2
import string
import random
char=" "+string.ascii_letters + string.digits
char=list(char)
key =char.copy()
random.shuffle(key)


#INCRYPT
plaint_text = input("Enter the text to encrypt: ")
encrypted_text = ""
for char in plaint_text:
    index=char.index(char)
    encrypted_text+=key[index]
print(f"Plaint text: {plaint_text}")
print(f"Encrypted text: {encrypted_text}")
#DECRYPT
decrypted_text=""
for char in encrypted_text:
    index=key.index(char)
    decrypted_text+=char[index]
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")

#EXERCISE 23  HANGMAN GAME
import random
wors= ("apple", "banana", "orange", "grape", "kiwi", "strawberry", "pineapple", "mango", "watermelon", "peach")

def hangman():
    word = random.choice(wors)
    guessed_letters = []
    attempts = 6

    while True:
        print("Guess the word:")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print("You lost! The word was:", word)
                break

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break
if __name__ == "__main__":
    hangman()
#EXERCISE 24  EXCEPTONS
try:
    num = int(input("Enter a number: "))
    denominator = int(input("Enter a denominator: "))
    result = num / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
#EXERCISE 25  GET TIME
from datetime import datetime
current_time = datetime.now()
print("Current time:", current_time)
#EXERCISE 26  GET DATE
from datetime import date
current_date = date.today()
print("Current date:", current_date)
#EXERCISE  27 ALARM CLOCK
from datetime import datetime

alarm_time = input("Enter the alarm time (HH:MM): ")
alarm_datetime = datetime.strptime(alarm_time, "%H:%M:%S")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_datetime:
        print("Time's up!")
        break 
print("Alarm set for", alarm_time)

#EXERCISE 28  REQUEST API
import requests
base_url = "https://pokeapi.co/api/v2/"
def get_pokemon_inf(*args, **kwargs):
    pokemon_name = input("Enter the name of the Pokemon: ")
    url=f'{base_url}pokemon/{pokemon_name}'
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json(**kwargs)
        print(f"Name: {pokemon_data['name']}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}")
    else:
        print("Pokemon not found.")

if __name__ == "__main__":
    get_pokemon_inf()

'''