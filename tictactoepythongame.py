import random

# displays the board
def display_board(board):
    for x in range(3):  # Prints out the empty board
        for y in range(3):
            print(board[x][y], end=" ")
        print("")

# starts the tic tac toe game
def startgame():
    print("Welcome to Tic-Tac-Toe : ")

    winner_choice = "" # this variable holds the winners shape

    player_name = input("Enter your name : ") # the name of the player
    enemy_name = input("Enter a name for the AI opponent : ") # the name of the enemy AI

    player_choice = input("Will you be X or O? ") # let the player decide which one they want to be
    if(player_choice.upper() == "X"):
        enemy_choice = "O" # set enemy AI to be O
    elif(player_choice.upper() == "O"):
        enemy_choice = "X" # set enemy AI to be X



    game_board = [["_","_","_"], ["_","_","_"] , ["_","_","_"]] # store all player and enemy content here

    GameOver = False # boolean flag
    while(GameOver != True): # keep the game going until the boolean flag becomes true

        display_board(game_board) # call this func to display the game board
        player_turn(player_choice,game_board, enemy_choice) # Lets the user use their turn

        VictoryInARow = check_rows(game_board, player_choice, enemy_choice, player_name,enemy_name)  # check the rows for three in a row
        VictoryInAColumn = check_columns(game_board, player_choice, enemy_choice, player_name,enemy_name)
        VictoryInADiagonal = check_diagonals(game_board, player_choice, enemy_choice, player_name,
                                             enemy_name)  # check the diagonals of the board

        if (VictoryInARow == True):  # if there were three X or Os in a row then end the game
            GameOver = True
            break
        elif(VictoryInAColumn == True):
            GameOver = True
            break
        elif(VictoryInADiagonal == True):
            GameOver = True
            break

        FullBoard = check_for_fullboard(player_choice, enemy_choice, game_board)  # checks to see if the board is full

        if(FullBoard == True): # if the board IS full at this point then end the game
            GameOver = True
            break
        else: # if the board isnt full then let the AI make their move
            AI_turn(player_choice, enemy_choice, game_board, enemy_name)  # Lets the AI make their turn

    display_board(game_board) # display the final results at the end of the game
    print("Game Over!") # print a game over message before quitting


# this function checks to see if the user or AI has three in a row
def check_rows(board, p_choice, ai_choice, name_of_player,name_of_opponent):

    VictoryAchieved = False

    print("\n")
    for x in range(3):     # CHECK EACH ROW TO SEE IF THERE IS THREE SHAPES IN A ROW
        if(board[x][0] ==  p_choice and board[x][1] ==  p_choice and board[x][2] ==  p_choice): # all three in the current row are X's
            VictoryAchieved = True
            print(name_of_player + " is the winner!")
        elif(board[x][0] == ai_choice and board[x][1] == ai_choice and board[x][2] == ai_choice): # all three in the current row are O's
            VictoryAchieved = True
            print(name_of_opponent  + " is the winner!")
    return VictoryAchieved

# this function checks to see if the user or AI has three in a column
def check_columns(board, p_choice, ai_choice, name_of_player,name_of_opponent):
    VictoryStatus = False

    for x in range(1):
        for y in range(3):
            if(board[x][y] == p_choice and board[x + 1][y] == p_choice and board[x + 2][y] == p_choice): # all three in the current column are X's
                VictoryStatus = True
                print(name_of_player + " is the winner!")
                break
            elif(board[x][y] == ai_choice and board[x + 1][y] == ai_choice and board[x + 2][y] == ai_choice): # all three in the current column are O's
                VictoryStatus = True
                print(name_of_opponent + " is the winner!")
                break
        if(VictoryStatus == True): # if bool flag is true, end the outer for loop
            break
    return VictoryStatus

# this function checks to see if the user or AI has three in a diagonal
def check_diagonals(board, p_choice, ai_choice, name_of_player,name_of_opponent):
    VictoryStatus = False

    for x in range(1):
        for y in range(1):
            if(board[x][y] == p_choice and board[x+1][y+1] == p_choice and board[x + 2][y + 2] == p_choice): # all three in the current diagonal are X's
                VictoryStatus = True
                print(name_of_player + " is the winner!")
                break
            elif(board[x][y] ==  ai_choice and board[x + 1][y +1] == ai_choice and board[x + 2][y +2] ==  ai_choice): # all three in the current diagonal are O's
                VictoryStatus = True
                print(name_of_opponent + " is the winner!")
                break
        if(VictoryStatus == True):
            break

    if(VictoryStatus != True): # if three matching shapes were not found in the first diagonal, check the opposite diagonal
        for x in range(1):
            for y in range(1):
                if(board[x][y +2] == p_choice and board[x+1][y+1] == p_choice and board[x + 2][y] == p_choice):  # all three in the current diagonal are X's
                    print(name_of_player + " is the winner!")
                    VictoryStatus = True
                    break
                elif(board[x][y +2] ==  ai_choice and board[x + 1][y +1] ==  ai_choice and board[x + 2][y] ==  ai_choice):  # all three in the current diagonal are O's
                    print(name_of_opponent + " is the winner!")
                    VictoryStatus = True
                    break
            if(VictoryStatus == True):
                break

    return VictoryStatus


# allows the user to select where they want to place their X or O.
def player_turn(choice,board, ai_choice):
    print("\n")
    ValidPosition = False # bool flag that is False until the user picks an empty position on the board
    chosen_square = int(input("Select a square to place your X or O on : "))

    while (chosen_square < 1 or chosen_square > 9):  # keep looping until player enters a valid number
        print("Invalid Number! Please select a number from 1 to 9!")
        chosen_square = int(input("Select a square to place your X or O on : "))

    while(ValidPosition != True): # keep looping until the player selects an EMPTY SPOT
        if(chosen_square == 1 or chosen_square == 2 or chosen_square == 3): # if the number chosen is in the first row
            x_index = 0
            y_index = chosen_square - 1
        elif (chosen_square == 4 or chosen_square == 5 or chosen_square == 6):  # if the number is in the second row
            x_index = 1
            y_index = chosen_square - 4
        else:  # if the number is in the third row
            x_index = 2
            y_index = chosen_square - 7

        if(board[x_index][y_index] == choice or board[x_index][y_index] == ai_choice): # if the spot on the board is filled already
            print("This space has been taken already!") # let the user know the spot is filled
            chosen_square = int(input("Select a square to place your X or O on : ")) # ask the user for a new number from 1 to 9

            while (chosen_square < 1 or chosen_square > 9):  # keep looping until player enters a valid number
                print("Invalid Number! Please select a number from 1 to 9!")
                chosen_square = int(input("Select a square to place your X or O on : "))
        else: # the spot on the board is not filled yet so its a valid position for the user to pick
            ValidPosition = True # set the bool flag to true and exit the while loop

    if(chosen_square == 1 or chosen_square == 2 or chosen_square == 3 ): # the number is in the first row
        place_in_row_1(board, chosen_square, choice)# place the player choice in the empty space in the first row

    elif(chosen_square == 4 or chosen_square == 5 or chosen_square == 6): # the number is in the second row
        place_in_row_2(board,chosen_square, choice) # place the player choice in the empty space in the second  row
    else: #  the number is in the third row
        place_in_row_3(board, chosen_square, choice) # place the player choice in the empty space in the third row


# allows  the AI to make a move on the tic tac toe board
def AI_turn(player_choice, ai_enemy_choice, board, name_of_enemy):

    print(name_of_enemy + " is making their move!")

    available_spaces_y = [0,1,2]  # list that holds y index value
    available_spaces_x = [0,1,2] # list that holds x index value

    AI_X_Index = random.choice(available_spaces_x) # randomly chooses one of the X values in the list
    AI_Y_Index = random.choice(available_spaces_y) # randomly chooses one of the Y values in the list

    ''' Enters the loop if the index values above were taken up by the player already.
    The loop will change the X and Y index values over again until it finds a spot that 
    hasnt been taken by the player already '''

    while(board[AI_X_Index][AI_Y_Index] == player_choice or board[AI_X_Index][AI_Y_Index] == ai_enemy_choice):
        AI_Y_Index = random.choice(available_spaces_y)
        AI_X_Index = random.choice(available_spaces_x)


    board[AI_X_Index][AI_Y_Index] = ai_enemy_choice # places the AI's X or O in this empty spot on the board

    print(name_of_enemy + " is done making their move!")

# places an X or O on a specific part of the board in row 1
def place_in_row_1(board, square_num, choice):
    board[0][square_num - 1] = choice # places an X or O in the correct spot


# places an X or O on a specific part of the board in row 2
def place_in_row_2(board, square_num, choice):
    board[1][square_num - 4] = choice # places an X or O in the correct spot


# places an X or O on a specific part of the board in row 3
def place_in_row_3(board, square_num, choice):
    board[2][square_num - 7] = choice # places an X or O in the correct spot

# checks the entire board to see if all spaces have been taken up, if so then the game will end!
def check_for_fullboard(p_choice,ai_choice, board):
    BoxesFull = 0
    IsFull = False

    for x in range(3):
        for y in range(3):
            if(board[x][y] == p_choice or board[x][y] == ai_choice):
                BoxesFull += 1
    if(BoxesFull == 9):
        print("There are no more spaces available to use!")
        IsFull = True

    return IsFull

def main():

    PlayAgain = True
    while(PlayAgain): # Start the game and if the user wants to play again then the game will reset
        startgame()
        choice = input("Would you like to play again? (Y/N) : ")
        if(choice != "Y"):
            break

main()
