# This is our in-class tutorial for our Battleship project.
# This version of the game will have a ship that is 1 unit long.  To get a C, the
# ship needs to be 3 units long.
# To get a B, the game should have 3 ships of 3 different lengths, randomly placed
# horizontally or vertically around the board.
# To get an A, there must a human player and a computer player, two separate ship boards.

import random
# import the random library for the random number generator

import time
# import the time library so we can have a delay between turns

# begin with creating the game board.  for the beginner level it is 5 x 5 units

# append a row of "O"s, 5 times
board = [] #the guessing board for the user

for x in range(10): 
    board.append(["O"]*10)
#--------------------------------    
ship_board = [] #the board that shows where the computer's ships are

for y in range(10): 
    ship_board.append(["i"]*10)
#-------------------------------
user_board = [] #the board that has where the user inputted ships are

for z in range(10):
    user_board.append(["U"]*10)


#-------------------------------

#randomizer functions
def Random_Ori():
    return random.randint(0, 1)

def Random_Row(x, y):
    return random.randint(x, y)

def Random_Col(x, y):
    return random.randint(x, y)
    
#-------------------------------    
# function to print the board
def Print_Board(playerboard):
    for row in playerboard:
        print(" ". join(row))
        
print("Welcome to Battleship!  This game has three ship, which are 3, 5, and 7 units long. \n")
print("The board is 10 x 10.  You get 25 guesses to find the ships.  Good luck!  \n \n")
#Print_Board(board)
#print("\n")
#----------------------------------------------------------------------------------------
user_board = []

for z in range(10):
    user_board.append(["U"]*10)
    
#print the board
Print_Board(user_board)
#stuff

user_ships = 0

while user_ships < 3:
    if user_ships == 0: #first ship being loaded in
        print("Time to choose where you want to place your 3 unit ship.")
        user_ori = int(input("What orientation would you like? Type 0 for vertical. Type 1 for horizontal. "))
        if user_ori == 0: #vertical for 3 unit ship
            #limit the rows
            user_row = int(input("What row between 2 and 9 would you like to place the middle point of your ship? "))
            user_row = user_row - 1
            time.sleep(0.5)
            user_col = int(input("What column between 1 and 10 would you like to place the middle point of your ship? "))
            user_col = user_col - 1
            if user_row <= 8 and user_row >= 1 and user_col <= 9 and user_col >= 0:
                user_board[user_row][user_col] = "S"
                user_board[user_row + 1][user_col] = "S"
                user_board[user_row - 1][user_col] = "S"
                user_ships = user_ships + 1
            else:
                print("Row or column invalid. ")
        elif user_ori == 1: #hortizontal for 3 unit ship
            #limit the columns
            user_row = int(input("What row between 1 and 10 would you like to place the middle point of your ship? "))
            user_row = user_row - 1
            time.sleep(0.5)
            user_col = int(input("What column between 2 and 9 would you like to place the middle point of your ship? "))
            user_col = user_col - 1
            if user_col <= 8 and user_col >= 1 and user_row <= 9 and user_row >= 0:
                user_board[user_row][user_col] = "S"
                user_board[user_row][user_col + 1] = "S"
                user_board[user_row][user_col - 1] = "S"
                user_ships = user_ships + 1
            else:
                print("Row or column invalid. ")
        else:
            print("That's not a valid input for orientation.")
        Print_Board(user_board)
            #################SECOND SHIP LOOOOOOOL######################################
    elif user_ships == 1: #second ship being loaded in
        print("Time to choose where you want to place your 5 unit ship.")
        user_ori = int(input("What orientation would you like? Type 0 for vertical. Type 1 for horizontal. "))
        if user_ori == 0: #vertical for a 5 unit ship
            #limit the rows
            user_row = int(input("What row between 3 and 8 would you like to place the middle point of your ship? "))
            user_row = user_row - 1
            time.sleep(0.5)
            user_col = int(input("What column between 1 and 10 would you like to place the middle point of your ship? "))
            user_col = user_col - 1
            if user_row <= 7 and user_row >= 2 and user_col <= 9 and user_col >= 0:
                if user_board[user_row][user_col] == "S" or user_board[user_row + 1][user_col] == "S" or user_board[user_row + 2][user_col] == "S" or user_board[user_row - 1][user_col] == "S" or user_board[user_row - 2][user_col] == "S":
                    print("Uh oh! This ship collides with another you made. Choose a different spot.")
                else:
                    user_board[user_row][user_col] = "T"
                    user_board[user_row + 1][user_col] = "T"
                    user_board[user_row + 2][user_col] = "T"
                    user_board[user_row - 1][user_col] = "T"
                    user_board[user_row - 2][user_col] = "T"
                    user_ships = user_ships + 1
            else:
                print("Row or column invalid.")
        elif user_ori == 1: #horizontal for a 5 unit ship
            #limit the columns
            user_row = int(input("What row between 1 and 10 would you like to place the middle point of your ship? "))
            user_row = user_row - 1
            time.sleep(0.5)
            user_col = int(input("What column between 3 and 8 would you like to place the middle point of your ship? "))
            user_col = user_col - 1
            if user_col <= 7 and user_col >= 2 and user_row <= 9 and user_row >= 0:
                if user_board[user_row][user_col] == "S" or user_board[user_row][user_col + 1] == "S" or user_board[user_row][user_col + 2] == "S" or user_board[user_row][user_col - 1] == "S" or user_board[user_row][user_col - 2] == "S":
                    print("Uh oh! This ship collides with another you made. Choose a different spot.")
                else:
                    user_board[user_row][user_col] = "T"
                    user_board[user_row][user_col + 1] = "T"
                    user_board[user_row][user_col + 2] = "T"
                    user_board[user_row][user_col - 1] = "T"
                    user_board[user_row][user_col - 2] = "T"
                    user_ships = user_ships + 1
        else:
            print("That's not a valid input for orientation.")
        Print_Board(user_board)
             #################THIRD SHIP LOOOOOOOL######################################
    elif user_ships == 2: #third ship is being loaded in
        print("Time to choose where you want to place your 7 unit ship.")
        user_ori = int(input("What orientation would you like? Type 0 for vertical. Type 1 for horizontal. "))
        if user_ori == 0: #vertical for a 7 unit ship
            #limit the rows
            user_row = int(input("What row between 4 and 7 would you like to place the middle point of your ship? "))
            user_row = user_row - 1
            time.sleep(0.5)
            user_col = int(input("What column between 1 and 10 would you like to place the middle point of your ship? "))
            user_col = user_col - 1
            if user_row <= 6 and user_row >= 3 and user_col <= 9 and user_col >= 0:
                if user_board[user_row][user_col] == "S" or user_board[user_row + 1][user_col] == "S" or user_board[user_row + 2][user_col] == "S" or user_board[user_row + 3][user_col] == "S" or user_board[user_row - 1][user_col] == "S" or user_board[user_row - 2][user_col] == "S" or user_board[user_row - 3][user_col] == "S" or user_board[user_row][user_col] == "T" or user_board[user_row + 1][user_col] == "T" or user_board[user_row + 2][user_col] == "T" or user_board[user_row + 3][user_col] == "T" or user_board[user_row - 1][user_col] == "T" or user_board[user_row - 2][user_col] == "T" or user_board[user_row - 3][user_col] == "T":
                    print("Uh oh! This ship collides with another you made. Choose a different spot.")
                else:
                    user_board[user_row][user_col] = "Y"
                    user_board[user_row + 1][user_col] = "Y"
                    user_board[user_row + 2][user_col] = "Y"
                    user_board[user_row + 3][user_col] = "Y"
                    user_board[user_row - 1][user_col] = "Y"
                    user_board[user_row - 2][user_col] = "Y"
                    user_board[user_row - 3][user_col] = "Y"
                    user_ships = user_ships + 1
            else:
                print("Row or column invalid.")
        elif user_ori == 1: #horizontal for a 7 unit ship
            #limit the columns
            user_row = int(input("What row between 1 and 10 would you like to place the middle point of your ship? "))
            user_row = user_row - 1
            time.sleep(0.5)
            user_col = int(input("What column between 4 and 7 would you like to place the middle point of your ship? "))
            user_col = user_col - 1
            if user_col <= 6 and user_col >= 3 and user_row <= 9 and user_row >= 0:
                if user_board[user_row][user_col] == "S" or user_board[user_row][user_col + 1] == "S" or user_board[user_row][user_col + 2] == "S" or user_board[user_row][user_col + 3] == "S" or user_board[user_row][user_col - 1] == "S" or user_board[user_row][user_col - 2] == "S" or user_board[user_row][user_col - 3] == "S" or user_board[user_row][user_col] == "T" or user_board[user_row][user_col + 1] == "T" or user_board[user_row][user_col + 2] == "T" or user_board[user_row][user_col + 3] == "T" or user_board[user_row][user_col - 1] == "T" or user_board[user_row][user_col - 2] == "T" or user_board[user_row][user_col - 3] == "T":
                    print("Uh oh! This ship collides with another you made. Choose a different spot.")
                else:
                    user_board[user_row][user_col] = "Y"
                    user_board[user_row][user_col + 1] = "Y"
                    user_board[user_row][user_col + 2] = "Y"
                    user_board[user_row][user_col + 3] = "Y"
                    user_board[user_row][user_col - 1] = "Y"
                    user_board[user_row][user_col - 2] = "Y"
                    user_board[user_row][user_col - 3] = "Y"
                    user_ships = user_ships + 1
        else:
            print("That's not a valid input for orientation.")
        Print_Board(user_board)
#----------------------------------------------------------------------------------------
# add a delay before you guess so it feels more natural to play
time.sleep(1)

# We need to randomly place a ship on the board.  So, we'll choose one column
# and one row.  The x coordinate and y coordinate should be between 0 and 4.  If this
# were the A, B, or C level, you would also have randomly choose horizontal or vertical.
#------------------------FIGURE OUT THE SHIP THING---------------------------------------------------------------
#functions before i changed them loool
#def Random_Row():
#    return random.randint(0, len(board)-1)

#def Random_Col():
#    return random.randint(0, len(board)-1)
#---------------------------------------------




# right here, i'm trying to get the row and column of the first ship point. the first ship point is found in the middle
# since it's in the middle, it can't be on the edges, so the following code keeps it from spawning on the edges
num_ships = 0

while num_ships < 3:
    ship_ori = Random_Ori()
    if ship_ori == 0:
        #vertical
        if num_ships == 0: #if this is the first ship being loaded in, make it 3 units
            ship_col = Random_Col(0, len(board)-1)
            ship_row = Random_Row(1, len(board)-2)
            
            if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row + 1][ship_col] == "S" or ship_board[ship_row - 1][ship_col] == "S":
                print(" ")
            else:
                ship_board[ship_row][ship_col] = "S"
                ship_board[ship_row + 1][ship_col] = "S"
                ship_board[ship_row - 1][ship_col] = "S"
                num_ships = num_ships + 1
        elif num_ships == 1: #if this is the second ship being loaded in, make it 5 units
            ship_col = Random_Col(0, len(board)-1)
            ship_row = Random_Row(2, len(board)-3)
            
            if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row + 1][ship_col] == "S" or ship_board[ship_row + 2][ship_col] == "S" or ship_board[ship_row - 1][ship_col] == "S" or ship_board[ship_row - 2][ship_col] == "S":
                print(" ")
            else:
                ship_board[ship_row][ship_col] = "T"
                ship_board[ship_row + 1][ship_col] = "T"
                ship_board[ship_row + 2][ship_col] = "T"
                ship_board[ship_row - 1][ship_col] = "T"
                ship_board[ship_row - 2][ship_col] = "T"
                num_ships = num_ships + 1
        elif num_ships == 2: #if this is the third ship being loaded in, make it 7 units
            ship_col = Random_Col(0, len(board)-1)
            ship_row = Random_Row(3, len(board)-4)
            
            if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row + 1][ship_col] == "S" or ship_board[ship_row + 2][ship_col] == "S" or ship_board[ship_row + 3][ship_col] == "S" or ship_board[ship_row - 1][ship_col] == "S" or ship_board[ship_row - 2][ship_col] == "S" or ship_board[ship_row - 3][ship_col] == "S" or ship_board[ship_row][ship_col] == "T" or ship_board[ship_row + 1][ship_col] == "T" or ship_board[ship_row + 2][ship_col] == "T" or ship_board[ship_row + 3][ship_col] == "T" or ship_board[ship_row - 1][ship_col] == "T" or ship_board[ship_row - 2][ship_col] == "T" or ship_board[ship_row - 3][ship_col] == "T":
                print(" ")
            else:
                ship_board[ship_row][ship_col] = "Y"
                ship_board[ship_row + 1][ship_col] = "Y"
                ship_board[ship_row + 2][ship_col] = "Y"
                ship_board[ship_row + 3][ship_col] = "Y"
                ship_board[ship_row - 1][ship_col] = "Y"
                ship_board[ship_row - 2][ship_col] = "Y"
                ship_board[ship_row - 3][ship_col] = "Y"
                num_ships = num_ships + 1
    elif ship_ori == 1:
        #horizontal
        if num_ships == 0: #if this is the first ship being loaded in, make it 3 units
            ship_col = Random_Col(1, len(board)-2)
            ship_row = Random_Row(0, len(board)-1)
            
            if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row][ship_col + 1] == "S" or ship_board[ship_row][ship_col - 1] == "S":
                print(" ")
            else:
                ship_board[ship_row][ship_col] = "S"
                ship_board[ship_row][ship_col + 1] = "S"
                ship_board[ship_row][ship_col - 1] = "S"
                num_ships = num_ships + 1
        elif num_ships == 1: #if this is the second ship being loaded in, make it 5 units
            ship_col = Random_Col(2, len(board)-3)
            ship_row = Random_Row(0, len(board)-1)
            
            if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row][ship_col + 1] == "S" or ship_board[ship_row][ship_col + 2] == "S" or ship_board[ship_row][ship_col - 1] == "S" or ship_board[ship_row][ship_col - 2] == "S":
                print(" ")
            else:
                ship_board[ship_row][ship_col] = "T"
                ship_board[ship_row][ship_col + 1] = "T"
                ship_board[ship_row][ship_col + 2] = "T"
                ship_board[ship_row][ship_col - 1] = "T"
                ship_board[ship_row][ship_col - 2] = "T"
                num_ships = num_ships + 1
        elif num_ships == 2: #if this is the third ship being loaded in, make it 7 units
            ship_col = Random_Col(3, len(board)-4)
            ship_row = Random_Row(0, len(board)-1)
            
            if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row][ship_col + 1] == "S" or ship_board[ship_row][ship_col + 2] == "S" or ship_board[ship_row][ship_col + 3] == "S" or ship_board[ship_row][ship_col - 1] == "S" or ship_board[ship_row][ship_col - 2] == "S" or ship_board[ship_row][ship_col - 3] == "S" or ship_board[ship_row][ship_col] == "T" or ship_board[ship_row][ship_col + 1] == "T" or ship_board[ship_row][ship_col + 2] == "T" or ship_board[ship_row][ship_col + 3] == "T" or ship_board[ship_row][ship_col - 1] == "T" or ship_board[ship_row][ship_col - 2] == "T" or ship_board[ship_row][ship_col - 3] == "T":
                print(" ")
            else:
                ship_board[ship_row][ship_col] = "Y"
                ship_board[ship_row][ship_col + 1] = "Y"
                ship_board[ship_row][ship_col + 2] = "Y"
                ship_board[ship_row][ship_col + 3] = "Y"
                ship_board[ship_row][ship_col - 1] = "Y"
                ship_board[ship_row][ship_col - 2] = "Y"
                ship_board[ship_row][ship_col - 3] = "Y"
                num_ships = num_ships + 1
        #horizontal
        # ship_col = Random_Col(1, len(board)-2)
        # ship_row = Random_Row(0, len(board)-1)
        
        # if ship_board[ship_row][ship_col] == "S" or ship_board[ship_row][ship_col+1] == "S" or ship_board[ship_row][ship_col-1] == "S":
        #     print(" ")
        # else:
        #     ship_board[ship_row][ship_col] = "S"
        #     ship_board[ship_row][ship_col+1] = "S"
        #     ship_board[ship_row][ship_col-1] = "S"
        #     num_ships = num_ships + 1

print("You've placed all of your ships! Time to start playing!")
print("\n")
print("------------------------------------------------------------------------------------")
print("This is where the computer's ships are. it won't be here for the actual gameplay, this is just to show that my code works.")
Print_Board(ship_board)
#print("\n")
#Print_Board(board)
    




#ship_row = Random_Row()
#ship_col = Random_Col()
#ship_ori = Random_Ori()

#if ship_ori == 0:
    #vertical
#    if ship_row == 0:
#        ship_1 = ()
        
    
#elif ship_ori = 1:
    #horizontal

#----------------------------------------------------------------------------------------------------------------
# the ship_row and ship_col is the location of the ship.  If this were a C level 
# project, you would have to make it 3 units long and randomly decide if it is 
# horizontal or vertical.
counter_first_ship = 0
counter_second_ship = 0
counter_third_ship = 0

computer_counter_one = 0
computer_counter_two = 0
computer_counter_three = 0

first_sunk = False
second_sunk = False
third_sunk = False

comp1_sunk = False
comp2_sunk = False
comp3_sunk = False


game_won = False
# create the game play in a for loop, limited by the number of turns the user gets
while game_won == False:
    print("------------------------------------------------------------------------------------")
    # because this is the D level project, you can let the user input integers for the
    # row and column,  for the real project, you let the user input in the form 
    # "C4" or "A5" etc.
    Print_Board(board)
    guess_row = int(input("What row between 1 and 10 do you guess? "))
    guess_row = guess_row - 1
    time.sleep(0.5)
    guess_col = int(input("What column between 1 and 10 do you guess? "))
    guess_col = guess_col - 1
    time.sleep(0.5)
   
    # check if their guess is a hit, or a miss, or not on the board.  output the 
    # results.  when you build the next level, make sure the check if they already 
    # guessed that location
    
    if ship_board[guess_row][guess_col] == "S":
        board[guess_row][guess_col] = "X"
        Print_Board(board)
        time.sleep(0.5)
        print("You hit one part of my ship!")
        counter_first_ship = counter_first_ship + 1
        if counter_first_ship == 3:
            print("You sunk my 3 unit ship!")
            first_sunk = True
            if first_sunk == True and second_sunk == True and third_sunk == True:
                print("You sunk all my battleships! Good job!")
                game_won = True
                break
    elif ship_board[guess_row][guess_col] == "T":
        board[guess_row][guess_col] = "X"
        Print_Board(board)
        time.sleep(0.5)
        print("You hit one part of my ship!")
        counter_second_ship = counter_second_ship + 1
        if counter_second_ship == 5:
            print("You sunk my 5 unit ship!")
            second_sunk = True
            if first_sunk == True and second_sunk == True and third_sunk == True:
                print("You sunk all my battleships! Good job!")
                game_won = True
                break
    elif ship_board[guess_row][guess_col] == "Y":
        board[guess_row][guess_col] = "X"
        Print_Board(board)
        time.sleep(0.5)
        print("You hit one part of my ship!")
        counter_third_ship = counter_third_ship + 1
        if counter_third_ship == 7:
            print("You sunk my 7 unit ship!")
            third_sunk = True
            if first_sunk == True and second_sunk == True and third_sunk == True:
                print("You sunk all my battleships! Good job!")
                game_won = True
                break
    else:
        if guess_row < 0 or guess_row > 9 or guess_col < 0 or guess_col > 9:
        # this is when the guess is off the board
            print("That guess is not on the board.")
            time.sleep(0.5)
        elif board[guess_row][guess_col] == "-":
        # this is a spot that was already guessed
            print("Oops!  You already guessed that spot!")
            time.sleep(0.5)
        else:
        # this is if they missed
            board[guess_row][guess_col] = "-"
            print("You missed! Now it's the computer's turn!")
            time.sleep(0.5)
        #if turn == 24:
        #    print("Uh oh! You have run out of turns.  You didn't sink the ship. You lose.")
        #    print("The ship location was row %d and column %d" % (ship_row, ship_col))
        #    break
        time.sleep(0.5)
        # after each turn, you print the board and tell the user how many turns and how many
        # ships are left
        Print_Board(board)
        #print("You are on turn %d of 25 attempts." %(turn + 2))
        #print("You have one ship remaining, and it is 1 x 1 unit.")
        time.sleep(0.5)
        
    #computadoraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    
    print("------------------------------------------------------------------------------------")
    
    #this is the computer's guess. it's random, and it can't already be a place it guessed
    comp_point = False
    
    while comp_point == False:
        temp_row = Random_Row(0, len(board)-1)
        temp_col = Random_Col(0, len(board)-1)
        if user_board[temp_row][temp_col] == "-" or user_board[temp_row][temp_col] == "X" :
            print("")
        else:
            comp_row = temp_row
            comp_col = temp_col
            comp_point = True
            
    #after we make sure the place hasn't already been guessed, we can begin checking if it hit a ship
    if user_board[comp_row][comp_col] == "S":
        user_board[comp_row][comp_col] = "X"
        Print_Board(user_board)
        time.sleep(0.5)
        print("The computer hit one part of your ship!")
        computer_counter_one = computer_counter_one + 1
        if computer_counter_one == 3:
            print("The computer sunk your 3 unit ship!")
            comp1_sunk = True
            if comp1_sunk == True and comp2_sunk == True and comp3_sunk == True:
                print("The computer sunk all your battleships! You lose!")
                break
    elif user_board[comp_row][comp_col] == "T":
        user_board[comp_row][comp_col] = "X"
        Print_Board(user_board)
        time.sleep(0.5)
        print("The computer hit one part of your ship!")
        computer_counter_two = computer_counter_two + 1
        if computer_counter_two == 5:
            print("The computer sunk your 5 unit ship!") 
            comp2_sunk = True
            if comp1_sunk == True and comp2_sunk == True and comp3_sunk == True:
                print("The computer sunk all your battleships! You lose!")
                break
    elif user_board[comp_row][comp_col] == "Y":
        user_board[comp_row][comp_col] = "X"
        Print_Board(user_board)
        time.sleep(0.5)
        print("You hit one part of my ship!")
        computer_counter_three = computer_counter_three + 1
        if computer_counter_three == 7:
            print("You sunk my 7 unit ship!")
            comp3_sunk = True
            if comp1_sunk == True and comp2_sunk == True and comp3_sunk == True:
                print("The computer sunk all your battleships! You lose!")
                break
    else:
        if ship_row < 0 or ship_row > 9 or ship_col < 0 or ship_col > 9: #this will literally always be false lol
        # this is when the guess is off the board
            print("this isnt supposed to be here1.")
            time.sleep(0.5)
        if ship_board[comp_row][comp_col] == "-": #so will this lol
        # this is a spot that was already guessed
            print("this isnt supposed to be here2!")
            time.sleep(0.5)
        else:
        # this is if they missed
            user_board[comp_row][comp_col] = "-"
            print("The computer missed!")
            time.sleep(0.5)
            print("\n")
        #if turn == 24:
        #    print("Uh oh! You have run out of turns.  You didn't sink the ship. You lose.")
        #    print("The ship location was row %d and column %d" % (ship_row, ship_col))
        #    break
        time.sleep(0.5)
        # after each turn, you print the board and tell the user how many turns and how many
        # ships are left
        Print_Board(user_board)
        #print("You are on turn %d of 25 attempts." %(turn + 2))
        #print("You have one ship remaining, and it is 1 x 1 unit.")
        time.sleep(0.5)