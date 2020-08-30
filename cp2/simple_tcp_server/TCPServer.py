from socket import *
from config import server_port

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('The server is ready to receive')

while True:
    connection_socket, addr = server_socket.accept()
    with connection_socket:
        sentence = connection_socket.recv(1024)
        capitalized_sentence = sentence.upper()
        connection_socket.send(capitalized_sentence)

