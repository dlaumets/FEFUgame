import random
import pygame

class Character():
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, x, y):
        self.texture = texture
        self.hitbox = hitbox
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.diagonal_speed = diagonal_speed
        self.x = x
        self.y = y

class Player(Character):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, x, y)
        self.shield = shield

    def moving(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_a]:
            if (self.x > 246 or (self.y > 378 and self.y + self.hitbox.height < 510)) and (self.y > 222 or (self.x > 574 and self.x + self.hitbox.width < 708)):
                self.x -= self.diagonal_speed
                self.y -= self.diagonal_speed
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            if (self.x > 246 or (self.y > 378 and self.y + self.hitbox.height < 510)) and (self.y < 614 or (self.x > 574 and self.x + self.hitbox.width < 708)):
                self.x -= self.diagonal_speed
                self.y += self.diagonal_speed
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            if (self.y < 614 or (self.x > 574 and self.x + self.hitbox.width < 708)) and (self.x < 970 or (self.y > 378 and self.y + self.hitbox.height < 510)):
                self.x += self.diagonal_speed
                self.y += self.diagonal_speed
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            if (self.x < 970 or (self.y > 378 and self.y + self.hitbox.height < 510)) and (self.y > 222 or (self.x > 574 and self.x + self.hitbox.width < 708)):
                self.x += self.diagonal_speed
                self.y -= self.diagonal_speed

        elif keys[pygame.K_a]:
            if self.x > 246 or (self.y > 378 and self.y + self.hitbox.height < 510):
                self.x -= self.speed
        elif keys[pygame.K_d]:
            if self.x < 970 or (self.y > 378 and self.y + self.hitbox.height < 510):
                self.x += self.speed
        elif keys[pygame.K_s]:
            if self.y < 614 or (self.x > 574 and self.x + self.hitbox.width < 708):
                self.y += self.speed
        elif keys[pygame.K_w]:
            if self.y > 222 or (self.x > 574 and self.x + self.hitbox.width < 708):
                self.y -= self.speed

class Enemy(Character):
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, texture, hitbox, hp, damage, speed, diagonal_speed, x, y)


class Warrior(Player):
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y)

    def attack(self):
        pass

class Archer(Player):
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y)
    
    def attack(self):
        pass

class Mob(Enemy):
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y)

    def collision(self):
        pass

class Boss(Enemy):
    def __init__(self, name, hp, damage, texture, x, y, phrases):
        super().__init__(name, hp, damage, texture, x, y)
        self.phrases = phrases # Список строк

    def speak(self):
        pass
        # print(f"{self.name}: {random.choice(self.phrases)}")

class Arrow:
    def __init__(self, speed, damage):
        self.speed = speed
        self.damage = damage