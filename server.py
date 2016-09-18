import sys
import socket

def Main():
    host = '127.0.0.1'  # this may change
    port = sys.argv[-2]
    file_name = sys.argv[-1]  # name of text file for baord, may have to cast to string
    w, h = 10, 10    # maybe use 2d array for board
    board = [[0 for x in range(w)] for y in range (h)]

    board_file = open((str)file_name, 'r')  # r for read only, r+ for read and write, w for write
    # create 2d array or other text file here
    # by reading from board_file object ie board_file.read() etc
    for i in range(h):
        board.append([])
        for j in range(w):
            board[i] = board_file.read(1)

    print board

    # create connection and listen for client
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    conn, addr = sock.accept()             # conn is connection object

    print 'Connection from: ' + str(addr)  # used for testing/debug only

    # this will run until killed by user, client will be invoked each play
    # all other functionallity will be done by calling other methods
    while True:
        data = conn.recv(1024)
        # maybe do a try except here??
        if not data:
            break
        print 'from connected user: ' + str(data)  # used for testing/debug only

        data = 'put something here'                # data will be x,y coords from client
        #read_board(data)
        reply = process_request()                  # reply will be message returned to client
        conn.send(reply)
    conn.close()


# read_board() used for reading board at coords sent from client
# will return hit, miss, sunk to be sent to reply method to be replied
# to clinet
def read_board():


# update_board() will record state of board
def update_board():


# process_reply() will take result of read_board and
# return reply variable to send proper reply back to client via conn.send(reply)
def process_reply():


if __name__ == '__main__':
    Main()