  

import cmd
import textwrap
import sys
import time
import os
import random

screen_width = 100

##class player:
##    def__init__(self):
##        self.name = ''
##        self.hp = 5
##        self.status_effects = []
##        self.location = "start_point"
##theplayer = player()

player_position = "room 1"
player_name = " "

def menu_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() #doesn't exist yet
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        print("Thanks for playing!")
        sys.exit()
        quit()
    else:
        print("Please enter a valid command")
        menu_selections()
def main_menu():
    print("#########################################")
    print("# Welcome to Alex's Text Dungeon Puzzle #")
    print("#########################################")
    print("                 -Play-                  ")
    print("                 -Help-                  ")
    print("                 -Quit-                  ")
    print("         Copyright 2019 a.xia7.com       ")
    menu_selections()

def help_menu():
    print("####################################")
    print("#             Help Menu            #")
    print("####################################")
    print("   -Type the commands to do them-   ")
    print(" -Work your way through the dungeon- ")
    print("      -Good luck and have fun!-      ")
    menu_selections()

#######
##Map##
#######    
    
DESCRIPTION = 'description'
INFO = 'info'
PUZZLE = 'puzzle'
SOLVED = False
FORWARD = "forward"
BACKWARD = "backward"

room_solved = {"room 1": False, "room 2": False, "room 3": False, "room 4": False, "Boss Room": False}

dungeon = {
            "room 1": {
                    DESCRIPTION: "You find yourself in a cold, and dark room. The room is completely bare \nexcept a door and a sign next to it.",
                    INFO: "You walk towards the door and read the rough words etched out on the sign.",
                    PUZZLE: "Welcome" + player_name+ ", you are inside a dungeon with four 5 rooms. Each room has \nits own puzzle. In order to exit this dungeon, you must clear all four rooms. \nType 'go forward' to move on to the next room. Good Luck.",
                    SOLVED: "go forward",
                    },
            "room 2": {
                    DESCRIPTION: "You find yourself in a dimly lit room decorated with a traditional Chinese theme.",
                    INFO: "You walk towards a small monitor on the wall and read the words on the screen.",
                    PUZZLE: "What year did the Chinese Cultural Revolution first start?",
                    SOLVED: "1966",
                    },
            "room 3": {
                    DESCRIPTION: "You find yourself in a bright room filled with European decorations",
                    INFO: "You walk towards a small monitor on the wall and read the words on the screen.",
                    PUZZLE: "Who introduced the German Rentenmark in 1923?",
                    SOLVED: "gustav stresemann",
                    },
            "room 4": {
                    DESCRIPTION: "You find yourself in a cold room with snow covering the ground,\na campfire glows brightly in the centre.",
                    INFO: "As you walk closer the campfire, molten red words display themselves before you:",
                    PUZZLE: "What bites without teeth?",
                    SOLVED: "frost",
                    },
            "Boss Room": {
                    DESCRIPTION: "You find yourself in a spacious room with large stone bird perched in the middle. ",
                    INFO: "As you walk closer to the bird, it begins to speak to you",
                    PUZZLE: "'I fly without wings. I see without eyes. I move without legs.\nI conjure more love than any lover and more fear than any beast.\nI am cunning, ruthless, and tall; in the end, I rule all. \nWhat am I?'",
                    SOLVED: "imagination",
                    },      
            }
#################
##Game handling##
#################

def print_location():
    global player_position
    print("\n" + ('#' * (2 + len(player_position))))
    print('#' + player_position.upper() + '#')
    print('#' * (2 + len(player_position)))
    print('\n' + (dungeon[player_position][DESCRIPTION]))
    prompt()

def prompt():
    global player_position
    if player_position == "room 1":
        print("\nWhat would you like to do? \n \nYour available options are: \nexamine \nquitgame \ngo forward")
        action = input("> ")
        acceptable_actions = ["examine", "quitgame", "go forward"]
        while action.lower() not in acceptable_actions:
            print("Unknown action command. Please try again.")
            action = input("> ")
        if action.lower() == "quitgame":
            print("Thanks for playing!")
            sys.exit()
        elif action.lower() == "examine":
            examine()
        elif action.lower() == "go forward":
            move_forward()
    if player_position == "room 2" or "room 3" or "room 4":
        print("\nWhat would you like to do? \n \nYour available options are: \ngo back  \ngo forward \nexamine \nquitgame")
        action = input("> ")
        acceptable_actions = ["go back", "examine", "quitgame", "go forward"]
        while action.lower() not in acceptable_actions:
            print("Unknown action command. Please try again.")
            action = input("> ")
        if action.lower() == "quitgame":
            print("Thanks for playing!")
            sys.exit()
        elif action.lower() == "go back":
            move_back()
        elif action.lower() == "examine":
            examine()
        elif action.lower() == "go forward":
            move_forward()
    if player_position == "Boss Room":
        print("\nWhat would you like to do? \n \nYour available options are: \ngo back \nexamine \nquitgame")
        action = input("> ")
        acceptable_actions = ["examine", "quitgame", "go back"]
        while action.lower() not in acceptable_actions:
            print("Unknown action command. Please try again.")
            action = input("> ")
        if action.lower() == "quitgame":
            print("Thanks for playing!")
            sys.exit()
        elif action.lower() == "examine":
            examine()
        elif action.lower() == "go back":
            move_back()

            
def examine():
    global player_position
    if room_solved[player_position] == False:
        print("\n" + (dungeon[player_position][INFO]))
        print("\n" + (dungeon[player_position][PUZZLE]))
        puzzle_answer = input("> ")
        if puzzle_answer.lower() == "quitgame":
            print("Thanks for playing!")
            sys.exit()
        elif puzzle_answer.lower() == "go back":
            move_back()
        else:
            check_answer(puzzle_answer)
    else:
        print("\n" + "There is nothing else for you to see here.")
        prompt()

def check_answer(puzzle_answer):
    global player_position
    if puzzle_answer.lower() == (dungeon[player_position][SOLVED]):
        if player_position == "Boss Room":
            print("\n" + "Congratulations " + player_name + "! You have cleared the dungeon!")
            main_menu()
        else:
            print("\n" + "Correct! You have cleared this room." + "\n" + "Please move on to the next room")
            global room_solved
            room_solved[player_position] = True
            prompt()
    else:
        print("\n" + "That is not the correct answer." + "\n" + "Please try again.")
        puzzle_answer = input("> ")
        if puzzle_answer.lower() == "quitgame":
            print("Thanks for playing!")
            sys.exit()
        elif puzzle_answer.lower() == "go back":
            move_back()
        else:
            check_answer(puzzle_answer)

def move_back():
    global player_position
    print("\n" + "You decide to take a rest in the previous room.")
    if player_position == "room 2":
        player_position = "room 1"
        print_location()
    if player_position == "room 3":
        player_position = "room 2"
        print_location()
    if player_position == "room 4":
        player_position = "room 3"
        print_location()
    if player_position == "Boss Room":
        player_position = "room 4"
        print_location()
        

def move_forward():
    global player_position
    if room_solved[player_position] == False:
        print("\n" + "You try to open the door that leads to the next room but find that it is locked. \nSolving the puzzle is the only way to unlock the door.")
        prompt()
    if room_solved[player_position] == True:
        print("\n" + "You open the door that leads to the next room.")
        if player_position == "room 1":
            player_position = "room 2"
            print_location()
        if player_position == "room 2":
            player_position = "room 3"
            print_location()
        if player_position == "room 3":
            player_position = "room 4"
            print_location()
        if player_position == "room 4":
            player_position = "Boss Room"
            print_location()

##############    
##Game Setup##
##############

def setup_game():
    os.system("clear")
    #Clears game terminal
    question1 = "Hello there, what is your name? \n"

    for char in question1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    global player_name    
    player_name = input("> ")

    speech1 = "Interesting... if it is you ... you may be able to solve it. \n"
    speech2 = "Oh, you don't know where you are? Well... that is for you to find out.\n"
    speech3 = "Now " + player_name + ", this is where we must part.\n"
    speech4 = "You must now embark on a journey, and it starts with escaping this dungeon. \n"
    speech5 = "Good luck. \n"
    
    for char in speech1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for char in speech2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for char in speech3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for char in speech4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)                    
    for char in speech5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(1)

    os.system("clear")
    print("#################################")
    print("# Your adventure begins here... #")
    print("#################################")

    time.sleep(2)

    os.system("clear")
    print_location()

os.system("clear")
main_menu()    
    

        
    
            


                   
