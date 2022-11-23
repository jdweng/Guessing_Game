#Josh Wenger
#Programming Assignment 1 (Guessing Game)
#September 16, 2022

#A number between 1 and 100 is chosen at random and the player has four guesses to guess the chosen number.
#Player's will be told whether their guess is too high or too low after each correct guess.

from random import randint
import webbrowser
from time import sleep

numbertry = 0


#Opening banter
#The sleep function just adds dramatic pauses between text.

print("Welcome to the number guessing game.")
sleep(1)
print("It's pretty fun I guess...")
sleep(1)
print("I don't know...")
sleep(1)
print("I'd probably rather do most anything else.")
sleep(1)
print("Anyway, what's your name?")

#Collect name for leaderboard.

name = str(input())
print("That was sarcastic. I don't really care")
sleep(1)

#Allows participant to not play the game by setting 'again' to 'n' or 'N', avoiding the game loop before it starts, or set it to 'y'/'Y' to fulfill the while loop condition.

while True:
    print("You wanna play or not? (Y/N)")
    again = input()
    
    if again == "N" or again == "n":
        print("Fine. I didn't want you to play anyway.")
        break

    elif again == "Y" or again == "y":
        break

    else:
        print("Invalid input")
        continue    


#The full game is in this while loop so that if the player ever changes 'again' to 'n' or 'N', the game stops.

while again == "Y" or again == "y":
    num = randint(1,100)
    #print(num)
    condition = "lose"

#First guess

#The guess blocks are all set within a 'while True' loop so they will be asked to input a valid number again if they do not the first time.
#Additionally, the try and except functions keep it from crashing if the input is not valid. 

    while True:
        
        guess1 = input("I've chosen a number between 1 and 100. You will have four guesses to guess the number.")
        try:
            guess1 = int(guess1)
        except:
            print("Invalid input")
            continue
        
        if guess1 == num:
            attempt = 1
            print("You got it in one. Big whoop. Make yourself a medal or something.")
            condition = "win"
            break

        elif guess1 < num:
            print("Too low, you have three more guesses.")
            break

        elif guess1 > num:
            print("Too high, you have three more guesses.")
            break

#Second guess

#Each of these guess sections after the first begins by checking that the player's condition == 'lose'.
#This makes it so these sections will be skipped as soon as the player guesses correctly. When they loop back to the beginning the condition is reassigned to 'lose'.

    if condition == "lose":
        while True:

            guess2 = input()
            try:
                guess2 = int(guess2)
            except:
                print("Invalid input")
                continue

            if guess2 == num:
                attempt = 2
                print("You got it in two. That's not as good as getting it in one.")
                condition = "win"
                break

            elif guess2 < num:
                print("Too low, you have two more guesses.")
                break

            elif guess2 > num:
                print("Too high, you have three more guesses.")
                break
        
#Third guess

    if condition == "lose":
        while True:

            guess3 = input()
            try:
                guess3 = int(guess3)
            except:
                print("Invalid input")
                continue

            if guess3 == num:
                attempt = 3
                print("You got it in three. That's a pretty lackluster performance " + name + '.')
                condition = "win"
                break

            elif guess3 < num:
                print("Too low, you have one more guess.")
                break

            elif guess3 > num:
                print("Too high, you have one more guess.")
                break

#Fourth guess

#This makes use of the numbertry variable which keeps track of the number of failed attempts throughout the game. The variable does not get reset until the game is rebooted.
#If they fail three times there is a snarky comment for them and it opens up a webpage.           

    if condition == "lose":
        while True:
            
            guess4 = input()
            try:
                guess4 = int(guess4)
            except:
                print("Invalid input")
                continue

            if guess4 == num:
                attempt = 4
                print("You got it in four. At least you have a LOT of room to improve.")
                condition = "win"
                break

            elif guess4 < num:
                print("Too low, the number was:", num)
                numbertry += 1
                if numbertry == 3:
                    sleep(1)
                    print("Maybe you need a new hobby.")
                    sleep(1)
                    webbrowser.open('https://en.wikipedia.org/wiki/List_of_hobbies')
                break
                
            elif guess4 > num:
                print("Too high, the number was:", num)
                numbertry += 1
                if numbertry == 3:
                    sleep(1)
                    print("Maybe you need a new hobby.")
                    sleep(1)
                    webbrowser.open('https://en.wikipedia.org/wiki/List_of_hobbies')
                break

#Leaderboard

#The player's number of tries and name are added to the text file if they win, then the file is converted to a list, sorted by score, and the three lowest scores are displayed.
#The try and except section at the bottom is to avoid an error if there are not enough scores to retrieve i.e. it's the player's first time and the scoreboard is empty.

    with open("leaderboard.txt", "a+") as l:
        if condition == "win":
            l.write(str(attempt) + "        " + str(name) + "\n")
        l.seek(0)
        read = l.read().splitlines()
        read.sort()
        print("Leaderboard:")
        print("Score \t Name")
        try:
            print(read[0])
        except:
            pass
        try: 
            print(read[1])
        except:
            pass
        try:
            print(read[2])
        except:
            pass
            
#Here is where the participant can play again or break out of the loop by changing the variable 'again'.

    while True:
        print("You wanna play again or not? (Y/N)")
        again = input()
    
        if again == "Y" or again == "y":
            break

        elif again == "N" or again == "n":
            print("Fine. Leave.")
            break

        else:
            print("Invalid input")
    
