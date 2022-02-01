import string
import random
from translate import translate_word
from randomly import randoml
from display import displays



def main():
    try:
        print(translate_word())
    except AttributeError:
        print("Group ERROR, can't translate the phrase")

    randomly = randoml()
    print("Try to guess any letter:")
    word = ["_" for i in range(len(randomly))]
    print(" ".join(word))

    letters = [i for i in randomly]
    for i in range(8):
        letters.append(random.choice(string.ascii_uppercase))
    letters = " ".join(set(letters))
    print(letters)
    guessCount = 0
    displays(randomly, word, letters, guessCount)


if __name__ == "__main__":
    main()