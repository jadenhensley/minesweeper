import pygame
from pygame import font

pygame.font.init()
normal_font = pygame.font.SysFont('Roboto Bold', 30)
small_font = pygame.font.SysFont('Roboto Bold', 26)

def draw_text(surface, text, font, text_col, x, y):
    
    img = font.render(text, True, text_col)
    surface.blit(img,(x, y))
    
    words = ['']
    count = 0
    linecount = 0
