import random
import math

class Enemy():
    def __init__(self, lvlMin, lvlMax):
        self.lvlMin = lvlMin
        self.lvlMax = lvlMax
        self.level = random.randint(self.lvlMin, self.lvlMax)
        self.hp = 10 * (self.level/2)
        self.dmg = 5 * math.ceil(self.level/2)

    def __str__(self):
        return f"ENEMY | LVL: {enemy.level} | HP: {enemy.hp} | DMG: {enemy.dmg}"

class Weapon():
    def __init__(self, name, price, dmgMulti, sides, canCrit, desc):
        self.name = name
        self.price = price
        self.dmgMulti = dmgMulti
        self.sides = sides
        self.canCrit = canCrit
        self.desc = desc
      
    def __str__(self):
        return f"{self.name} | Price: {self.price} | {self.desc}"

class Item():
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc

    def __str__(self):
        return f"{self.name} | Price: {self.price} | {self.desc}"

def crit(chance):
    if random.randint(1, 100) <= chance:
        print("CRITICAL HIT!")
        return roll * weapon.dmgMulti * 2
    else:
        return roll * weapon.dmgMulti
    
def heal(amount):
    global hp
    if maxhp - hp < amount:
        hp += maxhp - hp
    else:
        hp += amount


# WEAPONS
dice = Weapon("Dice", 0, 1, 6, False, "The starting weapon.")
betterDice = Weapon("Better Dice", 100, 2, 6, False, "Double the damage.")
gamblerDice = Weapon("Gambler's Dice", 250, 2, 6, True, "2x damage and has a 25% chance to crit.")
goldenDice = Weapon("Golden Dice", 1000, 4, 6, True, "4x damage and has a 25% chance to crit.")
twelveSideDice = Weapon("12-Sided Dice", 2500, 3, 12, False, "3x damage and rolls up to 12.")

# ITEMS
bandage = Item("Bandage", 50, "Heals 25 HP.")
healthPotion = Item("Health Potion", 200, "Heals 100 HP.")

# STATS
coins = 100
hp = 100
maxhp = 100
inventory = [bandage, healthPotion]
weapon = twelveSideDice

# FLOORS
floor1 = "Floor 1 (Level 1-3)"
floor2 = "Floor 2 (Level 2-5)"
floor3 = "Floor 3 (Level 4-6)"


shop = [betterDice, gamblerDice, goldenDice, twelveSideDice, bandage]
floors = [floor1, floor2, floor3]


while True:
    print("-------------------------------------------")
    choice = input("FIGHT/SHOP/INV/QUIT: ").lower()
    if choice == "fight":
        print("-------------------------------------------")
        for x in floors:
            print(x)
        floorChoice = int(input("Choose a floor (NUMBER): "))
        if floorChoice == 1:
            enemy = Enemy(1, 3)
        elif floorChoice == 2:
            enemy = Enemy(2, 5)
        elif floorChoice == 3:
            enemy = Enemy(4, 6)
        print("-------------------------------------------")
        print("You encountered an enemy!")
        while True:
            print(enemy)
            print(f"YOU | HP: {hp} / {maxhp}")
            choice = input("ROLL/FLEE: ").lower()
            if choice == "roll":
                print("-------------------------------------------")
                roll = random.randint(1, weapon.sides)
                if weapon.canCrit == True:
                    attack = crit(25)
                else:
                    attack = roll * weapon.dmgMulti
                print(f"You rolled a {roll} and did {attack} damage!")
                enemy.hp -= attack
                if enemy.hp <= 0:
                    reward = (enemy.level*5) * random.randint(enemy.level, 10)
                    coins += reward
                    print(f"You won! You got {reward} coins!")
                    break
                hp -= enemy.dmg
                if hp <= 0:
                    coins = 0
                    hp = 100
                    inventory = []
                    print("-------------------------------------------")
                    print("You died! You lost your stuff!")
                    break
            elif choice == "flee":
                print("You fleed from the battle!")
                break
    elif choice == "shop":
        while True:
            print("-------------------------------------------")
            print(f"Coins: {coins}")
            print("FOR SALE:")
            temp = 0
            for x in shop:
                temp += 1
                print(f"{temp} | {x}")
            choice = input("BUY/BACK: ").lower()
            if choice == "buy":
                buyChoice = int(input("What would you like to buy? (NUMBER): "))
                if buyChoice <= len(shop):
                    if coins >= shop[buyChoice-1].price:
                        coins -= shop[buyChoice-1].price
                        inventory.append(shop[buyChoice-1])
                        if type(shop[buyChoice-1]) is Weapon:
                            shop.pop(buyChoice-1)
                        else:
                            pass
                    else:
                        print("-------------------------------------------")
                        print("You don't have enough coins!")
                        continue
                else:
                    print("-------------------------------------------")
                    print("This item is not in the shop.")
                    continue
            elif choice == "back":
                break
    elif choice == "inv":
        while True:
            print("-------------------------------------------")
            print(f"HP: {hp} / {maxhp}")
            print(f"Coins: {coins}")
            print(f"Weapon: {weapon}")
            print("Inventory:")
            temp = 0
            for x in inventory:
                temp += 1
                print(f"{temp} | {x}")
            choice = input("USE/SELL/BACK: ").lower()
            if choice == "use":
                if len(inventory) == 0:
                    print("You don't have any items!")
                    continue
                useChoice = int(input("Which item do you want to use? (NUMBER): "))
                if useChoice <= len(inventory):
                    if type(inventory[useChoice-1]) is Weapon:
                        inventory.append(weapon)
                        weapon = inventory[useChoice-1]
                        inventory.remove(weapon)
                    elif inventory[useChoice-1] == bandage:
                        heal(25)
                        inventory.pop(useChoice-1)
                        print("-------------------------------------------")
                        print("You healed 25 HP.")
                    elif inventory[useChoice-1] == healthPotion:
                        heal(100)
                        inventory.pop(useChoice-1)
                        print("-------------------------------------------")
                        print("You healed 100 HP.")
                    else:
                        print("-------------------------------------------")
                        print("Item is not usable.")
                        continue
                else:
                    print("-------------------------------------------")
                    print("You don't have this many items!")
                    continue
            elif choice == "sell":
                if len(inventory) == 0:
                    print("-------------------------------------------")
                    print("You don't have any items!")
                    continue
                sellChoice = int(input("What item do you want to sell? (NUMBER): "))
                if sellChoice <= len(inventory):
                    coins += inventory[sellChoice-1].price
                    inventory.pop(sellChoice-1)
                else:
                    print("-------------------------------------------")
                    print("You don't have this many items!")
                    continue
            elif choice == "back":
                break
    elif choice == "quit":
        break
