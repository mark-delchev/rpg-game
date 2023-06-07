import pygame
import sys
from player import *

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RPG")

# Create player
player_a = Player()

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the game display
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS
        player_a.draw_player(screen)

# Run the game
def run_game():
    game_loop()
    pygame.quit()
    sys.exit()

# Entry point of the program
if __name__ == "__main__":
    run_game()