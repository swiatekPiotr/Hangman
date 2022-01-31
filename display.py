
def prompt(letters, word):
    letters = [i for i in letters if i not in word]
    print("".join(letters))


def displays(rand, word, letter):
    guess = (input(">")).upper()
    for i in range(len(rand)):
        if rand[i] == guess:
            word[i] = rand[i]
    print(" ".join(word))
    if "_" not in word:
        return print("BRAVO! You are winner!")
    prompt(letter, word)
    displays(rand, word, letter)