import random

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print("  " + " | ".join(row))
        if row != board[-1]:
            print(" ---|---|---")

def is_winner(board, player):
    """Checks if a player has won."""
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check row
            return True
        if all(board[j][i] == player for j in range(3)):  # Check column
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

def main():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        while True:
            try:
                x = int(input("Enter the X coordinate (0-2): "))
                y = int(input("Enter the Y coordinate (0-2): "))
                if board[x][y] == ' ':
                    board[x][y] = 'X'
                    break
                else:
                    print("That position is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 2.")

        # Check for a winner or a tie
        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)

        # Computer's turn
        while True:
            comp_x = random.randint(0, 2)
            comp_y = random.randint(0, 2)
            if board[comp_x][comp_y] == ' ':
                board[comp_x][comp_y] = 'O'
                break

        # Check for a winner or a tie
        if is_winner(board, 'O'):
            print_board(board)
            print("Sorry, the computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)

if __name__ == "__main__":
    main()
