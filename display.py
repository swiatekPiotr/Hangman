
def prompt(letters, word):
    letters = [i for i in letters if i not in word]
    print("".join(letters))


def displays(rand, word, letter, guessCount):
    guess = (input(">")).upper()
    for i in range(len(rand)):
        if rand[i] == guess:
            word[i] = rand[i]
    if guess not in rand:
        guessCount += 1
    hangman(guessCount)
    print(" ".join(word))
    if guessCount == 6:
        return print(f"You lose! The right answear was: {rand}")
    if "_" not in word:
        return print("BRAVO! You are winner!")
    prompt(letter, word)
    displays(rand, word, letter, guessCount)

def hangman(num):
    if num == 0:
        print("""
          ____
         |    |
         | 
         |
         |
         |   
        _|_""")
    elif num == 1:
        print("""
          ____
         |    |
         |    o
         | 
         | 
         |   
        _|_""")
    elif num == 2:
        print("""
          ____
         |    |
         |    o
         |    |
         | 
         |   
        _|_""")
    elif num == 3:
        print("""
          ____
         |    |
         |    o
         |   /|
         | 
         |   
        _|_""")
    elif num == 4:
        print("""
          ____
         |    |
         |    o
         |   /|\\
         | 
         |   
        _|_""")
    elif num == 5:
        print("""
          ____
         |    |
         |    o
         |   /|\\
         |   /
         |   
        _|_""")
    else:
        print("""
          ____
         |    |
         |    o
         |   /|\\
         |   / \\
         |   
        _|_""")