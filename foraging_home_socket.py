

import socket, time

nPings = 10
timeBuff = []

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '192.168.0.10'
port = 12345
sock.bind((host,port))

sock.listen(5)

conn, addr = sock.accept()
print('Connection received')

for pp in range(nPings):
    conn.recv(1)
    timeBuff.append(time.time())
    conn.send('1'.encode())

for pp in range(nPings):
    conn.recv(1)
    time_str = '{}'.format(int(1000000*timeBuff[pp]))
    conn.send(time_str.encode())

conn.close()
print('All done')