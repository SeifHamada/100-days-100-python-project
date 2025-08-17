board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

current_player = "X"


def print_board(board):
    for i in range(3):
        print(f"{board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("---------")


while True:
    print_board(board)
    pos = int(input(f"Player {current_player}, choose your move (1-9): "))

    row = (pos - 1) // 3
    col = (pos - 1) % 3

    if board[row][col] not in ["X", "O"]:
        board[row][col] = current_player

        if board[0][0] == board[0][1] == board[0][2]:
            print_board(board)
            print(f"Player {board[0][0]} wins!")
            break
        elif board[1][0] == board[1][1] == board[1][2]:
            print_board(board)
            print(f"Player {board[1][0]} wins!")
            break
        elif board[2][0] == board[2][1] == board[2][2]:
            print_board(board)
            print(f"Player {board[2][0]} wins!")
            break

        if board[0][0] == board[1][0] == board[2][0]:
            print_board(board)
            print(f"Player {board[0][0]} wins!")
            break
        elif board[0][1] == board[1][1] == board[2][1]:
            print_board(board)
            print(f"Player {board[0][1]} wins!")
            break
        elif board[0][2] == board[1][2] == board[2][2]:
            print_board(board)
            print(f"Player {board[0][2]} wins!")
            break

        if board[0][0] == board[1][1] == board[2][2]:
            print_board(board)
            print(f"Player {board[0][0]} wins!")
            break
        elif board[0][2] == board[1][1] == board[2][0]:
            print_board(board)
            print(f"Player {board[0][2]} wins!")
            break

        full = True
        for r in range(3):
            for c in range(3):
                if board[r][c] not in ["X", "O"]:
                    full = False
        if full:
            print_board(board)
            print("It's a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    else:
        print("That spot is already taken. Try again!")
