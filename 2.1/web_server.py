from socket import *
from threading import Thread
import sys 

def main(connection_socket):
    try:
        message = connection_socket.recv(20)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()

        connection_socket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        for i in range(0, len(outputdata)):
            connection_socket.send(outputdata[i].encode())

        connection_socket.close()
    except IOError:
        connection_socket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n".encode())

        connection_socket.close()

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(5)

while True:
    print("ready to serve...")
    connection_socket, addr = server_socket.accept()
    
    t = Thread(target=main, args=[connection_socket])
    t.start()

server_socket.close()
sys.exit()