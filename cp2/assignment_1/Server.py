from socket import *
from config import server_port
import datetime as dt


with socket(AF_INET, SOCK_STREAM) as server_socket:
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print('Ready to serve...\n')
    
    while True:
        connection_socket, addr = server_socket.accept()
        
        with connection_socket:
            message = connection_socket.recv(1024).decode()
            
            print(f'--------------got request at {dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}-----------------')
            for msg in message.split('\r\n'):
                print(msg)

            filename = message.split()[1]
            try:
                with open(filename[1:], 'r') as f:
                    outputdata = f.read()
                # Send one HTTP header line into socket
                header = ' HTTP/1.1 200 OK\n' \
                         + ' Connection: close\n' \
                         + ' Content-Type: text/html\n' \
                         + ' Content-Length: {}\n\n'.format(len(outputdata))
            except FileNotFoundError:
                # Send response message for file not found
                filename = message.split()[1]
                with open('./html/404.html', 'r') as f:
                    outputdata = f.read()
                header = ' HTTP/1.1 404 NOT FOUND\n' + \
                         + ' Connection: close\n' \
                         + ' Content-Type: text/html\n' \
                         + f' Content-Length: {}\n\n'.format(len(outputdata))
            finally:
                connection_socket.send(header.encode())
                for i in range(0, len(outputdata)):
                    connection_socket.send(outputdata[i].encode())

