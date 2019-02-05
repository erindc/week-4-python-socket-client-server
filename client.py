import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('', 9500))
    while True:
        msg = input('Input something to send to the server (exit to quit): ').encode()
        s.sendall(msg)
        if msg.decode("utf-8") == 'exit':
            break
        data = s.recv(1024)
        print('Server response: ', data.decode("utf-8") )