import pygame
import random

# Init
pygame.init()
screen = pygame.display.set_mode((1200, 800))

#? W E A T H E R 
# Each Rain Drop Particle Class
class rainDrop():
    def __init__(self, startYLevel, screenWidth, width, height):
        self.x = random.randint(0, screenWidth)
        self.y = startYLevel
        self.width = width
        self.height = height
        self.rainDropSpeed = 1

# Each Snow Flake
class snowFlake():
    def __init__(self, startYLevel, screenWidth, width, height, radius):
        self.x = random.randint(0, screenWidth)
        self.y = startYLevel
        self.width = width
        self.height = height
        self.radius = radius
        self.snowFlakeSpeed = 1
        randomRoll = random.randint(0, 1)
        if randomRoll == 0:
            self.type = "circle"
        else:
            self.type = "rectangle"

# Weather System
class Weather():
    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.rainDrops = []
        self.snowFlakes = []
        self.rainAmount = 1
        self.rainColor = (0, 0, 255)
        self.rainStartLevel = 0
        self.rainDropWidth = 1
        self.rainDropHeight = 2
        self.rainDropSpeed = 1
        self.snowAmount = 1
        self.snowColor = (255, 255, 255)
        self.snowStartLevel = 0
        self.snowFlakeWidth = 1
        self.snowFlakeHeight = 2
        self.snowFlakeSpeed = 1
        self.snowFlakeRadius = 1

    #? R A I N
    def rain(self, amount, speed, color, startYLevel, width, height):
        self.rainAmount = amount
        self.rainColor = color
        self.rainStartLevel = startYLevel
        self.rainDropWidth = width
        self.rainDropHeight = height
        self.rainDropSpeed = speed
        for i in range(0, amount):
            newRainDrop = rainDrop(startYLevel, self.screenWidth, width, height)
            self.rainDrops.append(newRainDrop)

    def rainFall(self):
        self.screen.fill((0, 0, 0))
        self.clearRainLevel = False
        for i in range(0, len(self.rainDrops) - 1):
            if self.rainDrops[i].y >= self.screenHeight:
                self.clearRainLevel =  True
            self.rainDrops[i].y += self.rainDropSpeed
            pygame.draw.rect(self.screen, self.rainColor, (self.rainDrops[i].x, self.rainDrops[i].y, self.rainDrops[i].width, self.rainDrops[i].height), self.rainDrops[i].width)
        self.rainFallManager()

    def rainFallManager(self):
        if self.clearRainLevel == True:
            for i in range(0, self.rainAmount):
                del self.rainDrops[i]
            self.clearRainLevel = False
        self.rain(self.rainAmount, self.rainDropSpeed, self.rainColor, self.rainStartLevel, self.rainDropWidth, self.rainDropHeight)

    #? S N O W 
    def snow(self, amount, speed, color, startYLevel, width, height, radius):
        self.snowAmount = amount
        self.snowColor = color
        self.snowStartLevel = startYLevel
        self.snowFlakeWidth = width
        self.snowFlakeHeight = height
        self.snowFlakeSpeed = speed
        self.snowFlakeRadius = radius
        for i in range(0, amount):
            newSnowFlake = snowFlake(startYLevel, self.screenWidth, width, height, radius)
            self.snowFlakes.append(newSnowFlake)

    def snowFall(self):
        self.screen.fill((0, 0, 0))
        self.clearSnowLevel = False
        for i in range(0, len(self.snowFlakes) - 1):
            if self.snowFlakes[i].y >= self.screenHeight:
                self.clearSnowLevel =  True
            self.snowFlakes[i].y += self.snowFlakeSpeed
            if self.snowFlakes[i].type == "rectangle":
                pygame.draw.rect(self.screen, self.snowColor, (self.snowFlakes[i].x, self.snowFlakes[i].y, self.snowFlakes[i].width, self.snowFlakes[i].height), self.snowFlakes[i].width)
            else:
                pygame.draw.circle(self.screen, self.snowColor, (self.snowFlakes[i].x, self.snowFlakes[i].y), self.snowFlakes[i].radius, self.snowFlakes[i].width)
        self.snowFallManager()

    def snowFallManager(self):
        if self.clearSnowLevel == True:
            for i in range(0, self.snowAmount):
                del self.snowFlakes[i]
            self.clearSnowLevel = False
        self.snow(self.snowAmount, self.snowFlakeSpeed, self.snowColor, self.snowStartLevel, self.snowFlakeWidth, self.snowFlakeHeight, self.snowFlakeRadius)



# Implementation
weather = Weather(screen, 1200, 800)
weather.rain(1, 2, (255, 0, 255), 0, 1, 10)
weather.snow(1, 5, (255, 255, 255), 0, 2, 2, 8)

# Game Loop
isRunning = True
while isRunning:
    weather.snowFall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    pygame.display.update()
pygame.quit()