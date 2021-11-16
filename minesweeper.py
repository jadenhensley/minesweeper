import pygame
from pygame.locals import *
from gtts import gTTS
import os, sys
from button import Button
from text import draw_text
from math import ceil

import path_util  # needed for getting path of project media files, when script is ran remotely.

PROJECT_PATH = path_util.get_project_directory()
print(PROJECT_PATH)


pygame.init()
pygame.display.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# loading in fonts
pygame.font.init()

FONT = pygame.font.SysFont("Sans", 20)

roboto_large = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 72)
roboto_medium = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 24)
roboto_small = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 20)
roboto_italic_medium = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-BoldItalic.ttf', 28)
roboto_italic_small = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-BoldItalic.ttf', 18)

# Circle and GUI colors
GREEN = pygame.Color("#57CC99")
GREEN_IN = pygame.Color("#80ED99")
BLUE = pygame.Color("#0F4C75")
BLUE_IN = pygame.Color("#3282B8")
RED = pygame.Color("#B42B51")
RED_IN = pygame.Color("#E63E6D")
PURPLE = pygame.Color("#52057B")
PURPLE_IN = pygame.Color("#892CDC")
YELLOW = pygame.Color("#FDA65D")
YELLOW_IN = pygame.Color("#FFD07F")

GRAY = pygame.Color("#525252")
DARKGRAY = pygame.Color("#414141")
DARK = pygame.Color("#171010")
SILVER = pygame.Color("#EEEEEE")

BG_PURPLE = pygame.Color("#1F002E")
# BG_COLOR = BG_PURPLE
BG_COLOR = DARK
TEXT_COLOR = pygame.Color('#50A14F')


# sound group (for stopping / unloading all sounds simultaneously,
# when exiting a scene, regardless of the scene that is quit.
# Prevents having to manually do it.)
sounds_group = []
# Loading in sound wav files
WAV_CLICK = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/click_tile.wav')
WAV_ONE.set_volume(0.3)
sounds_group.append(WAV_ONE)
WAV_MINE = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/click_mine.wav')
WAV_MINE.set_volume(0.3)
sounds_group.append(WAV_MINE)
WAV_CLEAR = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/click_mine.wav')
WAV_CLEAR.set_volume(0.3)



    render_navbar()

    pygame.display.update()
    clock.tick(60)

pygame.quit()