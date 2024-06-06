import random

def print_board(board):
    for r in range(3):
        print("  " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if (r != 2):
            print("---|---|---")

def is_winner(board, player):
    # 가로, 세로, 대각선 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    board = [[' ' for x in range(3)] for y in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # 사용자의 입력 받기
        x = int(input("다음 수의 X좌표를 입력하시오: "))
        y = int(input("다음 수의 Y좌표를 입력하시오: "))

        # 사용자가 빈 곳에 X 표시하기
        if board[x][y] != ' ':
            print("이미 선택된 위치입니다. ")
            continue
        else:
            board[x][y] = 'X'

        # 게임 종료 조건 확인
        if is_winner(board, 'X'):
            print_board(board)
            print("축하합니다! 당신이 이겼습니다!")
            break
        elif is_board_full(board):
            print_board(board)
            print("비겼습니다!")
            break

        # 컴퓨터가 무작위 위치에 O 표시하기
        while True:
            comp_x = random.randint(0, 2)
            comp_y = random.randint(0, 2)
            if board[comp_x][comp_y] == ' ':
                board[comp_x][comp_y] = 'O'
                break

        # 게임 종료 조건 확인
        if is_winner(board, 'O'):
            print_board(board)
            print("안타깝지만, 컴퓨터가 이겼습니다!")
            break
        elif is_board_full(board):
            print_board(board)
            print("비겼습니다!")
            break

        print_board(board)