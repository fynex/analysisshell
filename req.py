import socket

def single_send(ip, port, data, receive_size=2048):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((ip,port))
    s.sendall(data)
    response = s.recv(receive_size)
    s.close()
    
    return response
