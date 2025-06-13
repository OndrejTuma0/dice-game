import random
import math

class Enemy():
    def __init__(self):
        self.level = random.randint(1, 3)
        self.hp = 10 * (self.level/2)
        self.dmg = 5 * math.ceil(self.level/2)

    def __str__(self):
        return f"ENEMY | LVL: {enemy.level} | HP: {enemy.hp} | DMG: {enemy.dmg}"

class Weapon():
    def __init__(self, name, price, dmgMulti):
        self.name = name
        self.price = price
        self.dmgMulti = dmgMulti

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Damage Multiplier: {self.dmgMulti}"

class Item():
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc

    def __str__(self):
        return f"{self.name} | Price: {self.price} | {self.desc}"


# WEAPONS
dice = Weapon("Dice", 0, 1)
goldenDice = Weapon("Golden Dice", 100, 2)
gamblerDice = Weapon("Gambler's Dice", 250, 3)

# ITEMS
bandage = Item("Bandage", 50, "Heals 25 HP.")

# STATS
coins = 100
hp = 100
inventory = [goldenDice, bandage]
weapon = dice


shop = [goldenDice, gamblerDice, bandage]


while True:
    print("-------------------------------------------")
    choice = input("FIGHT/SHOP/INV/QUIT: ").lower()
    if choice == "fight":
        enemy = Enemy()
        print("-------------------------------------------")
        print("You encountered an enemy!")
        while True:
            print(enemy)
            print(f"YOU | HP: {hp}")
            choice = input("ROLL/FLEE: ").lower()
            if choice == "roll":
                roll = random.randint(1, 6)
                attack = roll * weapon.dmgMulti
                print("-------------------------------------------")
                print(f"You rolled a {roll} and did {attack} damage!")
                enemy.hp -= attack
                hp -= enemy.dmg
                if enemy.hp <= 0:
                    reward = (enemy.level*5) * random.randint(1, 10)
                    print(f"You won! You got {reward} coins!")
                    coins += reward
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
                        print("You don't have enough coins!")
                        continue
                else:
                    print("This item is not in the shop.")
                    continue
            elif choice == "back":
                break
    elif choice == "inv":
        while True:
            print("-------------------------------------------")
            print(f"HP: {hp}")
            print(f"Coins: {coins}")
            print(f"Weapon: {weapon.name} | Price: {weapon.price} | Damage Multiplier: {weapon.dmgMulti}")
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
                        hp += 25
                        inventory.pop(useChoice-1)
                        print("You healed 25 HP.")
                    else:
                        print("Item is not usable.")
                        continue
                else:
                    print("You don't have this many items!")
                    continue
            elif choice == "sell":
                if len(inventory) == 0:
                    print("You don't have any items!")
                    continue
                sellChoice = int(input("What item do you want to sell? (NUMBER): "))
                if sellChoice <= len(inventory):
                    coins += inventory[sellChoice-1].price
                    inventory.pop(sellChoice-1)
                else:
                    print("You don't have this many items!")
                    continue
            elif choice == "back":
                break
    elif choice == "quit":
        break
