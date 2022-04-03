import pygame
import random

# Init
pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Loads images, and animates them
class AssetImage():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.imagePath = 0
        self.screen = screen
        self.imageSurface = 0
        self.flipImageX = False
        self.flipImageY = False
        self.scaleImageX = 1
        self.scaleImageY = 1
        self.rotateImageAngle = 0.0
    def loadImage(self, filePath):
        self.imagePath = filePath
        self.imageSurface = pygame.image.load(self.imagePath)
    def flipImage(self, flipX, flipY):
        self.flipImageX = flipX
        self.flipImageY = flipY
        self.imageSurface = pygame.transform.flip(self.imageSurface, self.flipImageX, self.flipImageY)
    def scaleImage(self, scaleX, scaleY):
        self.scaleImageX = scaleX
        self.scaleImageY = scaleY
        self.imageSurface = pygame.transform.scale(self.imageSurface, (self.scaleImageX, self.scaleImageY))
    def rotateImage(self, angle):
        self.rotateImageAngle = float(angle)
        if self.rotateImageAngle >= 360:
            self.rotateImageAngle = 0.0
        self.imageSurface = pygame.transform.rotate(self.imageSurface, self.rotateImageAngle)
    def displayImage(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.imageSurface, (x, y))

# Implementation
player = AssetImage()
player.loadImage("assets/images/1.png")
player.flipImage(True, False)
player.scaleImage(150, 200)
player.rotateImage(155.0)
xx = 50
angle = 0.0
# Game Loop
isRunning = True
while isRunning:
    player.displayImage(screen, 100, 100)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                angle += 10.0

        if event.type == pygame.KEYUP:
            angle += 0
        if event.type == pygame.QUIT:
            isRunning = False
    pygame.display.update()
pygame.quit()