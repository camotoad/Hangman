from getword import read_text, read_web

# word = read_text(15)  # read from text file
word = read_web()
wl = len(word)  # word length
MAX_ATTEMPTS = 6
# print(wl)

guessed = []
wrong = []
correct = []
gameState = True
key = list(word)
errors = 0
print(f"There are {wl} letters")
display = "_" * wl
print(display)

while gameState:
    input1 = ""
    input1 = input()
    if input1 != "" and input1 not in guessed:
        guessed += input1
    else:
        print(f"You have already guessed {input1}")
        continue
    display = ""
    for letter in word:     # checking for correct letters
        if letter in guessed:
            display += letter
            if word.count(letter) > correct.count(letter):
                correct += letter
                wl -= 1
        else:
            display += "_"
    for letter in guessed:      # checking for wrong letters
        if letter not in word and letter not in wrong:
            errors += 1
            wrong += letter

    print(f"{display}\n"
          f"Letters left: {wl}\n"
          f"Correct: {correct}\n"
          f"Wrong: {wrong}\n"
          f"Guessed: {guessed}\n"
          f" Errors: {errors}/{MAX_ATTEMPTS}")

    if sorted(correct) == sorted(key):
        print("Game win")
        gameState = False
    elif errors == MAX_ATTEMPTS:
        print(f"Game Over! \nRan out of tries\n The word was {word}")
        gameState = False
