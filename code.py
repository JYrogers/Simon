import random
import time
import board
from digitalio import DigitalInOut, Direction

white = DigitalInOut(board.D10)
white.direction = Direction.INPUT
bluebutn = DigitalInOut(board.D8)
bluebutn.direction = Direction.INPUT
greenbtn = DigitalInOut(board.D6)
greenbtn.direction = Direction.INPUT
yellowbtn = DigitalInOut(board.D9)
yellowbtn.direction = Direction.INPUT
redbtn = DigitalInOut(board.D7)
redbtn.direction = Direction.INPUT

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

# main / infinite loop

def add_to_sequence(lsit):
    lsit.append(random.randint(0 , 3))
    sequence.append(new_color)
    
 


def display_sequence():

colors = (1,2,3,4)
def add(points):
    list1.append(random.choice(colors))
    points +=1
    print(points)
    return points
while True:
    inp = input(" 1 : Add to Sequence "
                "2 : Display Sequence "
                "3 : Exit Program ")
    print("")
    if inp.lower() == "1":
        add_to_sequence(list1)
    elif inp.lower() == "2":
        display_sequence(list1)
    elif inp.lower() == "3":
        print("Bye")
        break
    else:
        print("Invalid Input")
