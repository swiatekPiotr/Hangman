import random



def randoml():
    path = "C:\\Users\\Piotrek\\PycharmProjects\\untitled\\Hangman\\sowpods_dict.txt"
    with open(path, 'r') as open_file:
        if open_file.readable():
            wordList = open_file.read().split("\n")
    randomly = random.choice(wordList)
    # print(randomly)
    return randomly
