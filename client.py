import sys
import socket

def Main():
    host = sys.argv[-4]
    port = sys.argv[-3]
    x_coor = sys.argv[-2]
    y_coor = sys.argv[-1]

    
    # print statments just for testing
    print host
    print port
    print x_coor
    print y_coor
    
    # 10x10 playing area, used for a2d array
    # client needs to keep track of opponents board per assignment instrucitons
    w,h = 10,10
    board = [[0 for x in range(w)] for y in range(h)] 

    # reply_message used to hold response from server and send to update board
    # instantiat reply_message to something
    reply_message = 'something for now'

    # open connection to server
    sock = socket.socket()
    sock.connect((host, port))

    fire_message()
    process_response()
    update_board()

    sock.close()


# fire_message() will send http post request to server and update
# reply message variable upon response from server, then call
# appropriate method to update board then close connection
def fire_message(x_coor, y_coor, host, port):
    sock = socket.socket()
    sock.connect((host, port))
    conn, addr = sock.accept()
    conn.request("POST", "FIRE", x_coor, y_coor)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()

    print 'fire_message() not done need to finish, put here to run and test program'

# update_board() will modify 2d array or text file
# maybe use a text file since the client will be invoked several times
# --> do we change the board.txt file or create a temp_board.txt and maintain the field?
def update_board():
    
    print 'update_board() not done need to finish, put here to run and test program'

# process_response() could be renamed if desired, just put here for place holder
# this method will take the response message from the server and call
# update_board() to update local copy of board and call any other required methods
def process_response():
    # if using variables from main need to put global in front ie global x_coor
    print 'process_response() not done need to finish, put here to run and test program'


if __name__ == '__main__':
    Main()
