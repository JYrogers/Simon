import random
import time
import board
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.D2)
led.direction = Direction.OUTPUT
led2 = DigitalInOut(board.D3)
led2.direction = Direction.OUTPUT
# pin configuration / setup
white = DigitalInOut(board.D6)
orange = DigitalInOut(board.D7)
black = DigitalInOut(board.D8)

white.direction = Direction.INPUT
orange.direction = Direction.INPUT
black.direction = Direction.INPUT

# main / infinite loop
while True:
    if white.value:
        led.value = not led.value
        time.sleep(.3)      
    if orange.value:
        time.sleep(.3)
        led2.value = not led2.value
    if black.value:
        print("Button with pull-down was pressed")
        time.sleep(.3)    

#Change the list name for my comfortability 
list1 = []
game_seq = []

def add_to_sequence(lsit):
    lsit.append(random.randint(0 , 3))

def display_sequence(lsit):
  #The P was there to see if the buttons were working. 
    for x in lsit:
        if x == 0:
            p = "red"
            print(p)
        elif x == 1:
            p = "green"
            print(p)
        elif x == 2:
            p = "Yellow"
            print(p)
        else:
            p = "Blue"
            print(p)

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
