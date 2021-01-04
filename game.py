from readword import get_word

word = get_word(15)
wl = len(word)  # word length
#print(wl)

guessed = []
wrong = []
correct = []
gameState = True
key = list(dict.fromkeys(word))
print(f"There are {wl} letters")

while gameState:
    input1 = ""
    input1 = input()
    if input1 != "" and input1 not in guessed:
        guessed += input1
    else:
        continue
    for letter in guessed:
        if letter in word:
            if letter not in correct:
                correct += letter
            #print(f"{letter} is in {word}")
        else:
            if letter not in wrong:
                wrong += letter
            #print(f"{letter} is NOT in {word}")
    wl -= 1
    print(f"Correct: {correct}\n Wrong: {wrong}\n Guessed: {guessed}\nLetters left: {wl}")

    if sorted(correct) == sorted(key):
        print("Game win")
        gameState = False
