import sys

# one way to read from a command line argument
#   when you know how the input will look
ipAddress = sys.argv[-4]
ipPort = sys.argv[-3]
xCoor = sys.argv[-2]
yCoor = sys.argv[-1]

print ipAddress
print ipPort
print xCoor
print yCoor

# a 2d array representing the current board
#   we will need to read from the file to populate the array
w, h = 9, 9
board = [[0 for x in range(w)] for y in range(h)] 

# Taking a variable from the message and determing the 
#   action to take
# we need to determine how to check for sunken ships -- maybe global variable counters
#   that will increment each time you hit that ship until it max's out?

# response is the message sent back to the client
response = "void"

def process(x,y):
	if board[x,y] == '-':
		response = "HTTP/1.1 OK\nContent-Type:application/x-www-form-urlencoded\nContent-Length:7\n\nhit=0&sink=0\n\n\n"
	elif board[x,y] == 'c':
		# check for sink on 'c'
		response = "HTTP/1.1 OK\nContent-Type:application/x-www-form-urlencoded\nContent-Length:7\n\nhit=1&sink=0\n\n\n"
 	elif board[x,y] == 'b':
		# check for sink on 'b'
                response = "HTTP/1.1 OK\nContent-Type:application/x-www-form-urlencoded\nContent-Length:7\n\nhit=1&sink=0\n\n\n"
	elif board[x,y] == 'r':
		# check for sink on 'r'
                response = "HTTP/1.1 OK\nContent-Type:application/x-www-form-urlencoded\nContent-Length:7\n\nhit=1&sink=0\n\n\n"
	elif board[x,y] == 's':
 		# check for sink on 'c'
                response = "HTTP/1.1 OK\nContent-Type:application/x-www-form-urlencoded\nContent-Length:7\n\nhit=1&sink=0\n\n\n"
	elif board[x,y] == 'd':
 		# check for sink on 'c'
                response = "HTTP/1.1 OK\nContent-Type:application/x-www-form-urlencoded\nContent-Length:7\n\nhit=1&sink=0\n\n\n"
	else:
		response = "HTTP/1.1 400\nContent-Type:application/x-www-form-urlencoded\nContent-Length:11\n\nBad Request\n\n\n"


  
