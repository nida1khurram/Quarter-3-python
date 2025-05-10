# import socket
# import threading
# import json

# class GameServer:
#     def __init__(self):
#         self.host = '0.0.0.0'
#         self.port = 5555
#         self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server.bind((self.host, self.port))
#         self.server.listen()
        
#         self.players = {}
#         self.player_id = 0
        
#     def handle_client(self, conn, addr, player_id):
#         print(f"New connection from {addr} as player {player_id}")
        
#         try:
#             while True:
#                 data = conn.recv(2048).decode('utf-8')
#                 if not data:
#                     break
                
#                 # Update player position
#                 self.players[player_id] = json.loads(data)
                
#                 # Send all players' data back
#                 reply = json.dumps(self.players)
#                 conn.sendall(reply.encode('utf-8'))
                
#         except Exception as e:
#             print(f"Error with player {player_id}: {e}")
#         finally:
#             del self.players[player_id]
#             conn.close()
#             print(f"Player {player_id} disconnected")

#     def run(self):
#         print("Server started. Waiting for connections...")
#         while True:
#             conn, addr = self.server.accept()
#             self.player_id += 1
#             self.players[self.player_id] = {"x": 100, "y": 100, "color": (255, 0, 0)}
            
#             thread = threading.Thread(target=self.handle_client, args=(conn, addr, self.player_id))
#             thread.start()

# if __name__ == "__main__":
#     server = GameServer()
#     server.run()
import socket
import threading

# Server configuration
HOST = 'localhost'
PORT = 5555

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    try:
        # Sending a welcome message to the client
        client_socket.sendall(b"Welcome to Pong!")

        while True:
            try:
                player1_y = client_socket.recv(1024).decode()
                if not player1_y:
                    break
                print(f"Player 1 Y Position: {player1_y}")

                player2_y = client_socket.recv(1024).decode()
                if not player2_y:
                    break
                print(f"Player 2 Y Position: {player2_y}")

                client_socket.sendall(player1_y.encode())
                client_socket.sendall(player2_y.encode())
                
            except Exception as e:
                print(f"Error in communication: {e}")
                break

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    print("Server started, waiting for players...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    start_server()