# Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of 
# Rock-paper-scissors that allows five choices. Each choice
# wins against two other choices, loses against two other 
#choices and ties against itself. Much of RPSLS's popularity
# is that it has been featured in 3 episodes of the TV series
# "The Big Bang Theory".

#rules: scissors beats paper and lizard
# paper beats rock and spock
# rock beats scissors and lizard
# lizard beats spock and paper
# spock beats scissors and rock

import random

def name_to_number(name):
	if name == "rock":
		return 0
	elif name == "Spock":
		return 1
	elif name == "paper":
		return 2
	elif name == "lizard":
		return 3
	elif name == "scissors":
		return 4


def number_to_name(number):
	if number == 0:
		return "rock"
	elif number == 1:
		return "Spock"
	elif number == 2:
		return "paper"
    elif number == 3:
		return "lizard"
	elif number == 4:
		return "scissors"

def rpsls(player_choice): 

	print "The player chooses: ", player_choice
	player = name_to_number(player_choice)
	computer = random.randrange(0, 5)

	print(' ') #print out a blank line

	print "The computer chooses: ", number_to_name(computer)

	if player == 0 and computer == 1
		print 
	elif player == 0 and computer == 2
		print 
	elif player == 0 and computer == 3
		print 
	elif player == 0 and computer == 4
		print 	

	elif player == 1 and computer == 0
		print 
	elif player == 1 and computer == 2
		print 
	elif player == 1 and computer == 3
		print 
	elif player == 1 and computer == 4
		print 

	elif player == 2 and computer == 0
		print 
	elif player == 2 and computer == 1
		print 
	elif player == 2 and computer == 3
		print 
	elif player == 2 and computer == 4
		print 

	elif player == 3 and computer == 0
		print 
	elif player == 3 and computer == 1
		print 
	elif player == 3 and computer == 2
		print 
	elif player == 3 and computer == 4
		print 

	elif player == 4 and computer == 0
		print 
	elif player == 4 and computer == 1
		print 
	elif player == 4 and computer == 2
		print 
	elif player == 4 and computer == 3
		print

	elif player == computer
		print "Tie game!" 

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")