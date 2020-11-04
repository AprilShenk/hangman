import random
import string 

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    
    # better use of memory because the file wont stay open any longer than necessary
    # also condensed the readline and split methods to use less variables
    # did you know about f-strings? https://docs.python.org/3.7/reference/lexical_analysis.html#f-strings
    
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.readline().split()
        print(f'{len(wordlist)} words loaded.')
        return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

# turn the logic around for a shorter runtime if the word is not guessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    # if we complete the loop we know all letters in secret_word have been guessed.
    print(f'You guessed the word! {secret_word}')
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #    pass

    # use list comprehension to do the same without storing an additional variable,
    # "".join() sticks the letters together into a string without spaces
    return "".join([letter + " " if letter in letters_guessed else "_ " for letter in secret_word])


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    # use list comprehension to do the same without storing an additional variable,
    # "".join() sticks the letters together into a string without spaces
    return "".join([c for c in string.ascii_lowercase if c not in letters_guessed])


def check_guess(guess, secret_word):
    '''
    guess: a letter that the user guessed
    secret_word: the word the user is guessing
    returns: boolean, True if the letter is in the word, False if the letter is not
    '''

    return guess in secret_word


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    lives = 6
    letters_guessed = ''

    print('Welcome to the Game of Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    
    # once lives == 0 it will resolve to False, any positive integer resolves to True
    
    while not is_word_guessed(secret_word, letters_guessed) and lives:
        print(get_guessed_word(secret_word, letters_guessed))
        print(f'You have {lives} guesses left.')
        print(f'Available Letters: {get_available_letters(letters_guessed)}')
        guess = input('Guess a letter or word: ').lower()

        if guess == secret_word:  # check if the entire word was guessed
            break
        elif guess in letters_guessed:  # check for duplicates
            print(f'You have guessed this letter before: {guess}')
            lives -= 1
        elif guess not in string.ascii_lowercase:  # check for invalid input
            print(f'Oops, that is not a letter: {guess}')
        else:  # valid and not duplicates
            letters_guessed += guess
            if check_guess(guess, secret_word):
                print('Good guess!')
            else:
                print(f'Oops, the letter "{guess}" is not in the word!')
                lives -= 1
                
    # moved out of the loop, when it exits we already know one of these is true so only checking the int is more efficient
    # if lives == 0 it resolves to False, which means the word was guessed correctly.
    
    return print('Congrats! You guessed the word correctly and win!') if lives else print('Sorry, you ran out of tries.')


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    hangman(choose_word(wordlist))

