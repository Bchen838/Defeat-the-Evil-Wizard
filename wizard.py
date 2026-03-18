import random


# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.is_evading = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if opponent.is_evading:
            print(f"{self.name} attacks {opponent.name} for {damage} damage but {opponent.name} evades the attack!")
            opponent.is_evading = False
            return

        
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 20
        self.health = min(self.health + heal_amount, self.max_health)

        print(f"{self.name} heals for {heal_amount} health!")
        print(f"Current health: {self.health}/{self.max_health}")

    def use_ability(self, opponent):
        print()
        print("This character has no special ability.")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)
    
    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot for {damage} damage!")

    def evade(self): 
        self.is_evading = True
        print(f"{self.name} prepares to evade the next attack!")

    def use_ability(self, opponent):
        print("1. Quick Shot")
        print("2. Evade")

        choice = input("Choose an ability: ")

        if choice == "1":
            self.quick_shot(opponent)
        elif choice == "2":
            self.evade()


# Create Paladin class 
class Paladin(Character):
    def __init__(self,name):
        super().__init__(name, health=160, attack_power=20)

    def holy_strike(self, opponent):
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def divine_shield(self):
        self.is_evading = True
        print(f"{self.name} activates Divine Shield to block the next attack!")

    def use_ability(self, opponent):
        print("1. Holy Strike")
        print("2. Divine Shield")

        choice = input("Choose an ability: ")

        if choice == "1":
            self.holy_strike(opponent)
        elif choice == "2":
            self.divine_shield()


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.use_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()