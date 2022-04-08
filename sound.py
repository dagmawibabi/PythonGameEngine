from numpy import place
import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1200, 800))

class Sound():
    def __init__(self, filepath):
        self.sound = pygame.mixer.Sound(filepath)

    def getSound(self):
        return self.sound

    def setSound(self, filepath):
        self.sound = pygame.mixer.Sound(filepath)
    
    def play(self):
        self.sound.play()
    
    def stop(self, fadeout=0):
        self.stop(fadeout)

    def getLength(self):
        return self.sound.get_length()

    def setVolume(self, volume):
        self.sound.set_volume(volume)

sound = Sound("defaults/sounds/testSound.wav")

played = False
isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound.play()

    pygame.display.update()

pygame.mixer.quit()
pygame.quit()