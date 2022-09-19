from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024
PORT = 5000
HOST = "192.168.95.255"

def chatClient():
    username = input("Inserisci username: ")
    username = username.encode('utf8')
    while True:
        with socket(AF_INET, SOCK_DGRAM) as s:
            s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            msg = input("Inserisci un messaggio da inviare: ")
            msg = msg.encode('uft8')
            s.sendto(username, (HOST, PORT))
            s.sendto(msg, (HOST, PORT))
            print(f'Messaggio inviato in broadcast, su IP: {HOST}, {PORT}.\n')
        
if __name__ == "__main__":
    chatClient()