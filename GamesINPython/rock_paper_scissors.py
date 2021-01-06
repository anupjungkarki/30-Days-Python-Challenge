# This is the game built in python programming
import time 
import random

roke = 1
paper = 2
scissors = 3

names = {rock:"Rock", paper:"Paper", scissor = "Scissor"}
rules = {rock:scissors , paper:rock , scissors:paper}

player_score = 0
computer_score = 0

def start():
    print "Let's Play a game Rock , Paper ,Scissor 😄"
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1,3)
    result(player,computer)
    return play_again()

def move():
    while True:
        

