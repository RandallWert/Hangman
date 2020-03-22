# HANGMAN GAME with Graphical User Interface

from tkinter import *
from tkinter import ttk
from tkinter import font
import random

# Functions

# Get random word from .txt file
# This function adapted from Andrew Yang, found at https://medium.com/@andrewyang96/coding-a-game-of-hangman-in-python-from-scratch-a538542e5c0c
def get_random_word():
    # Get a random word from the wordlist using no extra memory.
    # Some initialization
    global solution
    global incorrect_guesses_remaining
    word_displayed.set('')
    letters_already_guessed.clear()
    incorrect_guesses_remaining = 6

    # Get the next random word (solution to game)
    WORDLIST = 'wordlist.txt'
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().upper()
            if len(word) < 4 or len(word) > 16:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    solution = curr_word

    # Set up initial display of word
    for char in curr_word:
          if char in letters_already_guessed:
              word_displayed.set(word_displayed.get() + char)
          else:
              word_displayed.set(word_displayed.get() + '_')

# Use the letter clicked as the user's next guess
def letter_entry(letter_clicked):
    global incorrect_guesses_remaining
    if letter_clicked in letters_already_guessed:
        msg_to_user.set('You already clicked that letter.')
    else:
        msg_to_user.set('')
        letters_already_guessed.add(letter_clicked)
        if letter_clicked not in solution:
            incorrect_guesses_remaining -= 1
            if incorrect_guesses_remaining < 1:
                msg_to_user.set('You lost :(  The word was ' + solution)
            else:
                msg_to_user.set('Incorrect guesses remaining: ' + str(incorrect_guesses_remaining))
        else:
            game_won = True
            for char in solution:
                if char not in letters_already_guessed:
                    game_won = False
            if game_won:
                word_displayed.set(solution)
                msg_to_user.set('You won! :)  The word was ' + solution)
            else:
                word_displayed.set('')
                for char in solution:
                    if char in letters_already_guessed:
                        word_displayed.set(word_displayed.get() + char)
                    else:
                        word_displayed.set(word_displayed.get() + '_')
 
# Quit the program
def quit_program():
    root.destroy()

# tkinter stuff to set up display
root = Tk()
root.title('Hangman Game')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

appHighlightFont = font.Font(family='Helvetica', size=36, weight='bold')
word_displayed = StringVar()
word_display = ttk.Label(mainframe, textvariable = word_displayed, font=appHighlightFont).grid(column=1, row=1, sticky=W)

ttk.Button(mainframe, text='Get new word', command = get_random_word).grid(column=9, row=1, sticky=E)

msg_to_user = StringVar()
msg_display = ttk.Label(mainframe, textvariable = msg_to_user).grid(column=1, row=8, sticky=W)

# Letter buttons. Lambda must be used, because if you simply pass the letter directly as an
# argument, the button's command is invoked immediately(!)
ttk.Button(mainframe, text='A', command = lambda arg1='A' : letter_entry(arg1)).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text='B', command = lambda arg1='B' : letter_entry(arg1)).grid(column=3, row=3, sticky=(W, E))
ttk.Button(mainframe, text='C', command = lambda arg1='C' : letter_entry(arg1)).grid(column=4, row=3, sticky=(W, E))
ttk.Button(mainframe, text='D', command = lambda arg1='D' : letter_entry(arg1)).grid(column=5, row=3, sticky=(W, E))
ttk.Button(mainframe, text='E', command = lambda arg1='E' : letter_entry(arg1)).grid(column=6, row=3, sticky=(W, E))
ttk.Button(mainframe, text='F', command = lambda arg1='F' : letter_entry(arg1)).grid(column=7, row=3, sticky=(W, E))
ttk.Button(mainframe, text='G', command = lambda arg1='G' : letter_entry(arg1)).grid(column=8, row=3, sticky=(W, E))
ttk.Button(mainframe, text='H', command = lambda arg1='H' : letter_entry(arg1)).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text='I', command = lambda arg1='I' : letter_entry(arg1)).grid(column=3, row=4, sticky=(W, E))
ttk.Button(mainframe, text='J', command = lambda arg1='J' : letter_entry(arg1)).grid(column=4, row=4, sticky=(W, E))
ttk.Button(mainframe, text='K', command = lambda arg1='K' : letter_entry(arg1)).grid(column=5, row=4, sticky=(W, E))
ttk.Button(mainframe, text='L', command = lambda arg1='L' : letter_entry(arg1)).grid(column=6, row=4, sticky=(W, E))
ttk.Button(mainframe, text='M', command = lambda arg1='M' : letter_entry(arg1)).grid(column=7, row=4, sticky=(W, E))
ttk.Button(mainframe, text='N', command = lambda arg1='N' : letter_entry(arg1)).grid(column=8, row=4, sticky=(W, E))
ttk.Button(mainframe, text='O', command = lambda arg1='O' : letter_entry(arg1)).grid(column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text='P', command = lambda arg1='P' : letter_entry(arg1)).grid(column=3, row=5, sticky=(W, E))
ttk.Button(mainframe, text='Q', command = lambda arg1='Q' : letter_entry(arg1)).grid(column=4, row=5, sticky=(W, E))
ttk.Button(mainframe, text='R', command = lambda arg1='R' : letter_entry(arg1)).grid(column=5, row=5, sticky=(W, E))
ttk.Button(mainframe, text='S', command = lambda arg1='S' : letter_entry(arg1)).grid(column=6, row=5, sticky=(W, E))
ttk.Button(mainframe, text='T', command = lambda arg1='T' : letter_entry(arg1)).grid(column=7, row=5, sticky=(W, E))
ttk.Button(mainframe, text='U', command = lambda arg1='U' : letter_entry(arg1)).grid(column=8, row=5, sticky=(W, E))
ttk.Button(mainframe, text='V', command = lambda arg1='V' : letter_entry(arg1)).grid(column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text='W', command = lambda arg1='W' : letter_entry(arg1)).grid(column=3, row=6, sticky=(W, E))
ttk.Button(mainframe, text='X', command = lambda arg1='X' : letter_entry(arg1)).grid(column=4, row=6, sticky=(W, E))
ttk.Button(mainframe, text='Y', command = lambda arg1='Y' : letter_entry(arg1)).grid(column=5, row=6, sticky=(W, E))
ttk.Button(mainframe, text='Z', command = lambda arg1='Z' : letter_entry(arg1)).grid(column=6, row=6, sticky=(W, E))

ttk.Button(mainframe, text='Quit', command = quit_program).grid(column=9, row=12, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

solution = ''
letters_already_guessed = set()
incorrect_guesses_remaining = 6
root.mainloop()
