import socket

TCP_IP = '10.0.0.4'
TCP_PORT = 3000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("I'm listening")

conn, addr = s.accept()
print 'Connection address:', addr
conn.send("You're connected at home")  # echo
while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    if data:
        print "received data:", data

    conn.close()
