def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board, player):
    for i in range(3):
        if all([s == player for s in board[i]]):
            return True

        if all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True

    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {player}, enter the row (0-2): "))
        col = int(input(f"Player {player}, enter the column (0-2): "))

        while board[row][col] != " ":
            print("Cell already filled. Try again.")
            row = int(input(f"Player {player}, enter the row (0-2): "))
            col = int(input(f"Player {player}, enter the column (0-2): "))

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        player = "O" if player == "X" else "X"
    else:
        print_board(board)
        print("It's a tie!")


if __name__ == "__main__":
    tic_tac_toe()
