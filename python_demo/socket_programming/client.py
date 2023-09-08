from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 8088))
print("connection established")
data = client.recv(1024)
print(data.decode())
#
# client.send(bytes("client: connection acknowledged", "utf-8"))

while True:
    input_var = input("enter msg")
    if input_var != "bye":
        client.send(bytes(input_var, "utf-8"))
    else:
        client.send(bytes(input_var, "utf-8"))
        break

client.close()