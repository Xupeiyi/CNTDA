from socket import *
from config import server_name, server_port


with socket(AF_INET, SOCK_STREAM) as client_socket:
    client_socket.connect((server_name, server_port))
    sentence = input('Input lowercase sentence: ')
    sentence = bytes(sentence, encoding='utf-8')
    client_socket.send(sentence)
    modified_sentence = client_socket.recv(1024)
    print('From server: ', modified_sentence)

