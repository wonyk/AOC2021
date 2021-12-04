f = open("input.txt", "r")

draw_nums = f.readline().strip().split(',')

all_bingo_boards = []

while True:
    linePad = f.readline()
    if linePad == '':
        break

    board = []
    for i in range(5):
        row = f.readline().strip()
        rowArr = [int(n) for n in row.split()]
        board.append(rowArr)
    all_bingo_boards.append(board)

def check_row(board, row):
    return all([board[row][i] == -1 for i in range(5)])

def check_col(board, col):
    return all([board[i][col] == -1 for i in range(5)])

def checkRightDiag(board):
    return all([board[i][i] == -1 for i in range(5)])

def checkLeftDiag(board):
    return all([board[i][4-i] == -1 for i in range(5)])

def check_diag(board, row, col):
    # If does not affect diagonal, ignore
    if row == col or row == 4 - col:
        return checkRightDiag(board) or checkLeftDiag(board)
    return False

def check_all(board, row, col):
    return check_row(board, row) or check_col(board, col) or check_diag(board, row, col)

def checkStatus(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == int(num):
                board[i][j] = -1
                return check_all(board, i, j)
    return False

def get_score(board, draw):
    sum = 0
    for i in range(5):
        for j in range(5):
            sum += board[i][j] if board[i][j] != -1 else 0
    return sum * int(draw)

def part2(draw_index, boards, draws):
    bingo_boards = boards.copy()
    for i in range(draw_index + 1, len(draws)):
        draw = draws[i]

        if len(bingo_boards) == 1 and checkStatus(bingo_boards[0], draw):
            print('Part 2:', get_score(bingo_boards[0], draw))
            return

        last_board_remaining = []
        for board in bingo_boards:
            if not checkStatus(board, draw):
                last_board_remaining.append(board)
        bingo_boards = last_board_remaining


def part1(bingo_boards, draws):
    for index, draw in enumerate(draws):
        foundWinner = False
        new_board = bingo_boards.copy()
        for board in bingo_boards:
            if checkStatus(board, draw):
                foundWinner = True
                print('Part 1:', get_score(board, draw))
                new_board.remove(board)
                
        if foundWinner:
            part2(index, new_board, draws)
            break

part1(all_bingo_boards, draw_nums)