import sys
import SimpleHTTPServer
import SocketServer

def Main():
    #host = '127.0.0.1'  # this may change
    PORT = sys.argv[1]
    file_name = sys.argv[2]  # name of text file for baord, may have to cast to string
    w, h = 10, 10    # maybe use 2d array for board
    board = [[0 for x in range(w+1)] for y in range (h)]  # added 1 to w to hande newline char when readig file

    board_file = open(file_name, 'r')  # r for read only, r+ for read and write, w for write

    # variables to keep track of ships
    carrier = 5
    battleship = 4
    submarine = 3
    cRuiser =3
    destroyer = 2
    
    # create 2d array or other text file here
    # by reading from board_file object ie board_file.read() etc
    for i in range(h):
        for j in range(w+1):                  # added 1 to w to handle newline char
            board[i][j] = board_file.read(1)  # need to figure out .strip() to remove /n from file

    print board        # used for testing and debug only

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print 'Serving at port: ', PORT
    httpd.serve_forever()

    
# read_board() used for reading board at coords sent from client
# will return hit, miss, sunk to be sent to reply method to be replied
# to clinet
def read_board(x, y):
    global h
    global w
    global board
    global submarine
    global carrier
    global battleship
    global cRuiser
    global destroyer
    result = 'n'   # initialize result to something
    boat = 'non'   # variable to send what ship to check if sunk to processs reply

    if x >= w || x < 0:
        result = 'o'   # letter o for out of bounds 
        #return result
    if y >= h || y < 0:
        result = 'o'    # letter o
    if board[x][y] == '-':
        result = 'm'
        # this boat assignment is redundent because its initilized to non
        #boat = 'non'     
        # m for miss
        process_reply(result, boat)
    if board[x][y] == 'S':
        submarine -= 1
        boat = 'sub'
        result = 'h'
    if board[x][y] == 'B':
        battleship -= 1
        boat = 'bs'
        result = 'h'
    if board[x][y] == 'C':
        carrier -= 1
        boat = 'car'
        result = 'h'
    if board[x][y] == 'D':
        destroyer -= 1
        boat = 'des'
        result = 'h'
    if board[x][y] == 'R':
        cRuiser -= 1
        boat = 'cru'
        result = 'h'
    if board[x][y] == 'X':
        result = 'x'
    # we should never get here without an if case being true
    # but maybe put an else here to handle any error????
    update_board(x, y, result)
    process_reply(result, boat)

# update_board() will record state of board
def update_board(x, y, result):
    global board
    if result == 'm':
        board[x][y] = 'X'
    else:
        board[x][y] = result


# process_reply() will take result of read_board and
def process_reply(result, boat):
    global submarine
    global cRuiser
    global battleship
    global destroyer
    global carrier

    if boat == 'sub':
        if submarine == 0:
            # include hit in the message as it falls in the rules
            # send http reply for sunk submarine
    if boat == 'car':
        if carrier == 0:
            #include hit in the message as it falls in the rules
            # send sunk carrier http
    if boat == 'cru':
        if cRuiser == 0:
            #include hit in the message as it falls in the rules
            # send sunk cruiser http
    if boat == 'des':
        if destroyer == 0:
            #include hit in the message as it falls in the rules
            # send sund destroyer http
    if boat == 'bs':
        if battleship == 0:
            #include hit in the message as it falls in the rules
            # send sunk battleship http
    # if we get this far send result
    if result == 'h':
        # a hit but no sink
    if result == 'm':
        # no hit its a miss
    if result == 'o':
        # error 404 as its out of bounds
    if result == 'x':
        # error 400 as this has already been called
        # send proper http response
    

if __name__ == '__main__':
    Main()
