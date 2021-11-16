import pygame
from pygame.locals import *

class Button():
    def __init__(self, surface, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.screen = surface

    def draw(self):
        action = False

        self.screen.blit(self.image, self.rect)

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            newimage = pygame.transform.scale(self.image, (int(self.image.get_width() * 1.2), int(self.image.get_height() * 1.2)))
            newrect = newimage.get_rect()
            newrect.x = self.rect.x
            newrect.y = self.rect.y
            self.screen.blit(newimage, newrect)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
        else:
            self.screen.blit(self.image, self.rect)
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action