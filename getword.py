import random
from bs4 import BeautifulSoup
import requests


MAXWORDS = 10000    # amount of words in the text file


def read_text():
    f = open("words.txt")
    words = f.readlines()
    lineToRead = random.randint(1, MAXWORDS)
    # print(words[lineToRead])
    word = words[lineToRead]
    if len(word) > 4:      # no 2 lettered or lower words preferably
        return word[:-1]  # return word without \n from text file
    # print(f"<2 letter {word}")
    return read_text()


def read_web():
    try:
        response = requests.get('http://randomword.com')
        soup = BeautifulSoup(response.text, 'html.parser')
        line = soup.find(id='random_word')
        word = line.string
        # print(word)
        return word
    except:
        print("Error retrieving word online")
        print("Taking a random word from words.txt")
        read_text()


"""
test = read_text()
print(test)
print(list(test))
"""