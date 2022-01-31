import string
import random
from randomly import randoml
from display import displays



def main():
    randomly = randoml()
    print("Try to guess any letter:")
    word = ["_" for i in range(len(randomly))]
    print(" ".join(word))

    letters = [i for i in randomly]
    for i in range(8):
        letters.append(random.choice(string.ascii_uppercase))
    letters = " ".join(set(letters))
    print(letters)
    displays(randomly, word, letters)


if __name__ == "__main__":
    main()