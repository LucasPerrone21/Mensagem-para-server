import socket
IP = ''  #alterar quando for usar outro computador como server

PORTA = 12345


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (IP, PORTA) 
tcp.connect(destino)
msg = None
while msg != 'break':
  msg = input()
  tcp.send(bytes(msg.encode('utf-8')))
tcp.close()
