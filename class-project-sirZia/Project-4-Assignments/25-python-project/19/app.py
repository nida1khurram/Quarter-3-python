import pygame
import random

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Game constants
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # J
    [[1, 1, 1], [0, 0, 1]],  # L
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Colors for shapes
SHAPE_COLORS = [CYAN, YELLOW, PURPLE, BLUE, ORANGE, GREEN, RED]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Tetris")

clock = pygame.time.Clock()

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
    
    def new_piece(self):
        shape = random.choice(SHAPES)
        color = SHAPE_COLORS[SHAPES.index(shape)]
        return {
            'shape': shape,
            'color': color,
            'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
            'y': 0
        }
    
    def valid_move(self, piece, x_offset=0, y_offset=0):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece['x'] + x + x_offset
                    new_y = piece['y'] + y + y_offset
                    if (new_x < 0 or new_x >= GRID_WIDTH or 
                        new_y >= GRID_HEIGHT or 
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True
    
    def lock_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = self.current_piece['color']
        
        # Check for completed lines
        self.clear_lines()
        
        # Get new piece
        self.current_piece = self.new_piece()
        
        # Game over if new piece is invalid
        if not self.valid_move(self.current_piece):
            self.game_over = True
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_cleared += 1
                # Move all lines above down
                for y2 in range(y, 0, -1):
                    self.grid[y2] = self.grid[y2-1][:]
                self.grid[0] = [0 for _ in range(GRID_WIDTH)]
        
        # Update score
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
    
    def rotate_piece(self):
        # Transpose and reverse rows to rotate 90 degrees
        rotated = [list(row) for row in zip(*self.current_piece['shape'][::-1])]
        old_shape = self.current_piece['shape']
        self.current_piece['shape'] = rotated
        if not self.valid_move(self.current_piece):
            self.current_piece['shape'] = old_shape
    
    def draw(self):
        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(screen, WHITE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
                if self.grid[y][x]:
                    pygame.draw.rect(screen, self.grid[y][x], (x*BLOCK_SIZE+1, y*BLOCK_SIZE+1, BLOCK_SIZE-2, BLOCK_SIZE-2))
        
        # Draw current piece
        if not self.game_over:
            for y, row in enumerate(self.current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, self.current_piece['color'], 
                                       ((self.current_piece['x']+x)*BLOCK_SIZE+1, 
                                        (self.current_piece['y']+y)*BLOCK_SIZE+1, 
                                        BLOCK_SIZE-2, BLOCK_SIZE-2))
        
        # Draw score
        font = pygame.font.SysFont('Arial', 20)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (BLOCK_SIZE*GRID_WIDTH + 10, 20))
        
        if self.game_over:
            font = pygame.font.SysFont('Arial', 30)
            game_over_text = font.render("GAME OVER!", True, RED)
            screen.blit(game_over_text, (BLOCK_SIZE*GRID_WIDTH//2 - 80, BLOCK_SIZE*GRID_HEIGHT//2 - 15))

def main():
    game = Tetris()
    fall_time = 0
    fall_speed = 0.5  # seconds
    
    while True:
        # Reset screen
        screen.fill(BLACK)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if not game.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and game.valid_move(game.current_piece, -1):
                        game.current_piece['x'] -= 1
                    if event.key == pygame.K_RIGHT and game.valid_move(game.current_piece, 1):
                        game.current_piece['x'] += 1
                    if event.key == pygame.K_DOWN and game.valid_move(game.current_piece, 0, 1):
                        game.current_piece['y'] += 1
                    if event.key == pygame.K_UP:
                        game.rotate_piece()
                    if event.key == pygame.K_SPACE:  # Hard drop
                        while game.valid_move(game.current_piece, 0, 1):
                            game.current_piece['y'] += 1
                        game.lock_piece()
        
        # Automatic falling
        if not game.game_over:
            current_time = pygame.time.get_ticks() / 1000
            if current_time - fall_time > fall_speed:
                if game.valid_move(game.current_piece, 0, 1):
                    game.current_piece['y'] += 1
                else:
                    game.lock_piece()
                fall_time = current_time
        
        # Draw everything
        game.draw()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()