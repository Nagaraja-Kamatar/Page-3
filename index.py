import random

def create_board(rows, cols, mines):
    # Create an empty board
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Place mines randomly on the board
    placed_mines = 0
    while placed_mines < mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != '*':
            board[row][col] = '*'
            placed_mines += 1
    
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]):
                if board[row + i][col + j] == '*':
                    count += 1
    return count

def reveal_empty(board, row, col, visited):
    if (row, col) in visited or board[row][col] != ' ':
        return
    
    visited.add((row, col))
    mines_count = count_adjacent_mines(board, row, col)
    if mines_count > 0:
        board[row][col] = str(mines_count)
    else:
        board[row][col] = '0'
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]):
                    reveal_empty(board, row + i, col + j, visited)

def play_game():
    rows = 8
    cols = 8
    mines = 10
    board = create_board(rows, cols, mines)
    print_board(board)
    uncovered_count = 0

    while True:
        try:
            row = int(input('Enter row (0 to {}): '.format(rows - 1)))
            col = int(input('Enter column (0 to {}): '.format(cols - 1)))
        except ValueError:
            print('Please enter valid row and column numbers.')
            continue
        
        if not (0 <= row < rows and 0 <= col < cols):
            print('Please enter row and column within range.')
            continue
        
        if board[row][col] == '*':
            print('Game Over! You hit a mine.')
            break
        
        if board[row][col] == ' ':
            visited = set()
            reveal_empty(board, row, col, visited)
            uncovered_count += 1
        else:
            uncovered_count += 1
        
        print_board(board)
        
        if uncovered_count == rows * cols - mines:
            print('Congratulations! You win!')
            break

if __name__ == "__main__":
    play_game()