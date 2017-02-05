import socket

TCP_IP = '129.31.212.117'
TCP_PORT = 8080
BUFFER_SIZE = 957  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
conn.send("You're connected in mfournial")  # echo
while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    if data:
        print "received data:", data

    conn.close()
