
import random
import os

puzzle_categories = os.listdir("puzzles")
art = os.listdir("art")

alpabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowel = ["a","e","i","o","u"]

def splash_screen():
    pic = open("art/splash_screen.txt")
    contents = pic.read()
    print(contents)
    pic.close()
    print()
    
def credits_screen():
    pic = open("art/credits_screen.txt")
    contents = pic.read()
    print(contents)
    pic.close()
    print()

    print("This game was created by Erik.")
    print("November 14th 2054")

def cooked_turkey():
    pic = open("art/cooked_turkey.txt")
    contents = pic.read()
    print(contents)
    pic.close()
    print()

def happy_turkey():
    pic = open("art/happy_turkey.txt")
    contents = pic.read()
    print(contents)
    pic.close()
    print()

def menu():
    for i,f in enumerate(puzzle_categories):
        print(str(i + 1) + ") " + f[:-4])

    print()
    
    choice = input("Which category do you want? ")
    choice = int(choice)

    file = "puzzles/" + puzzle_categories[choice - 1]

    with open(file,'r') as f:
        lines = f.read().splitlines()

    category = lines[0]
    print(category)
    print()
    
    return lines

    
    
def amount_of_players():
    while True:
        answer = input("How many people are playing, 1 or 2?: ")
        if answer == "1" or answer == "2":
            print()
            return answer
        else:
            print("Please enter '1' or '2'")

def get_puzzle():
    word = random.choice(menu())
    word = word.lower()
    
    if amount_of_players() == "1":
        return word
    else:
        return type_word()

def type_word():
    print("Player one will enter the word....")
    print("Player two will look away and try to guess the word.")
    word = input("Player one, what is your word?: ")
    for i in range(90):
        print()
    return word

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_hint(puzzle):
    count = 0
    for i in range(len(puzzle)):
        if puzzle[i].lower() in vowel:
            count += 1

    print("Hint: The word has " + str(count) + " vowel(s) in it.")

def cook_turkey(limit,tries):
    gap = limit - tries
    pic = open("art/" + str(gap) + ".txt")
    contents = pic.read()
    print(contents)
    pic.close()
    print() 

def get_guess(guesses,puzzle):
    while True:
        print()
        print("Type \"/hint\" for a hint.")
        guess = input("Guess a letter: ")
        if guess == "/hint":
            get_hint(puzzle)
        elif len(guess) > 1 or guess.lower() not in alpabet:
            print("Please enter only one alphabetical letter.")
        elif guess in guesses:
            print("You have already guessed that letter.")
        else:
            return guess

def display_board(solved,guesses,tries,limit):
    print("|----------------------------------------------------------------------|")
    print('|' + solved + "     Guessed:" + guesses + "     Tries:" + str(tries) + "/" + str(limit))
    print('|----------------------------------------------------------------------|')

def show_result(tries,limit,puzzle):
    if tries == limit:
        print()
        cooked_turkey()
        print()
        print("You Lose!")
        print("The word was \"" + puzzle + "\".")
        print()
    else:
        print()
        happy_turkey()
        print()
        print("You Win!")
        print()

def play():
    puzzle = get_puzzle()
    guesses = " ?,!,-"
    solved = get_solved(puzzle,guesses)

    tries = 0
    limit = 5

    display_board(solved,guesses,tries,limit)

    while solved != puzzle and tries < limit:
        letter = get_guess(guesses,puzzle)

        if letter not in puzzle:
            tries += 1
            print("Wrong!")
        print()

        guesses += ("," + letter)
        solved = get_solved(puzzle,guesses)
        display_board(solved,guesses,tries,limit)
        cook_turkey(limit,tries)

    show_result(tries,limit,puzzle)

def play_again():
    while True:
        print("Would you like to play again?(y/n): ")
        choice = input()
        if choice.lower() == "no" or choice.lower() == "n":
            print()
            return False
        elif choice.lower() == "yes" or choice.lower() == "y":
            print()
            return True
        else:
            print("Please enter 'y' or 'n'.")


splash_screen()

playing = True
while playing:
    play()
    playing = play_again()

credits_screen()

