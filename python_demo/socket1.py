from socket import *

# AF_INET = IPV4
# SOCK_STREAM = TCP absed connectivity ---> OSI
s = socket(AF_INET, SOCK_STREAM)

ip = gethostbyname('www.google.com')
print(ip)
# pass google ip and port num
s.connect((ip, 8055))# 0 to 65536
# https://realpython.com/python-sockets/