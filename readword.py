import random


def get_word(maxwords):
    f = open("words.txt")
    words = f.readlines()
    lineToRead = random.randint(0, maxwords) - 1
    #print(words[lineToRead])
    word = words[lineToRead]
    return word[:-1]
