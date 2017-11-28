#hangman game
#Erik B
import random

alpabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowel = ["a","e","i","o","u"]
word_options = ["mountain","school","programming","road","tree!","computers","python","lemonade","backpack","example word","what?","blueberry bush","bologna"]

def splash_screen():
    print("""
 _   _    __    _  _  ___  __  __    __    _  _
( )_( )  /__\  ( \( )/ __)(  \/  )  /__\  ( \( )
 ) _ (  /(__)\  )  (( (_-. )    (  /(__)\  )  (
(_) (_)(__)(__)(_)\_)\___/(_/\/\_)(__)(__)(_)\_)
     """)

def credits_screen():
    print("""
______            _
| ___ \          | |
| |_/ /_   _  ___| |
| ___ \ | | |/ _ \ |
| |_/ / |_| |  __/_|
\____/ \__, |\___(_)
        __/ |
       |___/
       """)

    print("This game was created by Erik.")
    print("November 14th 2054")

def cooked_turkey():
    print("""
            )
          (
          ___
       .-'_ =\\
     c=<___\-_)
    ~~~~~~~~~~~~
    """)

def happy_turkey():
    print("""

                                       ____
                                      :    :
                  ___                 :____:
          ___ ---\ ~~ /---___         :  []:
          \   \ ~ \~ /~~~/~~~/     ----,-------
        ,' \~~ \~~ \/ ~~/~~~/ `,     ,'  0 0 __
       -_~~ \   \,------,  / ~ _`    ;    _____\\
      ;   - _ \,'^^^^^^^ ""`,_-  \   `, `--'; u
      ; ~~   ,'^^^^-----------   /   ,'`,,,'
      ;~ ---, ^^^,`__----,  ..`,/  ,'..,'
      `,  ~ ,^^ <_'__--__ `, .. `,/ .. `
       `,---` ^<________--  `, .. ..  ,'     ___ [] ___
        `,---` <__ -__ ___  ,' .. . ,`     _/   \)(/   \_
         `, --` <__ __ _  ,' ... _,`      /   /      \   \\
          `--,___<___   ,'`-___,'       ,'   :   |        `,
                  <___,'(||)            :             :    :
                    ||   ||             :    :   |         ;
                  __||_ _||_            \_            :   _/
                 // ;;\\ ;;\\             \_  \  |   /  _/
                ~~     ~~   ~~              \__________/
                """)

def amount_of_players():
    while True:
        answer = input("How many people are playing, 1 or 2?: ")
        if answer == "1" or answer == "2":
            print()
            return answer
        else:
            print("Please enter '1' or '2'")

def get_dificulty():
    print("What do you want the difficulty to be?")
    print("Hard (4 tries).")
    print("Regular (6 tries).")
    while True:
        answer = input("Enter 'hard' or 'regular': ")
        if answer == 'hard':
            print()
            return 4
        elif answer == 'regular':
            print()
            return 6
        else:
            print("Please enter 'hard' or 'regular'.")
            print()


def get_puzzle():
    if amount_of_players() == "1":
        return random.choice(word_options)
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
    gap = "         " * (limit - tries)
    print()
    print("""  _   \|_|/ """ + gap + """  ) """ )
    print("""   (_` )_('>""" + gap + """ )\\""" )
    print("""   (__,~_)8 """ + gap + """/ ) (""")
    print("""      _YY_  """ + gap + """\(_)/""")
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
    guesses = " ?,!"
    solved = get_solved(puzzle,guesses)

    tries = 0
    limit = get_dificulty()

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
