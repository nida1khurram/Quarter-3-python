# import socket
# import json
# import pygame
# import threading

# # Game constants
# WIDTH, HEIGHT = 800, 600
# PLAYER_SIZE = 50

# class GameClient:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("Online Multiplayer Game")
#         self.clock = pygame.time.Clock()
        
#         self.host = input("Enter server IP: ") or "localhost"
#         self.port = 5555
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
#         self.player_id = None
#         self.players = {}
#         self.my_pos = {"x": 100, "y": 100, "color": (0, 0, 255)}
        
#     def connect(self):
#         try:
#             self.client.connect((self.host, self.port))
#             # First message is our player ID
#             self.player_id = int(self.client.recv(2048).decode('utf-8'))
#             print(f"Connected as player {self.player_id}")
            
#             # Start network thread
#             thread = threading.Thread(target=self.receive_data)
#             thread.daemon = True
#             thread.start()
            
#             self.run_game()
#         except Exception as e:
#             print(f"Connection error: {e}")
#         finally:
#             self.client.close()
    
#     def receive_data(self):
#         while True:
#             try:
#                 data = self.client.recv(2048).decode('utf-8')
#                 if data:
#                     self.players = json.loads(data)
#             except:
#                 print("Disconnected from server")
#                 break
    
#     def send_data(self):
#         try:
#             self.client.sendall(json.dumps(self.my_pos).encode('utf-8'))
#         except:
#             print("Failed to send data")
    
#     def run_game(self):
#         running = True
#         while running:
#             self.clock.tick(60)
            
#             # Handle input
#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_LEFT]:
#                 self.my_pos["x"] -= 5
#             if keys[pygame.K_RIGHT]:
#                 self.my_pos["x"] += 5
#             if keys[pygame.K_UP]:
#                 self.my_pos["y"] -= 5
#             if keys[pygame.K_DOWN]:
#                 self.my_pos["y"] += 5
            
#             # Send updated position
#             self.send_data()
            
#             # Handle events
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
            
#             # Draw everything
#             self.screen.fill((0, 0, 0))
            
#             # Draw other players
#             for pid, player in self.players.items():
#                 if pid != self.player_id:
#                     pygame.draw.rect(self.screen, player["color"], 
#                                    (player["x"], player["y"], PLAYER_SIZE, PLAYER_SIZE))
            
#             # Draw current player
#             pygame.draw.rect(self.screen, self.my_pos["color"], 
#                            (self.my_pos["x"], self.my_pos["y"], PLAYER_SIZE, PLAYER_SIZE))
            
#             pygame.display.flip()
        
#         pygame.quit()

# if __name__ == "__main__":
#     client = GameClient()
#     client.connect()
import socket
import pygame

# Game configuration
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Multiplayer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle and Ball
player1_rect = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_rect = pygame.Rect(WIDTH - 50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball_rect = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed = [5, 5]

# Socket configuration
SERVER = 'localhost'
PORT = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def game_loop():
    try:
        client_socket.connect((SERVER, PORT))
        print("Connected to server")

        # Game loop
        player1_y, player2_y = HEIGHT//2 - PADDLE_HEIGHT//2, HEIGHT//2 - PADDLE_HEIGHT//2
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    client_socket.close()
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player1_rect.top > 0:
                player1_rect.y -= 5
            if keys[pygame.K_s] and player1_rect.bottom < HEIGHT:
                player1_rect.y += 5

            if keys[pygame.K_UP] and player2_rect.top > 0:
                player2_rect.y -= 5
            if keys[pygame.K_DOWN] and player2_rect.bottom < HEIGHT:
                player2_rect.y += 5

            # Send player positions to server
            try:
                client_socket.sendall(str(player1_rect.y).encode())
                client_socket.sendall(str(player2_rect.y).encode())
            except Exception as e:
                print(f"Error sending data to server: {e}")
                break

            # Receive updated positions from server
            try:
                player1_y = int(client_socket.recv(1024).decode())
                player2_y = int(client_socket.recv(1024).decode())
            except Exception as e:
                print(f"Error receiving data from server: {e}")
                break

            # Move the ball
            ball_rect.x += ball_speed[0]
            ball_rect.y += ball_speed[1]

            if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
                ball_speed[1] = -ball_speed[1]

            if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
                ball_speed[0] = -ball_speed[0]

            if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
                ball_rect.center = (WIDTH//2, HEIGHT//2)
                ball_speed[0] = -ball_speed[0]

            # Draw everything
            screen.fill(BLACK)
            pygame.draw.rect(screen, WHITE, player1_rect)
            pygame.draw.rect(screen, WHITE, player2_rect)
            pygame.draw.ellipse(screen, WHITE, ball_rect)

            pygame.display.flip()
            clock.tick(FPS)

    except Exception as e:
        print(f"Error in game loop: {e}")
        client_socket.close()
        pygame.quit()

if __name__ == "__main__":
    game_loop()