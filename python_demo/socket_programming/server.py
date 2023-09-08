from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost", 8088))
# server.bind(("127.0.0.1", 8087))

server.listen()
print("Server is listening....")
connect_obj, address = server.accept() # connection object, address

print(f"Server accepted client connection....{address}")

connect_obj.send(bytes("server: connection acknowledged", "utf-8"))
#
# print(connect_obj.recv(1024).decode())

while True:
    data = connect_obj.recv(1024).decode()
    print(data)
    if data=="bye":
        break

connect_obj.close()