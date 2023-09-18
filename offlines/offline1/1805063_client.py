import socket
import struct as st
import crypt_1805063 as crypt
import key_xchange_1805063 as xchanger
import time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 12345

# private key
b=3367587046284275663





# Generate the key pairs
# key="Thats my Kung152"


# Connect to the server
client_socket.connect((server_ip, server_port))

# Receive key from the server

prime_bytes = client_socket.recv(1024)
prime=int.from_bytes(prime_bytes, 'big')

base_bytes = client_socket.recv(1024)
base=int.from_bytes(base_bytes, 'big')
confimation="ok"
client_socket.send(confimation.encode())


public_y=xchanger.create_public_key(b,base,prime)

key_bytes = public_y.to_bytes((public_y.bit_length() + 7) // 8, 'big')

number_bytes = client_socket.recv(1024)

# Convert the bytes back to an integer (using little-endian format)
public_x = int.from_bytes(number_bytes, 'big')
# public_x = client_socket.recv(1024) 
print("Received from server:", public_x)



client_socket.send(key_bytes)

# gen private key
shared_key=xchanger.construct_shared_key(public_x,b,prime)
print("shared key:", shared_key)

key=shared_key
crypt.get_all_keys(key)

# Receive data from the server

f = open("output_1805063.txt", "a")
f.write("New massage starts from here !\n")

final_massage=""
while(True):
    data = client_socket.recv(1024).decode()
    start_time = time.time()
    massage=crypt.decrypt(data, key) 
    end_time = time.time()
    print("Time taken to decrypt:", end_time - start_time)
    final_massage+=massage
    # print("Received from server:", massage)
    if('#' in massage):
        final_massage+="\n"
    #     # break
    if('$$' in massage):
        # print("Received from server:", final_massage)
        f.write(final_massage)
        break

# Send data to the server
message = "Bye, server!"
client_socket.send(message.encode())

# Close the connection
client_socket.close()
