import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 55555))
# set up a server
sock.listen()


while True:
    client, address = sock._accept()
    print(f"Connected to {address}")
    client.send("You are connected".encode())
    client.close()