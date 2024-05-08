# Amanda Kirby
# Assignment: Final
# Date: May 7, 2024

import os
import sys
import time


##PLAYER SETUP###################################################################
class Player:
    def __init__(self):
        self.game_over = None
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'


myPlayer = Player()


##TITLE SCREEN##################################################################
def title_screen_selections():
    option = input(">")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input(">")
        if option.lower() == "play":
            start_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    os.system("cls")
    print('############################')
    print('#     Welcome to My Game   #')
    print('############################')
    print('          -- Play --        ')
    print('          -- Help --        ')
    print('          -- Quit __        ')
    print('    Copyright 2024 akirby.me')
    title_screen_selections()


def help_menu():
    print('############################')
    print('#     Welcome to My Game   #')
    print('############################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good Luck and Have Fun')
    title_screen_selections()


# Map#######################################################################################
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = "examine"
TOUR = False
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

toured_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zone = {
    'a1': {
        ZONENAME: 'Windsor',
        DESCRIPTION: 'Welcome to Windsor',
        EXAMINATION: 'Quite the history of Royalty',
        TOUR: False,
        UP: 'up',
        DOWN: 'b1',
        LEFT: 'left',
        RIGHT: 'a2',
    },

    'a2': {
        ZONENAME: 'Goodbye Yellow Brick Road',
        DESCRIPTION: 'Where the dogs of society howl',
        EXAMINATION: 'Howling Old Owl in The Woods',
        TOUR: False,
        UP: 'up',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'b3',
    },
    'a3': {
        ZONENAME: 'Charity Event',
        DESCRIPTION: 'Lavish Charity Event',
        EXAMINATION: 'Raise Money for the Charity Event',
        TOUR: False,
        UP: 'up',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: 'The Hub',
        DESCRIPTION: 'Tastefully Over the Top!',
        EXAMINATION: 'Sits on the Edge of Windsor Great Park.',
        TOUR: False,
        UP: 'up',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'right',

    },
    'b1': {
        ZONENAME: 'Beverly Hills',
        DESCRIPTION: 'Rodeo Drive',
        EXAMINATION: 'Upscale Shopping',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!',
        EXAMINATION: '1960s- Era',
        TOUR: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },

    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'DESCRIPTION',
        EXAMINATION: 'examine',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },

    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'DESCRIPTION',
        EXAMINATION: 'examine',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },

    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'DESCRIPTION',
        EXAMINATION: 'examine',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },

    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'DESCRIPTION',
        EXAMINATION: 'examine',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },

    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'DESCRIPTION',
        EXAMINATION: 'examine',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },

    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'DESCRIPTION',
        EXAMINATION: 'examine',
        TOUR: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    }
}


# GAME FUNCTIONALITY##########################################################################


###### Game Interactivity ########

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zone[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def player_action(param):
    pass


def prompt():
    print('\n' + "=========================")
    print(input("What would you like to do?"))
    action = input(">")
    acceptable_actions = ['sign autographs', 'concert', 'music studio', 'trivia questions']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input(">")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['up', 'down', 'left', 'right']:
        player_move(action.lower())
    elif action.lower() in ['sign autographs', 'concert', 'music studio']:
        player_action(action.lower())


def player_move(my_action):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up']:
        destination = zone[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down']:
        destination = zone[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left']:
        destination = zone[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right']:
        destination = zone[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zone[myPlayer.location][TOUR]:
        print("You have already Toured this Zone!")
    else:
        print("TriviaTime!")


##### Game Functionality ##########
def start_game():
    return


def main_game_loop():
    while not myPlayer.game_over:
        prompt()


def setup_game():
    os.system('clear')


question1 = "Hello, what's your name?\n"
for character in question1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
    player_name = input(">")
    myPlayer.name = player_name

### Job Handling
question2 = "Hello, what character would you like to play?\n"
question2added = "(You can play as Music Man, Tiny Dancer, Rocket Man, Bennie)"
for character in question2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
player_job = input(">")
valid_jobs = ["Music Man", "Tiny Dancer", "Rocket Man", "Bennie"]
if player_job.lower() in valid_jobs:
    myPlayer.job = player_job
    print("You are now " + player_job + "!\n")
while player_job.lower() not in valid_jobs:
    player_job = input(">")
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now " + player_job + "!\n")

        if myPlayer.job == 'Music Man':
            myPlayer.hp = 100
            myPlayer.mp = 20
        elif myPlayer.job == 'Tiny Dancer':
            myPlayer.hp = 40
            myPlayer.mp = 120
        elif myPlayer.job == 'Rocket Man':
            myPlayer.hp = 60
            myPlayer.mp = 60
        elif myPlayer.job == 'Bennie':
            myPlayer.hp = 80
            myPlayer.mp = 20

#### Introduction
question3 = "Welcome, "
for character in question3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
    play_name = input(">")
myPlayer.name = player_name

speech1 = "Jesus freaks, out in the street handing tickets out for God"
speech2 = ""
speech3 = ""
speech4 = ""
for character in speech1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
for character in speech2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
for character in speech3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
for character in speech4:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)

    os.system('cls')
    print('###########################')
    print("#      Let's Start Now!   #")
    print("###########################")
    main_game_loop()

title_screen()
