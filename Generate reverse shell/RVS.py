import base64
import json
import argparse


f = open("revershell.json","r")
data = json.load(f)
f.close()


# parse user input
parser = argparse.ArgumentParser(description='Reverse Shell Generator')
parser.add_argument('-i', '--ip', help='IP address of the listener', required=True)
parser.add_argument('-p', '--port', help='Port number of the listener', required=True)
parser.add_argument('-t', '--type', help='Type of the listener', required=True)
parser.add_argument('-e', '--encode', help='List all available payloads', required=False, default=False)
args = parser.parse_args()

ip = args.ip
port = args.port
type = args.type
encode = args.encode

# check if the type is valid
if type not in data:
    print("Type not supported yet!")
    exit(1)

# check if the port is valid
if not port.isdigit():
    print("Port must be a number!")
    exit(1)

# check if the port is in range
if int(port) < 1 or int(port) > 65535:
    print("Port must be in range 1-65535!")
    exit(1)

# check if the ip is valid
if not ip.replace('.','').isdigit():
    print("IP address must be in the correct format!")
    exit(1)

# check if the ip is in range
for i in ip.split('.'):
    if int(i) < 0 or int(i) > 255:
        print("IP address must be in the correct format!")
        exit(1)

print("\n\n")
# generate the payload
for i in range(len(data[type])):
    payload = base64.b64decode(data[type][i]).decode("utf-8").replace("$host$",ip).replace("$port$",port)
    if encode:
        print("Payload %d:\n%s\n\n========================================\n\n"%((i+1),base64.b64encode(payload.encode()).decode()))
    else:
        print("Payload %d:\n%s\n\n========================================\n\n"%((i+1),payload))
