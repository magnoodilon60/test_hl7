#server

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7777))

print('Aguardando conexão:\n')

server.listen(5)

connection, address = server.accept()

namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for date in file.readlines():
        connection.send(data)
    
    print('Arquivo enviado!!')


