def print_board(board):
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def get_move(player):
    move = input(f"Player {player}, enter your move (1-9): ")
    while not move.isdigit() or int(move) not in range(1, 10):
        move = input("Invalid move. Please enter a number between 1 and 9: ")
    return int(move) - 1

def check_win(board):
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != " ":
            return True
    return False

def tic_tac_toe():
    board = [" "] * 9
    player = "X"
    while not check_win(board) and " " in board:
        print_board(board)
        move = get_move(player)
        if board[move] == " ":
            board[move] = player
            player = "O" if player == "X" else "X"
        else:
            print("That space is already taken. Please try again.")
    print_board(board)
    if check_win(board):
        print(f"Player {player} wins!")
    else:
        print("It's a tie.")

tic_tac_toe()
