from asyncio.windows_events import NULL
import pygame
import tkinter as tk
from fonts import Text


# Global Properties
# Defaults
gameWindowWidth = 800
gameWindowHeight = 600
gameWindowTitle = "Eunoia"
gameWindowIcon = pygame.image.load("defaults/icons/E_Logo.png")
curFontXPos = 0
curFontYPos = 0
curText = "Eunoia"
curFontSize = 10
curIsBold = False
curIsItalics = False
curIsUnderlined = False
curFGColor = (255, 255, 255)
curBGColor = (0, 0, 0)    
curFontPath = "defaults/fonts/VT323-Regular.ttf"
gameFonts = []

# Get All Properties
def getGameProperties():
    global gameWindowWidth, gameWindowHeight, gameWindowTitle, gameWindowIcon
    global curFontXPos, curFontYPos, curText, curFontSize, curIsBold, curIsItalics, curIsUnderlined, curFGColor, curBGColor, curFontPath

    # User Inputs
    global windowWidthE, windowHeightE, windowTitleE, windowIconE
    global spriteXPosE, spriteYPosE, spriteWidthE, spriteHeightE, spriteFlipXE, spriteFlipYE, spriteRotationE, spriteOpacityE, spritePathE

    #? Get Window Properties
    # Get Width and Height
    if windowWidthE.get() != "" and windowWidthE.get() != " " and windowWidthE.get() != NULL:
        gameWindowWidth = int(windowWidthE.get())
    if windowHeightE.get() != "" and windowHeightE.get() != " " and windowHeightE.get() != NULL:
        gameWindowHeight = int(windowHeightE.get())
    # Get window title
    if windowTitleE.get() != "" and windowTitleE.get() != " " and windowTitleE.get() != NULL:
        gameWindowTitle = windowTitleE.get()
    # Get Window Icon
    if windowIconE.get() != "" and windowIconE.get() != " " and windowIconE.get() != NULL:
        gameWindowIcon = pygame.image.load(windowIconE.get())

    #? Get Font Properties
    # Create New Font Object 
    pygame.init()
    newFontObj = Text()
    newFontObj.textPosition(curFontXPos, curFontYPos)
    newFontObj.setText(curText)
    newFontObj.setFontSize(curFontSize)
    newFontObj.setBold(curIsBold)
    newFontObj.setItalics(curIsItalics)
    newFontObj.setUnderline(curIsUnderlined)
    newFontObj.setFGColor(curFGColor)
    newFontObj.setBGColor(curBGColor)
    newFontObj.setFont(curFontPath)
    gameFonts.append(newFontObj)
    pygame.quit()

#! Run Game
isGameRunning = False
def runGame():
    global isGameRunning
    global gameWindowWidth, gameWindowHeight, gameWindowTitle, gameWindowIcon
    # Init
    getGameProperties()
    pygame.init()
    # Game Loop
    isGameRunning = True
    screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
    pygame.display.set_caption(gameWindowTitle)
    pygame.display.set_icon(gameWindowIcon)
    while isGameRunning:
        for texts in gameFonts:
            texts.displayText(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
    pygame.quit()

# Add New Sprite
def addNewSprite():
    pass

# Add New Font
def addNewfont():
    global curFontXPos, curFontYPos, curText, curFontSize, curIsBold, curIsItalics, curIsUnderlined, curFGColor, curBGColor, curFontPath
    global fontXPosE, fontYPosE, fontTextE, fontSizeE, fontIsUnderlinedE, fontIsBoldE, fontIsItalicsE, fontFGColorE, fontBGColorE, fontPathE

    #? Get Font Properties
    # Get Font X and Y Pos
    if fontXPosE.get() != "" and fontXPosE.get() != " " and fontXPosE.get() != NULL:
        curFontXPos = int(fontXPosE.get())
    if fontYPosE.get() != "" and fontYPosE.get() != " " and fontYPosE.get() != NULL:
        curFontYPos = int(fontYPosE.get())
    # Get Text
    if fontTextE.get() != "" and fontTextE.get() != " " and fontTextE.get() != NULL:
        curText = fontTextE.get()
    # Get Font Size
    if fontSizeE.get() != "" and fontSizeE.get() != " " and fontSizeE.get() != NULL:
        curFontSize = int(fontSizeE.get())
    # Get Font Style Bold
    if fontIsBoldE.get() != "" and fontIsBoldE.get() != " " and fontIsBoldE.get() != NULL:
        curIsBold = fontIsBoldE.get()
    # Get Font Style Italics
    if fontIsItalicsE.get() != "" and fontIsItalicsE.get() != " " and fontIsItalicsE.get() != NULL:
        curIsItalics = fontIsItalicsE.get()
    # Get Font Style Underline
    if fontIsUnderlinedE.get() != "" and fontIsUnderlinedE.get() != " " and fontIsUnderlinedE.get() != NULL:
        curIsUnderlined = fontIsUnderlinedE.get()
    # Get FG Color
    if fontFGColorE.get() != "" and fontFGColorE.get() != " " and fontFGColorE.get() != NULL:
        curFGColor = fontFGColorE.get()
    # Get BG Color
    if fontBGColorE.get() != "" and fontBGColorE.get() != " " and fontBGColorE.get() != NULL:
        curBGColor = fontBGColorE.get()
    # Get Font Path
    if fontPathE.get() != "" and fontPathE.get() != " " and fontPathE.get() != NULL:
        curFontPath = fontPathE.get()

# UI
# Window Properties
def windowProperties():
    global windowWidthE, windowHeightE, windowTitleE, windowIconE
    # Frame
    windowPropertiesF = tk.Frame(root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
    windowPropertiesF.grid(row = 1, column = 0, columnspan=2)
    windowPropertiesL = tk.Label(windowPropertiesF, text="Window Properties")
    windowPropertiesL.grid(row = 0, column = 0, columnspan=2)
    # Window Width and Height
    windowWidthL = tk.Label(windowPropertiesF, text="Width: ")
    windowWidthL.grid(row = 1, column = 0)
    windowWidthE = tk.Entry(windowPropertiesF)
    windowWidthE.grid(row = 1, column = 1)
    windowHeightL = tk.Label(windowPropertiesF, text="Height: ")
    windowHeightL.grid(row = 2, column = 0)
    windowHeightE = tk.Entry(windowPropertiesF)
    windowHeightE.grid(row = 2, column = 1)
    # Window Title
    windowTitleL = tk.Label(windowPropertiesF, text="Game Title: ")
    windowTitleL.grid(row = 3, column = 0)
    windowTitleE = tk.Entry(windowPropertiesF)
    windowTitleE.grid(row = 3, column = 1)
    # Window Icon
    windowIconL = tk.Label(windowPropertiesF, text="Game Icon Path: ")
    windowIconL.grid(row = 4, column = 0)
    windowIconE = tk.Entry(windowPropertiesF)
    windowIconE.grid(row = 4, column = 1)

# Sprite Properties
def sprites():
    global spriteXPosE, spriteYPosE, spriteWidthE, spriteHeightE, spriteFlipXE, spriteFlipYE, spriteRotationE, spriteOpacityE, spritePathE
    spritePropertiesF = tk.Frame(root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
    spritePropertiesF.grid(row = 2, column = 0)
    spritePropertiesL = tk.Label(spritePropertiesF, text="Sprite Properties")
    spritePropertiesL.grid(row = 0, column = 0, columnspan = 2)
    # sprite xPos and yPos
    spriteXPosL = tk.Label(spritePropertiesF, text="xPos: ")
    spriteXPosL.grid(row = 1, column = 0)
    spriteXPosE = tk.Entry(spritePropertiesF)
    spriteXPosE.grid(row = 1, column = 1)
    spriteYPosL = tk.Label(spritePropertiesF, text="yPos: ")
    spriteYPosL.grid(row = 2, column = 0)
    spriteYPosE = tk.Entry(spritePropertiesF)
    spriteYPosE.grid(row = 2, column = 1)
    # sprite Width and Height
    spriteWidthL = tk.Label(spritePropertiesF, text="Width: ")
    spriteWidthL.grid(row = 3, column = 0)
    spriteWidthE = tk.Entry(spritePropertiesF)
    spriteWidthE.grid(row = 3, column = 1)
    spriteHeightL = tk.Label(spritePropertiesF, text="Height: ")
    spriteHeightL.grid(row = 4, column = 0)
    spriteHeightE = tk.Entry(spritePropertiesF)
    spriteHeightE.grid(row = 4, column = 1)
    # sprite FlipX and FlipY
    spriteFlipXL = tk.Label(spritePropertiesF, text="FlipX: ")
    spriteFlipXL.grid(row = 5, column = 0)
    spriteFlipXE = tk.Entry(spritePropertiesF)
    spriteFlipXE.grid(row = 5, column = 1)
    spriteFlipYL = tk.Label(spritePropertiesF, text="FlipY: ")
    spriteFlipYL.grid(row = 6, column = 0)
    spriteFlipYE = tk.Entry(spritePropertiesF)
    spriteFlipYE.grid(row = 6, column = 1)
    # sprite Angle
    spriteRotationL = tk.Label(spritePropertiesF, text="Angle: ")
    spriteRotationL.grid(row = 7, column = 0)
    spriteRotationE = tk.Entry(spritePropertiesF)
    spriteRotationE.grid(row = 7, column = 1)
    # sprite Opacity
    spriteOpacityL = tk.Label(spritePropertiesF, text="Opacity: ")
    spriteOpacityL.grid(row = 8, column = 0)
    spriteOpacityE = tk.Entry(spritePropertiesF)
    spriteOpacityE.grid(row = 8, column = 1)
    # sprite Path
    spritePathL = tk.Label(spritePropertiesF, text="Sprite Path: ")
    spritePathL.grid(row = 9, column = 0)
    spritePathE = tk.Entry(spritePropertiesF)
    spritePathE.grid(row = 9, column = 1)
    # Add New sprite Button
    addSpriteB = tk.Button(spritePropertiesF, text="Add Sprite", command=addNewSprite)
    addSpriteB.grid(row = 10, column = 0, columnspan = 2)

# Font Properties
def fonts():
    global fontXPosE, fontYPosE, fontTextE, fontSizeE, fontIsUnderlinedE, fontIsBoldE, fontIsItalicsE, fontFGColorE, fontBGColorE, fontPathE
    fontPropertiesF = tk.Frame(root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
    fontPropertiesF.grid(row = 3, column = 0)
    fontPropertiesL = tk.Label(fontPropertiesF, text="Font Properties")
    fontPropertiesL.grid(row = 0, column = 0, columnspan = 2)
    # Font xPos and yPos
    fontXPosL = tk.Label(fontPropertiesF, text="xPos: ")
    fontXPosL.grid(row = 1, column = 0)
    fontXPosE = tk.Entry(fontPropertiesF)
    fontXPosE.grid(row = 1, column = 1)
    fontYPosL = tk.Label(fontPropertiesF, text="yPos: ")
    fontYPosL.grid(row = 2, column = 0)
    fontYPosE = tk.Entry(fontPropertiesF)
    fontYPosE.grid(row = 2, column = 1)
    # Text
    fontTextL = tk.Label(fontPropertiesF, text="Text: ")
    fontTextL.grid(row = 3, column = 0)
    fontTextE = tk.Entry(fontPropertiesF)
    fontTextE.grid(row = 3, column = 1)
    # Font Size
    fontSizeL = tk.Label(fontPropertiesF, text="Font Size: ")
    fontSizeL.grid(row = 4, column = 0)
    fontSizeE = tk.Entry(fontPropertiesF)
    fontSizeE.grid(row = 4, column = 1)
    # Font Is FG Color
    fontFGColorL = tk.Label(fontPropertiesF, text="FG Color: ")
    fontFGColorL.grid(row = 5, column = 0)
    fontFGColorE = tk.Entry(fontPropertiesF)
    fontFGColorE.grid(row = 5, column = 1)
    # Font Is BG Color
    fontBGColorL = tk.Label(fontPropertiesF, text="BG Color: ")
    fontBGColorL.grid(row = 6, column = 0)
    fontBGColorE = tk.Entry(fontPropertiesF)
    fontBGColorE.grid(row = 6, column = 1)
    # Font Is Bold
    fontIsBoldL = tk.Label(fontPropertiesF, text="Is Bold: ")
    fontIsBoldL.grid(row = 7, column = 0)
    fontIsBoldE = tk.Entry(fontPropertiesF)
    fontIsBoldE.grid(row = 7, column = 1)
    # Font Is Italics
    fontIsItalicsL = tk.Label(fontPropertiesF, text="Is Italics: ")
    fontIsItalicsL.grid(row = 8, column = 0)
    fontIsItalicsE = tk.Entry(fontPropertiesF)
    fontIsItalicsE.grid(row = 8, column = 1)
    # Font Is Underlined
    fontIsUnderlinedL = tk.Label(fontPropertiesF, text="Is Underlined: ")
    fontIsUnderlinedL.grid(row = 9, column = 0)
    fontIsUnderlinedE = tk.Entry(fontPropertiesF)
    fontIsUnderlinedE.grid(row = 9, column = 1)
    # Font Path
    fontPathL = tk.Label(fontPropertiesF, text="Font Path: ")
    fontPathL.grid(row = 10, column = 0)
    fontPathE = tk.Entry(fontPropertiesF)
    fontPathE.grid(row = 10, column = 1)
    # Add New Font Button
    addFontB = tk.Button(fontPropertiesF, text="Add font", command=addNewfont)
    addFontB.grid(row = 10, column = 0, columnspan = 2)


# Run Button
def runButton():
    runB = tk.Button(root, text="Run", command=runGame)
    runB.grid(row = 0, column = 0, columnspan = 2)



# Root Window
root = tk.Tk()
root.geometry("600x600")
root.title("Eunoia Engine")

# UI
windowProperties()
sprites()
fonts()
runButton()

# Mainloop
root.mainloop()