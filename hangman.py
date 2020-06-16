# Importing Libraries
import random

# function
def hangman(winning_word,char_guessed):
    for i in winning_word:
        if i in char_guessed:
            print(f' {i} ' , end='')
        else:
            print(' __ ', end='')
    print()

def over(winning_word,char_guessed):
    counts = 0
    for i in set(winning_word):
        if i in char_guessed:
            counts += 1
    return counts == len(set(winning_word))


# Word
words = ['promote','intelligent','facebook','alphabate','objective','individual','successful','character','otherwise','mountain','beautiful','processor','instagram']
random.shuffle(words)
winning_word = random.choice(words)
char_guessed = ''


# Welcome User
user_name = input('Type your name : ').title()
print(f"Welcome {user_name}. \nLet's play Word guessing game\nGuess the character one by one.")

# main
print(f'The word has {len(winning_word)} characters.\n')
user_guess = input('Guess any character: ').lower()[0]


while True:
    
    if user_guess in char_guessed:
       user_guess = input('Already guessed.\nGuess again: ')

    elif (user_guess in winning_word) and (user_guess not in char_guessed):
        print(f'Correct guess. "{user_guess}" in the word.')
        char_guessed += user_guess
        hangman(winning_word,char_guessed)
        game_over = over(winning_word,char_guessed)
        if game_over:
            print(f'\nCongrats. You guessed the Word "{winning_word.upper()}".')
            break
        else:
            user_guess = input('Guess next character: ')

    elif user_guess not in winning_word:
        print(f'Wrong guess. "{user_guess}" not in the word.')
        user_guess = input('Guess again: ')
    
    