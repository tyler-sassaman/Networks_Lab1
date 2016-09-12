import socket

def Main():
    host = '127.0.0.1'
    port = 2526

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print 'Connection from: ' + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print 'from connected user: ' + str(data)
        data = 'put something here'
        print 'sending: ' + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()