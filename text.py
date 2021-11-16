import pygame
from pygame import font

pygame.font.init()
normal_font = pygame.font.SysFont('Roboto Bold', 30)
small_font = pygame.font.SysFont('Roboto Bold', 26)

def draw_text(surface, text, font, text_col, x, y, span_vertically=True):
    if not span_vertically:
        img = font.render(text, True, text_col)
        surface.blit(img,(x, y))
    words = ['']
    count = 0
    linecount = 0
    if span_vertically:
        for letter in text:
            if letter != ' ':
                words[count] += letter
            else:
                words.append('')
                count += 1
        count = 0
        for word in words:
            img = font.render(word, True, text_col)
            surface.blit(img, (x, y + (linecount * 30)))
            # count += 1
            linecount += 1
            # if words.index(word) % 3 == 0:
            #     count = 0
            #     linecount += 1
            
