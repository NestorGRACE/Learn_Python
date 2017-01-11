# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name is "rock":
        return 0
    if name is "Spock":
        return 1
    if name is "paper":
        return 2
    if name is "lizard":
        return 3
    if name is "scissors":
        return 4
    else :
        return "Error"
    


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number is 0:
        return "rock"
    if number is 1:
        return "Spock"
    if number is 2:
        return "paper"
    if number is 3:
        return "lizard"
    if number is 4:
        return "scissors"
    else:
        return "Error"

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print 
    # print out the message for the player's choice
    import random
    print "Player chooses "+ player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number =name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses "+ comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    if (difference ==1) or (difference ==2):
        print "Computer wins!"
    if (difference ==3) or (difference ==4):
        print "Player wins!"
    if (difference ==0) or (difference ==5):
        print "Player and computer tie!"
    # use if/elif/else to determine winner, print winner message


# always remember to check your completed program against the grading rubric
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
 
# Handler for input field
def get_guess(guess):
    global player_choice
    player_choice=guess
    if player_choice in ["rock","Spock","paper","lizard","scissors"]:
        rpsls(player_choice)
    else:
        print "Player chooses", player_choice,"is (s)he trying to cheat?"
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
