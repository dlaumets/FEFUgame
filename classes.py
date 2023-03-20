class Character:
    def __init__(self, name, health, strength, texture, x, y):
        self.name = name
        self.health = health
        self.strength = strength
        self.texture = texture
        self.x = x
        self.y = y

class Player(Character):
    def __init__(self, name, health, strength, defense, inventory, texture):
        super().__init__(name, health, strength, texture)
        self.defense = defense
        self.inventory = inventory


class Enemy(Character):
    def __init__(self, name, health, strength, defense, xp, texture):
        super().__init__(name, health, strength, texture)
        self.defense = defense
        self.xp = xp


class Warrior(Player):
    def __init__(self, name, health, strength, defense, inventory, texture):
        super().__init__(name, health, strength, defense, inventory, texture)


class Archer(Player):
    def __init__(self, name, health, strength, defense, inventory,texture):
        super().__init__(name, health, strength, defense, inventory,texture)


class Mob(Enemy):
    def __init__(self, name, health, strength, defense):
        super().__init__(name, health, strength, defense)


class Boss(Enemy):
    def __init__(self, name, health, strength, defense, phrases):
        super().__init__(name, health, strength, defense)
        self.phrases = phrases

    def speak(self):
        print(f"{self.name}: {random.choice(self.phrases)}")

class Arrow:
    def __init__(self, speed, damage):
        self.speed = speed
        self.damage = damage