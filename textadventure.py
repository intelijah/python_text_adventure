# TEXT ADVENTURE by Elijah #
############################

# a 2D dictionary of rooms where:
# key = integer to keep track of y position of room
# value = is itself dictionary where:
#   key = integer to keep track of the x position of the room
#   value = string that holds the room information ('None' is the boundaries so that the player doesn't go off the map
mapOfGame = {1:{1:'None', 2:'None',            3:'None',         4:'None',        5:'None'},
             2:{1:'None', 2:'None',            3:'You found a secret here before. You can go S.',     4:'None',        5:'None'},
             3:{1:'None', 2:'A raccoon comes up and bites you and the hand! Hope you don\'t get rabies! You can go E.',  3:'There was a key here, I remember! You can go E, W, S.', 4:'There\'s nothing here. You can Go W.',  5:'None'},
             4:{1:'None', 2:'None',            3:'You are in the woods, and you must find your car. You can go NORTH or SOUTH.',      4:'None',        5:'None'},
             5:{1:'None', 2:'None',            3:'Nothing here. You can go N or S.',   4:'None',        5:'None'},
             6:{1:'None', 2:'You found a key here before... You can go E',          3:'Nothing here. You can go N, E, or W.',   4:'You found your car! You win!',    5:'None'},
             7:{1:'None', 2:'None',            3:'None',         4:'None',        5:'None'}}

# initialize room to the first room
y, x = 4, 3

# message that will appear if the room string value is 'None'
errorMessage = "You can't go that way"

# function that handles north, south, east, and west inputs. takes an argument that will be the specified cardinal direction
def useInputs(string):
    # get global variables x and y for editing specificRoom dictionary (equal to mapOfGame[y][x])
    global x, y, specificRoom
    
    # if input = north, y-=1 (go up). If going up means hitting a 'None' room, stay in same room and print error message
    if (string == 'N' or string == 'n' or string == 'north' or string == 'North'):
        if mapOfGame[y-1][x] != 'None':
            y-=1
        else:
            print(errorMessage)
            
    # same but for south
    elif (string == 'S' or string == 's' or string == 'south' or string == 'South'):
        if mapOfGame[y+1][x] != 'None':
            y+=1
        else:
            print(errorMessage)

    #same but for east
    elif (string == 'E' or string == 'e' or string == 'east' or string == 'East'):
        if mapOfGame[y][x+1] != 'None':
            x+=1
        else:
            print(errorMessage)

    #same but for west
    elif (string == 'W' or string == 'w' or string == 'west' or string == 'West'):
        if mapOfGame[y][x-1] != 'None':
            x-=1
        else:
            print(errorMessage)

# booleans to handle game progress (getting keys, etc.)
hasKey = False
hasKey2 = False
hasSecret = False

# boolean for game loop that will run the game if True, quit the game if False
running = True

# Title screen
print("Welcome to the game where you must find your car!\nType and enter anything to play!")
input()

# print the first room first, then go into game loop so that room strings are not repeated

print(mapOfGame[y][x])

############
#GAME LOOP:#
############

while running:
    
    # input string that will be passed to useInputs
    string = input()
    useInputs(string)

    #special cases if the room is entered; keeps progress of game, different than default room
    if x == 3 and y == 3:  # Check if the current position is (3, 3) where the key is located
        if hasKey == False:
            print("You found a key! You pick it up. You can go E, W, S.")
            hasKey = True
        else:
            print(mapOfGame[y][x])

    elif x == 2 and y == 6:
        if hasKey == True and hasKey2 == False:
            print("There is a chest. You have a key for it! You open the chest and find your car keys! Now find the car! You can go E.")
            hasKey2 = True
        elif hasKey == False and hasKey2 == False:
            print("You found a Key! You can go E.")
        else:
            print(mapOfGame[y][x])

    elif x == 3 and y == 2:
        if hasSecret == False:
            print("You found a secret! It's useless... You can go S.")
            hasSecret == True
        else:
            print(mapOfGame[y][x])

    
    elif x == 4 and y == 6:
        if hasKey2 == False:
            print("You found your car, but you don't have a key. You can go W.")
        else:
            pass         # endgame scenario
            print(mapOfGame[y][x])
            running = False

    # if there is no special cases, say the default room string
    else:
        specificRoom = mapOfGame[y][x]
        print(specificRoom)
        
        
print("Thanks for playing!")
        
