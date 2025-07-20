import socket
import time
SENT_MESSAGE = "Hello Server, Client 1" # Get user input

def run_client_request():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP v4 socket
    client.connect(('localhost', 12345)) # Connect to the server at localhost on port 12345
    while True:
        client.send(SENT_MESSAGE.encode('utf-8')) # Send the message to the server (Asynchronous)
        response = client.recv(1024) # Receive the response from the server (Asynchronous
        print("Server response: ", response.decode('utf-8')) # Print the response from the server
        time.sleep(5)
        
if __name__ == "__main__":
    run_client_request()      
