from socket import *


server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The server is ready to receive')


def modify_message(msg):
    print(f'modifying message: {msg}')
    modified_msg = msg.upper()
    return modified_msg


while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = modify_message(message)
    server_socket.sendto(modified_message, client_address)
    
    

