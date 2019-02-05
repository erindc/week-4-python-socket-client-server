import socket   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 9500))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if data == b'exit':
                break
            if data == b'Hello':
                conn.send(b'Hi')
            else:
                conn.send(b'Goodbye')