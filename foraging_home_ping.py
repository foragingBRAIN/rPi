

import socket, time

def serverConnect():
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = '192.168.0.10'
    port = 12345
<<<<<<< HEAD
    sock.connect((host,port))
    return sock
=======

    sock.connect((host,port))
    return sock

    conn = sock.connect((host,port))
    print('Connection received from {}'.format(host))
    return sock,conn

>>>>>>> 3a22b635888ae9683d5852922048629e8c8cb431

def pingServer(sock):
    tList = []
    tList.append(time.time())
    sock.send('0'.encode())
    msg = sock.recv(1)
    tList.append(time.time())
    sock.send('1'.encode())
    msg = sock.recv(1024)
    tList.append(int(msg.decode())/1000000)
    return tList

def closeConnection(sock):
    sock.send('2'.encode())
    sock.close()
    print('Connection closed')
