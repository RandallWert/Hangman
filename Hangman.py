# HANGMAN GAME

import random

# Get random word from .txt file
# This function adapted from Andrew Yang, found at https://medium.com/@andrewyang96/coding-a-game-of-hangman-in-python-from-scratch-a538542e5c0c
def get_random_word(min_word_length):
    """Get a random word from the wordlist using no extra memory."""
    WORDLIST = 'wordlist.txt'
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().upper()
            if len(word) < min_word_length or len(word) > 16:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word

# Outermost loop executes every time the player wants to play a(nother) game
play_another_game = True
while play_another_game:

    # Prompt user for choice of difficulty level and validate their input.
    # Difficulty level determines how many incorrect guesses are allowed (5-7).
    incorrect_guesses_remaining = 0
    awaiting_difficulty_level = True
    while awaiting_difficulty_level:
        difficulty_level = input('Please select difficulty level: 1 = easy, 2 - medium, 3 - hard  ')
        if difficulty_level == '1':
            incorrect_guesses_remaining = 7
            awaiting_difficulty_level = False
        elif difficulty_level == '2':
            incorrect_guesses_remaining = 6
            awaiting_difficulty_level = False
        elif difficulty_level == '3':
            incorrect_guesses_remaining = 5
            awaiting_difficulty_level = False
        else:
            print('Invalid input; try again!')

    # Select a word at random from the .txt file (between 4 and 16 letters)
    solution = get_random_word(4)

    # Initialize set of letters that have already been guessed
    letters_already_guessed = set()

    # This loop executes when it is time to prompt the user for another letter
    prompt_for_next_letter = True
    while prompt_for_next_letter:

        # Display word with unguessed letters obscured and number of incorrect
        # gueses remaining
        word_displayed = ''
        for char in solution:
            if char in letters_already_guessed:
                word_displayed = word_displayed + char
            else:
                word_displayed = word_displayed + '_'
        print(f'Solution: {word_displayed}')

        # Prompt user for next letter, coerce it upper case, and validate their input
        awaiting_next_letter = True
        while awaiting_next_letter:
            next_letter = input('Guess a letter!  ').upper()
            if len(next_letter) > 1:
                print('Please enter just one letter!')
            elif next_letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('That\'s not a letter!')
            elif next_letter in letters_already_guessed:
                print('You already guessed that letter!')
            else:
                # Keep track of letters that have already been guessed
                letters_already_guessed.add(next_letter)
                # Determine whether the guess is unsuccessful
                if next_letter not in solution:
                    incorrect_guesses_remaining -= 1
                awaiting_next_letter = False
        # Detect whether game has been won, lost, or should continue
        game_won = True
        for char in solution:
            if char not in letters_already_guessed:
                game_won = False
        if game_won:
            print(f'You won! :)  The word was {solution}')
            prompt_for_next_letter = False
        elif incorrect_guesses_remaining < 1:
            print(f'You lost :(  The word was {solution}')
            prompt_for_next_letter = False

        # If game has been won or lost, ask user whether to play another game
        if game_won or incorrect_guesses_remaining < 1:
            awaiting_play_another = True
            while awaiting_play_another:
                play_another = input('Play another game? Y/N  ')
                if play_another == 'n' or play_another == 'N':
                    awaiting_play_another = False
                    play_another_game = False
                elif play_another == 'y' or play_another == 'Y':
                    awaiting_play_another = False
