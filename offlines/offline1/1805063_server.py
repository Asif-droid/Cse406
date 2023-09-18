import socket
import struct as st
import crypt_1805063 as crypt
import key_xchange_1805063 as xchanger
import time

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to bind the socket to
host = '127.0.0.1'  # Localhost
port = 12345


# prime base
p=xchanger.get_prime()
g=xchanger.calculate_primitive_root(p,2,p)
if(g==None):
    print("no primitive root found")
    exit()
# private key
a=6832892905590973747
public_x=xchanger.create_public_key(a,g,p)

key_bytes = public_x.to_bytes((public_x.bit_length() + 7) // 8, 'big')

prime_bytes = p.to_bytes((p.bit_length() + 7) // 8, 'big')
g_bytes = g.to_bytes((g.bit_length() + 7) // 8, 'big')
# Generate the key pairs
# key="Thats my Kung15234"

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on {}:{}".format(host, port))

# Accept a client connection
client_socket, addr = server_socket.accept()
print("Connected to client:", addr)


# message = "Hello, client!"
# client_socket.send(message.encode())

# Send key to the client

# encrypted_message = crypt.encrypt(public_x, key)

client_socket.send(prime_bytes)
client_socket.send(g_bytes)

confirmation = client_socket.recv(1024).decode()
print("Received from client:", confirmation)

client_socket.send(key_bytes)

number_bytes = client_socket.recv(1024)

# Convert the bytes back to an integer (using little-endian format)
public_y = int.from_bytes(number_bytes, 'big')

# Receive key from the client
# public_y = client_socket.recv(1024)
print("Received from client:", public_y)

# gen private key
shared_key=xchanger.construct_shared_key(public_y,a,p)
print("shared key:", shared_key)

key=shared_key
crypt.get_all_keys(key)





lines=list()
with open("input_1805063.txt", "r") as f:
    lines = f.readlines()

# print(type(lines))
# print(lines[0])


for line in lines: 
    for i in range(0,len(line),16):
        msg=line[i:i+16]
        start_time = time.time()
        encrypted_message = crypt.encrypt(msg, key)
        end_time = time.time()
        print("encryption time:", end_time-start_time)
        client_socket.send(encrypted_message.encode())

# Receive data from the client
data = client_socket.recv(1024).decode()
print("Received from client:", data)

# Close the connection
client_socket.close()
server_socket.close()
