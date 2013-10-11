# This is a text based Hangman Program
# Out set of Secret words will be the diffrent types of colors
# for example, black, blue, yellow, orange, etc.

from random import choice
already_guessed_list = []
spaces = []

def update_word(secret, guessed):
    """
    Takes the secret and guessed word and updates the spaces list
    >>> update_word(red, d)
    _ _ d
    >>> update_word(orange, n)
    _ _ _ n _ _
    >>> update_word(yellow, l)
    _ _ l l _ _
    """
    # take each letter from secret word and if it is same as guessed
    # then find the index of guessed word in secret word and assign that
    # guessed word to the spaces list at that index.

    # this list stores the index of letter which are in secret word
    index_occurrence = []
    index = 0
    occurrence = 0

    #counts the number of occurence of letter in secret word
    occurrence = secret.count(guessed)
    last_occurrence = 0
    
    # to store the index of letters in index_occurence list
    for num in range(occurrence):
        index_occurrence.append(secret.index(guessed, last_occurrence))
        # if more than one occurence, then use last occurence in range
        # function to find the index of next occurence of same letter
        last_occurrence = secret.index(guessed, last_occurrence) + 1

    # if occurence is only one, then simple
    # assignment to the spaces index
    if occurrence == 1:
        for letter in secret:
            index = secret.index(letter)
            if letter == guessed:
                    spaces[index] = letter + ' '
    # if occurence is more than one, then use index_occurence to get the
    # index of same letter at different positions and assign guessed word
    # to that index in spaces list
    elif occurrence > 1:
        for num in range(occurrence):
            spaces[index_occurrence[num]] = guessed + ' '
        
            
    
        
def print_sequence(sequence):
    """
    list(str) -> str
    
    takes the sequence of strings and prints out as a complete single string

    >>>print_spaces(['a', 'b', 'c'])
    abc
    """
    name = ''
    for num in sequence:
        name += num
    return print(name)


def print_secret(secret, guessed):
    
    if guessed in already_guessed_list:
        print ("\nYou have already used this letter before!")
        return
    
    elif (not(guessed in already_guessed_list)) and (guessed in secret):
        print ("- - - - - - - - - - - - - - \n- - - - - - - - - - - - - - \nCorrect letter! \n")

        # appends the guessed word in already_guessed_list
        # and display all guessed word from list in string
        already_guessed_list.append(guessed)
        print("Already guessed: ", end = '')
        print_sequence(already_guessed_list)

        # update the spaces if guessed word is in secret
        update_word(secret, guessed)
        print ("Secret Color: ", end = ' ')
        print_sequence(spaces)

    else:
        print("\nInvalid Input \n")
        
        
##################################
# PROGRAM STARTS HERE #
#################################

colorList = ['aquamarine', 'cyan', 'purpule', 'magenta',
             'olive', 'turquoise', 'gold','grey', 'black',
             'blue', 'yellow', 'orange', 'pink', 'white',
             'red', 'brown', 'violet', 'green', 'indigo',
             'silver', 'teal', 'lime', 'maroon']

# choose a random element from
# colorList and assign as secret word
secret = choice(colorList)

print("Welcome to the world of Hangman!")
print("Guess the color\n")

# For one time only, to show the blank spaces
print(len(secret)*'_ ')

# update the spaces list to the number of letters in secret word
for letter in range(len(secret)):
    spaces.append('_ ')

# nnumber of guesses a player get, CHANGE THIS TO INCREASE LIFE
guess_left = 6


while guess_left > 0:
    # if there is no word left to guess, then the program is complete
    if not ('_ ' in spaces):
        print("\n\nCongratulations, You did it!")
        break
    guessed = input('\nEnter a letter: ')

    # if the guessed word is not in secret word, then decrease
    # guess_left and if guess_left becomes 0, stop program
    if (not(guessed in secret)):
        guess_left -= 1
        # add the already guessed word in a
        # list so that user cannot type it again

        # appends the guessed word in already_guessed_list
        # and display all guessed word from list in string
        already_guessed_list.append(guessed)
        print("\nAlready guessed: ", end = '')
        print_sequence(already_guessed_list)


        print('Wrong choice!')
        print("Guesses Left: " + str(guess_left))
        if guess_left == 0:
            print("Game Over, Correct answer was:", secret)
        continue
    
    print_secret(secret, guessed)
    

