from abc import ABC, abstractmethod
import random


class Character(ABC):

    def __init__(self, name: str, life: int):
        self.name = name
        self.life = life
        self.moviment = []

    @abstractmethod
    def heal(self):
        pass

    def attack(self, target: "Character", force: int = 50):
        if self.life > 0 and target.life > 0:
            # random.choice escolhe um item aleatório da lista diretamente
            hit = random.choice(self.moviment)
            print(
                f"{self.name} usou '{hit}' em {target.name} causando {force} de dano!"
            )
            target.damage_received(force)
        else:
            print(f"{self.name} não pode atacar porque alguém já está morto!")

    def damage_received(self, damage: int):
        defense = random.randint(0, 10)
        # max(0, ...) garante que o dano final nunca seja negativo
        final_damage = max(0, damage - defense)

        self.life -= final_damage
        print(f"-> {self.name} reduziu {defense} de dano com defesa.")

        if self.life <= 0:
            self.life = 0
            print(f"💀 {self.name} morreu!")
        else:
            print(f"❤️ {self.name} ficou com {self.life} de vida restante.\n")


class Warrior(Character):

    def __init__(self, name: str, life: int = 120):
        # Chama o __init__ do pai apenas com name e life
        super().__init__(name, life)
        # Define os movimentos específicos da subclasse
        self.moviment = ["Punch", "Kick", "Spin Hit"]

    def heal(self):
        heal_amount = 20
        self.life += heal_amount
        print(
            f"✨ {self.name} usou Poção e recuperou {heal_amount} de vida! Vida atual: {self.life}"
        )


class Mage(Character):

    def __init__(self, name: str, life: int = 80):
        super().__init__(name, life)
        self.moviment = ["Fireball", "Ice Bolt", "Lightning Bolt"]

    def heal(self):
        heal_amount = 35
        self.life += heal_amount
        print(
            f"✨ {self.name} usou Magia de Cura e recuperou {heal_amount} de vida! Vida atual: {self.life}"
        )


# Instanciando os personagens (Gandalf Guerreiro e Sauron Mago)

gandalf = Warrior("Gandalf Guerreiro")
sauron = Mage("Sauron Mago")

while True:
    dice = random.randint(0, 1)
    if dice == 0:
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        gandalf.attack(sauron)
        sauron.attack(gandalf)
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        sauron.attack(gandalf)
        gandalf.attack(sauron)
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")

    if gandalf.life == 0 or sauron.life == 0:
        break