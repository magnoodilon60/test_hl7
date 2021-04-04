#client

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))

print('Conectado!!\n')

namefile = str(input('Informe o nome do arquivo: '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while True:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{namefile} recebido!!\n')