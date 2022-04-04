from multiprocessing import Event
from turtle import back, bgcolor
import pygame
import tkinter as tk
from sprites import *

# Root Window
root = tk.Tk()
root.geometry("900x600")
root.title("Eunoia Engine")
#root.config(background="black")
#root.wm_attributes("-transparentcolor", "white")

# Defaults
gameWindowDefaultIcon = "defaults/icons/E_Logo.png"
gameWindowDefaultWidth = 800
gameWindowDefaultHeight = 600
gameWindowDefaultTitle = "New Game"
defaultAssetImagePath = "defaults/images/1.png"
defaultAssetImageWidth = 100
defaultAssetImageHeight = 100
defaultAssetImageXPos = 10
defaultAssetImageYPos = 10

# List Of Assets
listOfAssets = []
listOfAssetLabels = []

# Functions
def runGame():
    # Get Window Properties
    # Get Window Title and Icon Path
    windowIconPath = windowIconE.get()
    windowTitle = windowTitleE.get()
    if windowTitle == "" or windowTitle == " " or windowTitle:
        windowTitle = gameWindowDefaultTitle
    # Get Window Width and Height
    try:
        windowWidth = int(windowWidthE.get())
    except:
        windowWidth = gameWindowDefaultWidth
    try:
        windowHeight = int(windowHeightE.get())    
    except:
        windowHeight = gameWindowDefaultHeight    

    # Make Game
    pygame.init()
    # Set Window Properties
    try:
        windowIcon = pygame.image.load(windowIconPath)
    except:
        windowIcon = pygame.image.load(gameWindowDefaultIcon)
    pygame.display.set_icon(windowIcon)
    pygame.display.set_caption(windowTitle)
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    for curAssets in listOfAssets:
        curAssets.displayImage(screen)
        pygame.display.update()

# Add Assets
assetRowNum = 0
assetColNum = 0
addRow = False

class newAssetImageLabel():
    def __init__(self, assetPath):
        self.varName = "imagePI"+str(len(listOfAssets))
        self.varName = tk.PhotoImage(file=assetPath)
        self.varName = self.varName.zoom(5) # I ended up running out of memory with 250
        self.varName = self.varName.subsample(32)

def addNewAssetImage():
    # Asset Properties
    # Get Asset Path
    assetPath = assetImagePathE.get()
    # Get Asset Width and Height
    try:
        assetWidth = int(assetImageWidthE.get())
    except:
        assetWidth = defaultAssetImageWidth
    try:
        assetHeight = int(assetImageHeightE.get())
    except:
        assetHeight = defaultAssetImageHeight
    # Get Asset X and Y Postion
    try:
        assetXPos = int(assetImageXPosE.get())
    except:
        assetXPos = defaultAssetImageXPos
    try:
        assetYPos = int(assetImageYPosE.get())
    except:
        assetYPos = defaultAssetImageYPos
    # Set Asset Properties 
    asset = Sprite()
    try:
        asset.loadImage(assetPath)
    except:
        asset.loadImage(defaultAssetImagePath)
    asset.setImagePostion(assetXPos, assetYPos)
    asset.scaleImage(assetWidth, assetHeight)
    # Add into Assets List
    listOfAssets.append(asset)
    newAssetLabel = newAssetImageLabel(assetPath)
    listOfAssetLabels.append(newAssetLabel)
    addNewAssetToUI()

def selectImageAsset(event):
    if event.widget["background"] == "white":
        event.widget.configure(background="aqua")
    else:
        event.widget.configure(background="white")

def addNewAssetToUI():
    # Add To UI
    global assetColNum, assetRowNum, addRow
    for i in listOfAssetLabels:
        imageL = tk.Label(subFrameAALF, image = i.varName,  borderwidth = 2, relief = "groove", width = 80, height = 80, background="white")
    imageL.grid(row = assetRowNum, column = assetColNum)
    imageL.bind("<Button-1>", selectImageAsset)

    # Display In Grid
    if addRow == False:
        addRow = True
        assetColNum += 1
    else:
        addRow = False
        assetRowNum += 1
        assetColNum = 0



# UI
#? Window Properties
windowPropertiesF = tk.Frame(root, highlightbackground="black", highlightthickness=1, padx=20, pady=15)
windowPropertiesF.grid(row = 0, column = 0)
windowPropertiesL = tk.Label(windowPropertiesF, text="Window Properties")
windowPropertiesL.grid(row = 0, column = 0)
# Window Width and Height
subFrameWPF = tk.Frame(windowPropertiesF)
subFrameWPF.grid(row = 1, column = 0)
# Window Title
windowTitleL = tk.Label(subFrameWPF, text="Title: ")
windowTitleL.grid(row = 0, column = 0)
windowTitleE = tk.Entry(subFrameWPF)
windowTitleE.grid(row = 0, column = 1)
# Window Width
windowWidthL = tk.Label(subFrameWPF, text="Width: ")
windowWidthL.grid(row = 1, column = 0)
windowWidthE = tk.Entry(subFrameWPF)
windowWidthE.grid(row = 1, column = 1)
# Window Height
windowHeightL = tk.Label(subFrameWPF, text="Height: ")
windowHeightL.grid(row = 2, column = 0)
windowHeightE = tk.Entry(subFrameWPF)
windowHeightE.grid(row = 2, column = 1)
# Window Icon
windowIconL = tk.Label(subFrameWPF, text="Icon Path: ")
windowIconL.grid(row = 3, column = 0)
windowIconE = tk.Entry(subFrameWPF)
windowIconE.grid(row = 3, column = 1)


#? Asset Properties
assetImagePropertiesF = tk.Frame(root, highlightbackground="black", highlightthickness=1, padx=20, pady=15)
assetImagePropertiesF.grid(row = 1, column = 0)
assetImagePropertiesL = tk.Label(assetImagePropertiesF, text="Asset Image Properties")
assetImagePropertiesL.grid(row = 0, column = 0)
# Asset Image Width and Height
subFrameAIPF = tk.Frame(assetImagePropertiesF)
subFrameAIPF.grid(row = 1, column = 0)
# Asset Image Path
assetImagePathL = tk.Label(subFrameAIPF, text="Path: ")
assetImagePathL.grid(row = 0, column = 0)
assetImagePathE = tk.Entry(subFrameAIPF)
assetImagePathE.grid(row = 0, column = 1)
# Asset Image Width
assetImageWidthL = tk.Label(subFrameAIPF, text="Width: ")
assetImageWidthL.grid(row = 1, column = 0)
assetImageWidthE = tk.Entry(subFrameAIPF)
assetImageWidthE.grid(row = 1, column = 1)
# Asset Image Height
assetImageHeightL = tk.Label(subFrameAIPF, text="Height: ")
assetImageHeightL.grid(row = 2, column = 0)
assetImageHeightE = tk.Entry(subFrameAIPF)
assetImageHeightE.grid(row = 2, column = 1)
# Asset Image Width
assetImageXPosL = tk.Label(subFrameAIPF, text="xPos: ")
assetImageXPosL.grid(row = 3, column = 0)
assetImageXPosE = tk.Entry(subFrameAIPF)
assetImageXPosE.grid(row = 3, column = 1)
# Asset Image Height
assetImageYPosL = tk.Label(subFrameAIPF, text="yPos: ")
assetImageYPosL.grid(row = 4, column = 0)
assetImageYPosE = tk.Entry(subFrameAIPF)
assetImageYPosE.grid(row = 4, column = 1)
addAssetB = tk.Button(subFrameAIPF, text="Add Asset", command=addNewAssetImage)
addAssetB.grid(row = 5, column = 0, columnspan = 2)

#? Added Assets
addedAssetsListsF = tk.Frame(root, highlightbackground="black", highlightthickness=1, padx=20, pady=15)
addedAssetsListsF.grid(row = 2, column = 0)
addedAssetsListsL = tk.Label(addedAssetsListsF, text="Added Assets")
addedAssetsListsL.grid(row = 0, column = 0)
subFrameAALF = tk.Frame(addedAssetsListsF, highlightbackground="black", highlightthickness=1, padx=20, pady=15)
subFrameAALF.grid(row = 1, column = 0)

# Run Game
runGameF = tk.Frame(root, highlightbackground="black", highlightthickness=1, padx=20, pady=15)
runGameF.grid(row = 100, column = 0)
runGameB = tk.Button(runGameF, text="Run", command=runGame)
runGameB.grid(row = 0, column = 0)

# Init
newAssetLabel = newAssetImageLabel(defaultAssetImagePath)
listOfAssetLabels.append(newAssetLabel)
addNewAssetToUI()


# Main Loop
root.mainloop()