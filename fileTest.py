w, h = 10, 10
board = [[0 for x in range(w)] for y in range (h)]

board_file = open('board.txt', 'r')  # r for read only, r+ for read and write, w for write
# create 2d array or other text file here
# by reading from board_file object ie board_file.read() etc
for i in range(h):
    for j in range(w):
        board[i][j] = board_file.read(1)

print board[1][3]
