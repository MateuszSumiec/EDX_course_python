"""
Gra w wisielca
"""
import random
import string


WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far

    returns: boolean, True if all the letters of secretWord are
    in lettersGuessed; False otherwise
    '''
    return set(secretWord).issubset(set(lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    new = secretWord[:]
    for l in secretWord:
        if l not in lettersGuessed:
            new = new.replace(l, '_ ')
    return new


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = list(string.ascii_lowercase[:])
    for l in lettersGuessed:
        if l in alpha:
            del alpha[alpha.index(l)]
    return ''.join(alpha)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    numberOfGuesses = 8
    lettersGuessed = []
    newLetter = ''
    while numberOfGuesses > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print('------------')
            print('Congratulations, you won!')
            break

        print('------------')
        print('You have', numberOfGuesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        newLetter = input('Please guess a letter: ').lower()
        if newLetter in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ',
                  getGuessedWord(secretWord, lettersGuessed))

        elif newLetter in secretWord:
            lettersGuessed.append(newLetter)
            print('Good guess:',
                  getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed.append(newLetter)
            print('Oops! That letter is not in my word:',
                  getGuessedWord(secretWord, lettersGuessed))
            numberOfGuesses -= 1

    if numberOfGuesses == 0:
        print('------------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord)


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
