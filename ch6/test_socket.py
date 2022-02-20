import socket
import json

count = 10
count = count + 1
testJson = {"counter": count}

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
sock.connect(("akshaydandekar.in", 8001))

sock.send(json.dumps(testJson).encode("utf-8"))
# sock.send(b'\x00\x01\x02')

rcvd = sock.recv(100)
pyDict = json.loads(rcvd.decode("utf-8"))

print(pyDict)
print(pyDict["status"])


sock.close()
