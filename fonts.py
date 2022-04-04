import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((1200, 800))

class Text():
    def __init__(self):
        self.fontSize = 20
        self.color = (255, 255, 255)
        self.fontPath = "defaults/fonts/Abel-Regular.ttf"
        self.text = "Eunoia Engine"
        self.fontObj = pygame.font.Font(self.fontPath, self.fontSize)
        self.textObj = self.fontObj.render(self.text, True, self.color)
        self.xPos = 10
        self.yPos = 10
    def setFont(self, fontPath):
        self.fontPath = fontPath
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
    def setFontSize(self, fontSize):
        self.fontSize = fontSize
        self.fontObj = pygame.font.Font(self.fontPath, self.fontSize)
    def setColor(self, color):
        self.color = color
    def setText(self, text):
        self.text = text
    def setPosition(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
    def displayText(self, screen):
        self.textObj = self.fontObj.render(self.text, True, self.color)
        screen.blit(self.textObj, (self.x, self.y))
    def write(self, screen, text, fontPath, fontSize, fontColor, xPos, yPos):
        self.text = text
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.xPos = xPos
        self.yPos = yPos
        self.setFont(fontPath)
        self.setFontSize(fontSize)
        self.setColor(fontColor)
        self.setText(text)
        self.setPosition(xPos, yPos)
        self.displayText(screen)


# Implementation
newText = Text()
newText.setText("Hello World!")
newText.setFontSize(30)
newText.setPosition(10, 10)
newText.displayText(screen)
newText.write(screen, "Eunoia Engine", "defaults/fonts/Abel-Regular.ttf", 100, (255, 0, 255), 10, 30)

# Game Loop
isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    pygame.display.update()

pygame.quit()

