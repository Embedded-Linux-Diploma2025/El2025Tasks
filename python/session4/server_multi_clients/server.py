import threading
import socket
import time

SENT_MESSAGE = "Hello Client! your message received"

def Handle_client_request(client_socket):
    while True:
        received_message = client_socket.recv(1024) # Receive data from the client (Asynchronous)
        if not received_message:
            break
        print(f"Received message: {received_message.decode('utf-8')}")
        client_socket.send(SENT_MESSAGE.encode('utf-8')) # Send a responce message to the client (Asynchronous)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP v4 socket
    server.bind(('localhost', 12345)) # Bind the socket to the local host and port 12345
    server.listen(5) # Listen for incoming 5 connections
    print("Server is listening on port 12345...")
    while True:
        client_sock, client_address = server.accept() # Accept a connection from a client (socket, address)
        print(f"Connection from {client_address} has been established.")
        new_client_thread = threading.Thread(target = Handle_client_request, args = (client_sock,))
        new_client_thread.start()


if __name__ == "__main__":
    start_server()
