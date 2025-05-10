import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [[100, 100]]  # Starting position
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0][:]
        if self.direction == "UP":
            head[1] -= GRID_SIZE
        elif self.direction == "DOWN":
            head[1] += GRID_SIZE
        elif self.direction == "LEFT":
            head[0] -= GRID_SIZE
        elif self.direction == "RIGHT":
            head[0] += GRID_SIZE
        
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])  # Increase length

    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True  # Hit the wall
        
        if self.body[0] in self.body[1:]:  
            return True  # Hit itself

        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE)]

    def spawn(self):
        self.position = [random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE)]

    def draw(self):
        pygame.draw.rect(win, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    running = True
    while running:
        win.fill(BLACK)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != "DOWN":
            snake.direction = "UP"
        if keys[pygame.K_DOWN] and snake.direction != "UP":
            snake.direction = "DOWN"
        if keys[pygame.K_LEFT] and snake.direction != "RIGHT":
            snake.direction = "LEFT"
        if keys[pygame.K_RIGHT] and snake.direction != "LEFT":
            snake.direction = "RIGHT"

        # Move snake
        snake.move()

        # Check collision with food
        if snake.body[0] == food.position:
            snake.grow()
            food.spawn()

        # Check collision with wall or itself
        if snake.check_collision():
            print("Game Over!")
            running = False

        # Draw elements
        snake.draw()
        food.draw()
        
        pygame.display.update()
        clock.tick(10)  # Speed of the game

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game_loop()