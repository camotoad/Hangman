from getword import read_web
from game import drawtext
import pygame
import sys
from pygame.locals import *
import math

# colours
color_black = (0, 0, 0)
color_white = (255, 255, 255)

# fonts
DISPLAY_FONT = pygame.font.SysFont('comicsans', 60)
LETTER_FONT = pygame.font.SysFont('comicsans', 40)


class Controller:
    A = 65
    GAP = 15
    RADIUS = 20
    startx = 40
    starty = 400

    def __init__(self):
        self.guessed = []
        self.correct = []
        self.wrong = []
        self.errors = 0
        self.word = read_web()
        self.wl = len(self.word)
        self.key = list(self.word)
        self.gameState = None
        self.display = "_" * self.wl
        self.MAX_ATTEMPTS = 6

        self.letters = []
        for i in range(26):
            x = self.startx + self.GAP * 2 + ((self.RADIUS * 2 + self.GAP) * (i % 13))  # reset row if 13th letter+
            y = self.starty + ((i // 13) * self.GAP + self.RADIUS * 2)  # next row if 13th letter+
            self.letters.append([x, y, chr(self.A + i), True])

        for i in range(7):
            image = pygame.image.load("hangman" + str(i) + ".png")
            self.images.append(image)

    def get_word(self):
        print(f"{self.word}, {self.wl}")
        return self.word

    def insert(self, guess):
        self.guessed += guess
        for letter in self.word:
            if letter in self.guessed:
                self.display += letter
                if self.word.count(letter) > self.correct.count(letter):
                    self.correct.append(letter)
                    self.wl -= 1
            else:
                self.display += "_"

        for letter in self.guessed:
            if letter not in self.word and letter not in self.wrong:
                self.errors += 1
                self.wrong.append(letter)

    def check_GameState(self):
        if sorted(self.correct) == sorted(self.key):
            print("Game win")
            gameState = True
            return gameState
        elif self.errors == self.MAX_ATTEMPTS:
            print(f"Game Over! \nRan out of tries\n The word was {self.word}")
            gameState = False
            return gameState
        else:
            gameState = None
            return gameState

    def draw(self, win):
        win.fill(color_white)

        # draw word
        drawtext(self.display, DISPLAY_FONT, color_black, win, 400, 200)

        # draw buttons
        for letter in self.letters:
            x, y, char, visible = letter
            if visible:
                pygame.draw.circle(win, color_black, (x, y), self.RADIUS, 3)
                text = LETTER_FONT.render(char, 1, color_black)
                win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        # draw picture
        win.blit(self.images[self.errors], (150, 100))
