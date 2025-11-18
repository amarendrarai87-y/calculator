board = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]

winning_moves = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

def display_board():
    print("\n" + "="*13)
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("="*13 + "\n")

def check_winner(player):
    for a, b, c in winning_moves:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_draw():
    return all(pos in ("X", "O") for pos in board)

def get_player_move(current_player):
    while True:
        choice = input(f"Player {current_player}, choose a position (1-9): ").strip()

        if not (choice.isdigit() and '1' <= choice <= '9'):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue
        
        if choice in board:
            return choice
        else:
            print("That position is already taken! Try again.")

print("=== TIC TAC TOE ===")
print("Player 1 = X")
print("Player 2 = O")

display_board()

current_player = "X"

while True:
    
    choice = get_player_move(current_player)

    index = board.index(choice)
    
    board[index] = current_player

    display_board()

    if check_winner(current_player):
        print(f"🎉 Player {current_player} wins!")
        break

    if check_draw():
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
