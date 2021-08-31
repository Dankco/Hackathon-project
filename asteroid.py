import math
import pygame
import random


# Asteroids have a random X coordinate and start at the top of the screen(can be changed)
# They have a random angle of velocity between 0 and 180 degrees
# The magnitude of velocity can be changed for each asteroid
# The asteroid contains an encrypted value
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, level, value):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(max(0, 300-level*10), min(450+level*10, 750))
        self.rect.y = 0
        self.asteroidVelocity = level*2
        self.asteroidAngle = random.uniform(0, math.pi)
        self.asteroidValue = value
        if random.randint(0, 10) == 10:
            self.special1 = True
            self.image = pygame.image.load("Asteroids.png")
        elif random.randint(0, 5) == 5:
            self.special2 = True
            self.asteroidVelocity = level*2 + 3
            self.image = pygame.image.load("Specialasteroid.png")
            pygame.transform.rotate(self.image, self.asteroidAngle*180/math.pi)
        else:
            self.special1 = False
            self.special2 = False
            self.image = pygame.image.load("Specialasteroid.png")

    # makes the asteroid move on its own in its predetermined direction
    def update(self):
        self.rect.x += self.asteroidVelocity * math.cos(self.asteroidAngle)
        self.rect.y += self.asteroidVelocity * math.sin(self.asteroidAngle)

    # the asteroid will be destroyed if the laser is within 20 pixels of its center and return its value
    # it will also award points based on the asteroid destroyed
    def destroy(self, laserx, lasery, playershot, scores):
        distance = math.sqrt(math.pow(laserx - self.rect.x, 2) + math.pow(lasery - self.rect.y, 2))
        if distance < 20:
            del self
            # this asteroid
            if len(scores) > 0:
                if self.special1:
                    scores[0] += 100
                    return self.asteroidValue  # this will need to be changed to decrypt the encryption
                elif self.special2:  # if special asteroid #2, increases the player shots
                    playershot += 1
                    scores[0] += 500
                    return self.asteroidValue
                else:
                    scores[0] += 10
                    return self.asteroidValue

    # returns true if the asteroid collides with the player and destroys the asteroid or false if it does not
    def collide(self, playerx, playery):
        distance = math.sqrt(math.pow(playerx - self.rect.x, 2) + math.pow(playery - self.rect.y, 2))
        if distance < 50:
            del self
            return True
        else:
            return False

