import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Loads images, and animates them

class soundMusic():
    def __init__(self) -> None:
        pass

# Implementation


# Game Loop
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
        if event.type == pygame.KEYUP:
            pass
        if event.type == pygame.QUIT:
            isRunning = False
    pygame.display.update()
pygame.quit()