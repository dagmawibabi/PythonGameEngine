import pygame
import tkinter as tk
from assetImage import *

# Root Window
root = tk.Tk()
root.geometry("900x600")
root.title("Game Engine")

# List Of Assets
listOfAssets = []
# Functions
def runGame():
    # Get Window Properties
    # Get Window Title and Icon Path
    windowIconPath = windowIconE.get()
    windowTitle = windowTitleE.get()
    # Get Window Width and Height
    windowWidth = int(windowWidthE.get())
    windowHeight = int(windowHeightE.get())    

    # Make Game
    pygame.init()
    # Set Window Properties
    windowIcon = pygame.image.load(windowIconPath)
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption(windowTitle)
    pygame.display.set_icon(windowIcon)
    for i in range(0, len(listOfAssets) - 1):
        listOfAssets[i].displayImage(screen)
        print(listOfAssets[i].x)
        pygame.display.update()

def addNewAssetImage():
    print(listOfAssets)
    # Asset Properties
    # Get Asset Path
    assetPath = assetImagePathE.get()
    # Get Asset Width and Height
    assetWidth = int(assetImageWidthE.get())
    assetHeight = int(assetImageHeightE.get())
    # Get Asset X and Y Postion
    assetXPos = int(assetImageXPosE.get())
    assetYPos = int(assetImageYPosE.get())
    # Set Asset Properties 
    asset = pygame.image.load(assetPath)
    asset = AssetImage()
    asset.loadImage(assetPath)
    asset.setImagePostion(assetXPos, assetYPos)
    asset.scaleImage(assetWidth, assetHeight)
    # Add into Assets List
    listOfAssets.append(asset)

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


# Run Game
runGameF = tk.Frame(root, highlightbackground="black", highlightthickness=1, padx=20, pady=15)
runGameF.grid(row = 100, column = 0)
runGameB = tk.Button(runGameF, text="Run", command=runGame)
runGameB.grid(row = 0, column = 0)

# Main Loop
root.mainloop()