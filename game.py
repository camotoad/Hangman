from getword import read_web
import pygame
import sys
from pygame.locals import *


pygame.init()
mainClock = pygame.time.Clock()
pygame.font.init()

# colours
color_black = (0, 0, 0)
color_white = (255, 255, 255)

# fonts
title = pygame.font.SysFont("comicsans", 60)
font1 = pygame.font.SysFont("comicsans", 40)


def drawtext(text, font, color, win, x, y):
    textObj = font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    win.blit(textObj, textRect)


def drawTextCentered(text, color, font, display, x, y):
    def text_objects():
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    textSurf, textRect = text_objects()
    textRect.center = (x, y)
    display.blit(textSurf, textRect)


def main_menu():
    screen = pygame.display.set_mode((300, 250), 0, 32)
    buttonPlay = pygame.Rect(50, 175, 150, 50)
    buttonPlay.center = (screen.get_width()/2, 175)
    pygame.display.set_caption('Main Menu')

    clicked = False
    while True:
        screen.fill(color_white)
        pygame.draw.rect(screen, color_black, buttonPlay)

        drawTextCentered('PLAY', color_white, font1, screen, screen.get_width()/2 , buttonPlay.y + buttonPlay.height/2)
        drawTextCentered('HANGMAN', color_black, title, screen, screen.get_width()/2, 55)
        pygame.display.update()

        mx, my = pygame.mouse.get_pos()

        if buttonPlay.collidepoint((mx, my)):
            if clicked:
                pass
        clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True

        pygame.display.update()
        mainClock.tick(60)

main_menu()