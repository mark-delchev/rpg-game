import pygame

class Player:
    def __init__(self):
        self.health = 100

    def draw_player(self, screen):
        background_color = (255, 255, 255)  # White background color
        stick_color = (0, 0, 0)  # Black stick color
        head_color = (255, 0, 0)  # Red head color
        head_size = 60  # Adjust the size of the square head
        head_position = (screen.get_width() // 2 - head_size // 2, screen.get_height() // 2 - head_size // 2)  # Position the head in the center of the screen
        # Clear the screen with the background color
        screen.fill(background_color)
        points = [(0, 500), (290, 300), (600, 400)]
        pygame.draw.polygon(screen, (255, 255, 0), points)