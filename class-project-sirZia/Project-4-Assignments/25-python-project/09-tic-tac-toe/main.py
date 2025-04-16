# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to check if a player has won
def check_winner(board, player):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (tie)
def is_board_full(board):
    return all(cell != " " for cell in board)

# Main game function
def tic_tac_toe():
    # Initialize the board
    board = [" " for _ in range(9)]
    current_player = "X"  # Player X starts first

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Ask the current player for their move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move! Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Check if the selected cell is empty
        if board[move] == " ":
            board[move] = current_player
            print_board(board)

            # Check if the current player has won
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            # Check if the board is full (tie)
            if is_board_full(board):
                print("It's a tie!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already taken! Try again.")

# Run the game
tic_tac_toe()