import random
import time
import board
from digitalio import DigitalInOut, Direction

white = DigitalInOut(board.D10)
white.direction = Direction.INPUT
bluebutn = DigitalInOut(board.D8)
bluebutn.direction = Direction.INPUT
greenbutn = DigitalInOut(board.D6)
greenbutn.direction = Direction.INPUT
yellowbutn = DigitalInOut(board.D9)
yellowbutn.direction = Direction.INPUT
redbutn = DigitalInOut(board.D7)
redbutn.direction = Direction.INPUT

red = DigitalInOut(board.D2)
green = DigitalInOut(board.D4)
yellow = DigitalInOut(board.D3)
blue = DigitalInOut(board.D5)

red.direction = Direction.OUTPUT
green.direction = Direction.OUTPUT
yellow.direction = Direction.OUTPUT
blue.direction = Direction.OUTPUT

sequence = []
score = 0
#Initiliazing the variables/list


def add_to_sequence(lsit):
    lsit.append(random.randint(0 , 3))
    sequence.append(new_color)
    
 


def display_sequence():
    #This function displays the sequence by using the LEDs
    for color in sequence():
        if color == 0:
            red.value = not red.value
            time.sleep(0.3)
            red.value = not.red.value
        elif color == 1:
            green.value = not green.value
            time.sleep(0.3)
            green.value = not green.value
        elif color == 2:
            yellow.value = not yellow.value
            time.sleep(0.3)
            yellow.value = not yellow.value
        elif color == 3:
            blue.value = not blue.value
            time.sleep(0.3)
            blue.value = not blue.value
        time.sleep(0.3)  # Delay between colors

def player_input():
    #Function that captures the player's inputs and sees if it matches the sequence
    seq = []
    for i in range(len(sequence)):
        right = False:
        while not right: 
                if redbutn.value:
                    seq.append(0)
                    red.value = not red.value
                    time.sleep(0.5)
                    red.value = not red.value
                    correct = True
            elif greenbutn.value:
                    seq.append(1)
                    green.value = not green.value
                    time.sleep(0.5)
                    green.value = not green.value
                    correct = True
            elif yellowbutn.value:
                    seq.append(2)
                    yellow.value = not yellow.value
                    time.sleep(0.5)
                    yellow.value = not yellow.value
                    correct = True
            elif bluebutn.value:
                    seq.append(3)
                    blue.value = not blue.value
                    time.sleep(0.5)
                    blue.value = not blue.value
                    correct = True
            time.sleep(0.1)  
    return seq


def startgame():
    #Begins the game and adds the score
    global score
    while True:
        print('Press the white button to begin')
        red.value = green.value = yellow.value = blue.value = True
        time.sleep(0.5)
        red.value = green.value = yellow.value = blue.value = False
        tiome.sleep(0.5)
        while not white.value:
            time.sleep(0.1)

score = 0
seqeunce.clear()

def game_over(score):
    #Ends the game after the user fails
    red.value = green.value = yellow.value = blue.value = True
    time.sleep(0.5)
    red.value = green.value = yellow.value = blue.value = False
    time.sleep(0.5)
    for i in range(score):
        red value = not red.value
        time.sleep(0.2)
        red.value = not red.value
        time.sleep(0.2)
        sequence.clear()
        game_start()

startgame()
game_over()



