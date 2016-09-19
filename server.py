import sys
import socket
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

    # **** all this commented out is if we were to use the socket library  *****
    # **** leave commented out if using the simplehttpserver library       *****
    # create connection and listen for client
    #sock = socket.socket()
    #sock.bind((host, int(port)))
    #sock.listen(1)
    #conn, addr = sock.accept()             # conn is connection object
    #print 'Connection from: ' + str(addr)  # used for testing/debug only
    # this will run until killed by user, client will be invoked each play
    # all other functionallity will be done by calling other methods
    #while True:
    #    # might have to put sock.listen() and/or sock.accept() inside while loop
    #    data = conn.recv(1024)
    #    # maybe do a try except here??
    #    if not data:
    #        break
    #    print 'from connected user: ' + str(data)  # used for testing/debug only
    #
    #    data = 'put something here'                # data will be x,y coords from client
    #    #read_board(data)
    #    reply = process_request()                  # reply will be message returned to client
    #    conn.send(reply)
    #conn.close()
    # ****** Leave above out it using simplehttpserver library

# read_board() used for reading board at coords sent from client
# will return hit, miss, sunk to be sent to reply method to be replied
# to clinet
def read_board():
    print 'read_board() not done, need to finish'

# update_board() will record state of board
def update_board():
    print 'update_board() not done, need to finish'


# process_reply() will take result of read_board and
# return reply variable to send proper reply back to client via conn.send(reply)
def process_reply():
    print 'process_reply() not done, need to finish'

if __name__ == '__main__':
    Main()