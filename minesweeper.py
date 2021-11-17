import pygame
from pygame.locals import *
import os, sys
from button import Button
from text import draw_text
from math import ceil

import path_util  # needed for getting path of project media files, when script is ran remotely.
from random import choice


PROJECT_PATH = path_util.get_project_directory()

pygame.init()
pygame.display.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("minesweeper in pygame")
clock = pygame.time.Clock()


# loading in fonts
pygame.font.init()

FONT = pygame.font.SysFont("Sans", 20)

roboto_large = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 72)
roboto_medium = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 24)
roboto_small = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 20)
roboto_italic_medium = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-BoldItalic.ttf', 28)
roboto_italic_small = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-BoldItalic.ttf', 18)

# # Circle and GUI colors
# GREEN = pygame.Color("#57CC99")
# GREEN_IN = pygame.Color("#80ED99")
# BLUE = pygame.Color("#0F4C75")
# BLUE_IN = pygame.Color("#3282B8")
# RED = pygame.Color("#B42B51")
# RED_IN = pygame.Color("#E63E6D")
# PURPLE = pygame.Color("#52057B")
# PURPLE_IN = pygame.Color("#892CDC")
# YELLOW = pygame.Color("#FDA65D")
# YELLOW_IN = pygame.Color("#FFD07F")

# GRAY = pygame.Color("#525252")
# DARKGRAY = pygame.Color("#414141")
# DARK = pygame.Color("#171010")
# SILVER = pygame.Color("#EEEEEE")

# BG_PURPLE = pygame.Color("#1F002E")
# # BG_COLOR = BG_PURPLE
# BG_COLOR = DARK
# TEXT_COLOR = pygame.Color('#50A14F')


# # sound group (for stopping / unloading all sounds simultaneously,
# # when exiting a scene, regardless of the scene that is quit.
# # Prevents having to manually do it.)

# Loading in sound wav files

sounds_group = []

WAV_CLICK = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/click_tile.wav')
WAV_CLICK.set_volume(0.3)
sounds_group.append(WAV_CLICK)
WAV_MINE = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/click_mine.wav')
WAV_MINE.set_volume(0.3)
sounds_group.append(WAV_MINE)
WAV_CLEAR = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/click_mine.wav')
WAV_CLEAR.set_volume(0.3)
sounds_group.append(WAV_CLEAR)

# loading tile images
IMG_TILE_BLOCKED = pygame.image.load(f'{PROJECT_PATH}/img/tile_blocked.png')
IMG_TILE_0 = pygame.image.load(f'{PROJECT_PATH}/img/tile0.png')
IMG_TILE_1 = pygame.image.load(f'{PROJECT_PATH}/img/tile1.png')
IMG_TILE_2 = pygame.image.load(f'{PROJECT_PATH}/img/tile2.png')
IMG_TILE_3 = pygame.image.load(f'{PROJECT_PATH}/img/tile3.png')
IMG_TILE_4 = pygame.image.load(f'{PROJECT_PATH}/img/tile4.png')

TILESIZE = IMG_TILE_0.get_width()
LEVEL_WIDTH = 8
LEVEL_HEIGHT= 8
LEVEL_MINES = 20

USER_SCORE = 0

gameover = False
run = False

def print_map(tilemap):
    for row in tilemap:
        print(row)

def generate_map():
    global LEVEL_WIDTH, LEVEL_HEIGHT, LEVEL_MINES;
    width = LEVEL_WIDTH; height = LEVEL_HEIGHT; mines = LEVEL_MINES;
    
    possible = ['0','1','2','3','4']
    # '0' for clear, '4' for mines, else for numeral integers
    # by default, "blocked" tiles are layered on top of these tiles, for user to click
    tilemap = []
    mines = mines
    i = choice(possible)
    # tilemap.append(i)s
    for rowI in range(height):
        tilemap.append([])
        for columnI in range(width):
            tilemap[rowI].append('')

    for rowI in range(height):
        for columnI in range(width):
            t = choice(possible)
            if t == '4':
                if mines > 0:
                    tilemap[rowI][columnI] = '4'
                    mines -= 1
                else:
                    tilemap[rowI][columnI] = '1'
            else:
                tilemap[rowI][columnI] = t

    return tilemap

tilemap = generate_map()
# print_map(tilemap)

def render_tilemap(tilemap):
    global LEVEL_WIDTH, LEVEL_HEIGHT, LEVEL_MINES;
    global TILESIZE;
    width = LEVEL_WIDTH; height = LEVEL_HEIGHT; mines = LEVEL_MINES;

    for rowI in range(height):
        for columnI in range(width):
            render_tile(tilemap[rowI][columnI], rowI * TILESIZE, columnI*TILESIZE)

def render_tile(tile_type, pos_x, pos_y):
    if tile_type == '0':
        screen.blit(IMG_TILE_0, (pos_x, pos_y))
    if tile_type == '1':
        screen.blit(IMG_TILE_1, (pos_x, pos_y))
    if tile_type == '2':
        screen.blit(IMG_TILE_2, (pos_x, pos_y))
    if tile_type == '3':
        screen.blit(IMG_TILE_3, (pos_x, pos_y))
    if tile_type == '4':
        screen.blit(IMG_TILE_4, (pos_x, pos_y))

class Tile():
    def __init__(self, tile_type, pos_x, pos_y, surface=screen):
        global IMG_TILE_0, IMG_TILE_1, IMG_TILE_2, IMG_TILE_3, IMG_TILE_4, IMG_TILE_BLOCKED;
        self.tiles = (IMG_TILE_0, IMG_TILE_1, IMG_TILE_2, IMG_TILE_3, IMG_TILE_4, IMG_TILE_BLOCKED)
        if tile_type == '0':
            self.image = self.tiles[0]
        if tile_type == '1':
            self.image = self.tiles[1]
        if tile_type == '2':
            self.image = self.tiles[2]
        if tile_type == '3':
            self.image = self.tiles[3]
        if tile_type == '4':
            self.image = self.tiles[4]
        self.cover_image = self.tiles[5] # image for default tile state, before clicked.
        self.current_image = self.cover_image
        self.clicked = False
        self.x = pos_x
        self.y = pos_y
        self.rect = self.current_image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen = surface
    
    def click(self):
        global USER_SCORE
        self.current_image = self.image
        if self.clicked == False:
            WAV_CLICK.play()
            USER_SCORE += 1
            # print(USER_SCORE)
            self.clicked = True

    
    def draw(self):
        self.screen.blit(self.current_image, (self.x, self.y))

        # print(self.x)
        # print(self.y)
        self.screen.blit(collision, (self.x, self.y))


        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            # print('colliding')
            if pygame.mouse.get_pressed()[0] == 1:
                self.click()

                


def game_update():
    pass

def game_input():
    pass

def game_over():
    pass

run = True

def game_main():
    global run

    render_tilemap(tilemap)
    render_tile('1', 0*TILESIZE, 0*TILESIZE)
    render_tile('2', 1*TILESIZE, 1*TILESIZE)
    render_tile('3', 2*TILESIZE, 1*TILESIZE)
    render_tile('4', 3*TILESIZE, 1*TILESIZE)


    tile_group = []

    new = Tile('1', 64*0, 64)
    newb = Tile('2', 64*1, 64)
    newc = Tile('3', 64*2, 64)
    newd = Tile('4', 64*3, 64)
    tile_group.append(new)
    tile_group.append(newb)
    tile_group.append(newc)
    tile_group.append(newd)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if (key[pygame.K_LCTRL] or key[pygame.K_LALT]) and (key[pygame.K_q] or key[pygame.K_w]):
                    pygame.quit()
                    sys.exit()
                    quit()
                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()

        
        for tile in tile_group:
            tile.draw()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_main()