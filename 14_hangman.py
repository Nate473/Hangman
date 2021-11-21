import words
import random

run = True


def get_word():
    # generate a word
    correct_word = words.words[random.randint(0, len(words.words))]
    return correct_word


def print_hangman(n, m, blnk):
    print(words.hangman[n - 1])  # display hangman's current state
    print(' Guessed Letters: ', m)
    print(' Word: {0}'.format(blnk))
    # n is number of tries, m is guessed letters


while run:
    # main loop
    guessed = False  # True if word has been guessed
    guessed_letters = ''  # letters wrongly guessed
    tries = len(words.hangman)
    word = get_word()
    blank = "_ " * len(word)

    while not guessed:
        # game loop
        for i in range(3):
            print()
        print(word)
        print_hangman(tries, guessed_letters, blank)
        guess = input(' Enter a guess: ').lower()

        if len(guess) != 1 or not (guess in words.alphabet):  # checking if guess is a single letter in the alphabet
            print('Please enter a single character')
            continue
        if guess in guessed_letters:
            print(guess, ' has already been guessed')
            continue  # go back to re-guess
        if guess in word:
            # append guess to already guessed letters
            guessed_letters += guess
            guessed_letters += ' '
            # replace blanks with correctly guessed letters
            for i in range(len(word)):  # looping through the correct word for comparisons
                if guess == word[i]:
                    blank = blank.split(' ')  # make blank a list for easy replacement
                    blank[i] = word[i]  # replace a blank with it's rightful letter
                    blank = ' '.\
                        join(blank)  # make blank a string again

                # splitting and joining blank for comparisons sake without affecting blank itself
                tmp_blank = blank.split(' ')
                tmp_blank = ''.join(tmp_blank)

                if tmp_blank == word:  # word has been guessed correctly
                    print(blank)
                    print('wow nigga')
                    guessed = True
            continue  # go back to top of loop to guess another letter

        if guess not in word and tries > 0:  # checking if user has run out of tries
            if tries == 1:
                # still needs refractoring
                print('You\'re out of tries')  # irrelevant
                print('quitting now')  # irrelevant as well
                tries -= 1  # to ensure tries are 0
                guessed_letters += guess
                guessed_letters += ' '
                print('Word was, ', word)
                break  # break out of game loop
            tries -= 1  # only executes if tries are > 1
            guessed_letters += guess
            guessed_letters += ' '
            continue

    # TRY AGAIN
    if guessed:
        continue
    # if guessed, it won't reach this far

    q = input('Try again [y/n]')
    if q == 'y':
        print('CONTINUING.... ')
        continue
    else:
        print('QUITTING...')
        break

# TODO handle game over... DONE
# TODO handle retry... DONE
# TODO handle if correct word is guessed... DONE
# TODO add a functionality for pts
# TODO add dictionary words
# TODO Add complexity to random words, i.e never chose the same word twice
# TODO fix number issues
