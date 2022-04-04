import pygame

# A class to load and display images
class Sprite():
    def __init__(self):
        self.spritePath = "defaults/images/1.png"
        self.xPos = 0
        self.yPos = 0
        self.width = 100
        self.height = 100
        self.xFlip = False
        self.yFlip = False
        self.rotationAngle = 0.0
        self.spriteObject = pygame.image.load(self.spritePath)
    def loadSprite(self, spritePath):
        self.spritePath = spritePath
        self.spriteObject = pygame.image.load(self.spritePath)
    def positionSprite(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    def scaleSprite(self, width, height):
        self.width = width
        self.height = height
        self.spriteObject = pygame.transform.scale(self.spriteObject, (self.width, self.height))
    def flipSprite(self, xFlip, yFlip):
        self.xFlip = xFlip
        self.yFlip = yFlip
        self.spriteObject = pygame.transform.flip(self.spriteObject, self.xFlip, self.yFlip)
    def rotateSprite(self, angle):
        self.rotationAngle = angle
        self.spriteObject = pygame.transform.rotate(self.spriteObject, self.rotationAngle)
    def displaySprite(self, screen):
        self.spriteObject = pygame.image.load(self.spritePath)
        self.spriteObject = pygame.transform.flip(self.spriteObject, self.xFlip, self.yFlip)
        self.spriteObject = pygame.transform.scale(self.spriteObject, (self.width, self.height))
        self.spriteObject = pygame.transform.rotate(self.spriteObject, self.rotationAngle)
        screen.blit(self.spriteObject, (self.xPos, self.yPos))
    def showSprite(self, screen, spritePath, xPos, yPos, width, height, xFlip, yFlip, rotationAngle):
        self.loadSprite(spritePath)
        self.positionSprite(xPos, yPos)
        self.scaleSprite(width, height)
        self.flipSprite(xFlip, yFlip)
        self.rotateSprite(rotationAngle)
        self.displaySprite(screen)
 

# Init
pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Implementation
sampleSprite = Sprite()
# Implementation - Separated
sampleSprite.loadSprite("defaults/images/1.png")
sampleSprite.positionSprite(100, 200)
sampleSprite.scaleSprite(200, 200)
sampleSprite.flipSprite(False, True)
sampleSprite.rotateSprite(45.0)
sampleSprite.displaySprite(screen)
# Implementation - One Liner
sampleSprite.showSprite(screen, "defaults/images/1.png", 100, 100, 150, 150, False, False, 0.0)

# Game Loop
isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    pygame.display.update()
pygame.quit()


