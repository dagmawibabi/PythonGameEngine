import pygame

# Init
#pygame.init()
#screen = pygame.display.set_mode((1200, 800))

class Text():
    def __init__(self):
        self.fontSize = 20
        self.fgColor = (255, 255, 255)
        self.bgColor = (0, 0, 0)
        self.fontPath = "defaults/fonts/Abel-Regular.ttf"
        self.text = "Eunoia Engine"
        self.fontObj = pygame.font.Font(self.fontPath, self.fontSize)
        self.textObj = self.fontObj.render(self.text, True, self.fgColor, self.bgColor)
        self.xPos = 10
        self.yPos = 10
        self.isBold = False
        self.isItalics = False
        self.isUnderlined = False
    def setFont(self, fontPath):
        self.fontPath = fontPath
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
    def setFontSize(self, fontSize):
        self.fontSize = fontSize
        self.fontObj = pygame.font.Font(self.fontPath, self.fontSize)
    def setFGColor(self, color):
        self.fgColor = color
    def setBGColor(self, color):
        self.bgColor = color
    def setText(self, text):
        self.text = text
    def textPosition(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
    def setBold(self, bold):
        self.isBold = bold
        self.fontObj.set_bold(self.isBold)
    def setItalics(self, italics):
        self.isItalics = italics
        self.fontObj.set_italic(self.isItalics)
    def setUnderline(self, underline):
        self.isUnderlined = underline
        self.fontObj.set_underline(self.isUnderlined)
    def getSystemFonts(self):
        return pygame.font.get_fonts()
    def getAllFonts(self):
        return pygame.font.get_fonts()
    def displayText(self, screen):
        self.textObj = self.fontObj.render(self.text, True, self.fgColor, self.bgColor)
        screen.blit(self.textObj, (self.x, self.y))
    def write(self, screen, text, fontPath, fontSize, fgColor, bgColor, xPos, yPos):
        self.text = text
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.fgColor = fgColor
        self.bgColor = fgColor
        self.xPos = xPos
        self.yPos = yPos
        self.setFont(fontPath)
        self.setFontSize(fontSize)
        self.setFGColor(fgColor)
        self.setBGColor(bgColor)
        self.setText(text)
        self.textPosition(xPos, yPos)
        self.setBold(self.isBold)
        self.setItalics(self.isItalics)
        self.setUnderline(self.isUnderlined)
        self.displayText(screen)


# Implementation
#sampleText = Text()
#sampleText.setUnderline(True)
#sampleText.setText("Hello World!")
#sampleText.setFontSize(30)
#sampleText.textPosition(20, 10)
#sampleText.displayText(screen)
#sampleText.write(screen, "Eunoia Engine", "defaults/fonts/VT323-Regular.ttf", 100, (255, 0, 255), (50, 100, 50), 10, 50)

# Game Loop
#isRun = True
#while isRun:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            isRun = False
#    pygame.display.update()
#
#pygame.quit()

