# ------ Global Variables ------
# Noughts and Crosses Game

# Basis of board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is ongoing
game_continues = True

# Win vs. Tie
winner = None

# Player turn
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board() # Display the board first

    while game_continues: # Loop game until game is over

        # Give a turn to a player
        handle_turn(current_player)

        # Check game has ended
        check_game_over()

        # Flip to other player
        flip_player()

    # Game has ended
    if winner == " X " or winner == " O ":
        print(winner + " won")
    elif winner == None:
        print("Tie")

def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ") # User chooses a square

    valid = False # Prevents player overwritting other player's input
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        
        position = int(position) - 1 # Position is - 1 as board is 0-8

        if board[position] == "-":
            valid = True
        else: 
            print("You cannot go there. Go again.")

    
    board[position] = player
    
    display_board()

def check_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    global winner
    
    # check rows
    row_winner = check_rows()
    
    # check columns
    column_winner = check_columns()
    
    # check diagonals
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    
    elif column_winner:
        winner = column_winner
    
    elif diagonal_winner:
        winner = diagonal_winner

    return

def check_rows():
    global game_continues

    # Check rows add up
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # Return winner
    if row_1 or row_2 or row_3:
        game_continues = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_continues

    # Check columns add up
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # Return winner
    if column_1 or column_2 or column_3:
        game_continues = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_continues

    # Check diagonals add up
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # Return winner X or O
    if diagonal_1 or diagonal_2:
        game_continues = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_continues
    if "-" not in board:
        game_continues = False
    return

def flip_player():
    # Global variable
    global current_player

    # if current player is X, then change to O
    if current_player == "X":
        current_player = "O"

    # if current player is O, then change to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()



# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player
