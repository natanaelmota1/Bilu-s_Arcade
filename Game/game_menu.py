import pygame
import os
import sys
from game_play import game
from game_credits import credit
from sounds import *


def menu():
    # Inicialização do módulo de música
    pygame.mixer.pre_init(48000, -16, 2, 512)

    # Inicialização do módulo
    pygame.init()

    # Música e som do menu
    menu_song = "sounds/menu_song.mp3"
    selection = "sounds/selection.ogg"

    play_song(menu_song)

    # Definindo cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # Parâmetros da tela
    width = 800
    height = 700

    # Texto
    def write_text(text, color, posx, posy, font, size):
        font = pygame.font.SysFont(font, size)
        text1 = font.render(text, True, color)
        screen.blit(text1, [posx, posy])

    # Interface
    rect_pos_x = (width/2)-100
    rect_pos_y = (height/2)-35
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bilu's Arcade")
    FPS = pygame.time.Clock()
    background = pygame.image.load("sprites/menu_background.jpg").convert()

    on_menu = True

    while (on_menu):
        # Eventos
        for event in pygame.event.get():
            # Condição de saída
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    on_menu = False
            if event.type == pygame.QUIT:
                on_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and rect_pos_y == height1:
                    game()
                    on_menu = False
                if event.key == pygame.K_RETURN and rect_pos_y == height2:
                    credit()

        height1 = (height/2)-35
        height2 = (height/2)+35

        # Seleção do menu
        pygame.draw.rect(screen, blue, [rect_pos_x, rect_pos_y, 200, 70], 3)
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            rect_pos_y = height1
            play_sound(selection)
        if key[pygame.K_DOWN]:
            rect_pos_y = height2
            play_sound(selection)
        write_text("PLAY", white, (width/2)-71, (height/2)-25, "stencil", 80)
        write_text("CREDITS", white, (width/2)-88.5,
                   (height/2)+55, "stencil", 59)
        pygame.display.update()
        screen.blit(background, (0, 0))
        FPS.tick(25)


menu()
