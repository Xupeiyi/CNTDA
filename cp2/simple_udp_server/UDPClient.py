from socket import *
from config import server_name, server_port


with socket(AF_INET, SOCK_DGRAM) as client_socket:
    message = input('Input lowercase sentence: ')
    message = bytes(message, encoding="utf8")
    
    client_socket.sendto(message, (server_name, server_port))
    
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message)

