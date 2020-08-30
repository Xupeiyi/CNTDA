from socket import *

server_name = '192.168.1.8'
server_port = 12000
with socket(AF_INET, SOCK_DGRAM) as client_socket:
    message = input('Input lowercase sentence: ')
    message = bytes(message, encoding="utf8")
    
    client_socket.sendto(message, (server_name, server_port))
    
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message)

