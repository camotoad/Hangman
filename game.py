import pygame
import sys
from pygame.locals import *
from controller import Controller


pygame.init()
mainClock = pygame.time.Clock()
pygame.font.init()

# colours
color_black = (0, 0, 0)
color_white = (255, 255, 255)

# fonts
TITLE_FONT = pygame.font.SysFont("comicsans", 60)
BUTTON_FONT = pygame.font.SysFont("comicsans", 40)


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
    screen = pygame.display.set_mode((300, 250))
    buttonPlay = pygame.Rect(50, 175, 150, 50)
    buttonPlay.center = (screen.get_width()/2, 175)
    pygame.display.set_caption('Main Menu')

    while True:
        screen.fill(color_white)
        pygame.draw.rect(screen, color_black, buttonPlay)

        drawTextCentered('PLAY', color_white, BUTTON_FONT, screen, screen.get_width() / 2, buttonPlay.y + buttonPlay.height / 2)
        drawTextCentered('HANGMAN', color_black, TITLE_FONT, screen, screen.get_width() / 2, 55)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if buttonPlay.collidepoint((mx, my)):
                    main_game()

        pygame.display.update()
        mainClock.tick(60)


def main_game():
    screen2 = pygame.display.set_mode((800, 500), 0, 32)
    pygame.display.set_caption('Hangman Game')
    running = True

    # init game controller
    gc = Controller()
    while running:
        gc.draw(screen2)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.set_mode((300, 250))
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.set_mode((300, 250))
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # print(f"clicked x:{mx}, y:{my}")
                for letter in gc.letters:
                    x, y, char = letter
                    if char not in gc.wrong:
                        if (x + gc.get_radius()) > mx > (x - gc.get_radius()) \
                                and (y + gc.get_radius()) > my > (y - gc.get_radius()):
                            # print(f"Clicked {char}")
                            gc.insert(char)

        if gc.check_GameState():
            screen2.fill(color_white)
            drawTextCentered("You win! The word was " + gc.get_word(), color_black, TITLE_FONT,
                             screen2, screen2.get_width()/2, screen2.get_height()/2)
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.display.set_mode((300, 250))
            running = False
        elif gc.check_GameState() == False:
            screen2.fill(color_white)
            drawTextCentered("You Lose! The word was " + gc.get_word(), color_black, TITLE_FONT,
                             screen2, screen2.get_width() / 2, screen2.get_height() / 2)
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.display.set_mode((300, 250))
            running = False
        else:
            pass

        pygame.display.update()
        mainClock.tick(60)

main_menu()