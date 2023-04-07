import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
porta = 12345
meu_IP = ''
orig = (meu_IP, porta)
server.bind(orig)
server.listen()
while True:
    con,client = server.accept()
    print(f'{client[0]} se juntou a conexão')
    while True:
        recuperado = con.recv(1024)
        msg = recuperado.decode('utf-8')
        if msg == 'break':
            print(f'{client[0]} finalizou a conexão com o servidor')
            break
        print(f'{client[0]} falou: {msg}')
    con.close()
    break

        
