import pygame 

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        """
        Initialize an alien sprite.

        Args:
            color (str): The color of the alien (determines its image and value).
            x (int): The x-coordinate of the alien's position.
            y (int): The y-coordinate of the alien's position.
        """
        super().__init__()
        file_path = 'graphics\\' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y)) 

        if color == 'red':
            self.value = 100
        elif color == 'green':
            self.value = 200
        else:
            self.value = 300
    
    def update(self, direction):
        """
        Update the alien's position based on the direction.

        Args:
            direction (int): The direction in which the alien moves.
        """
        self.rect.x += direction

class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        """
        Initialize an extra alien sprite.

        Args:
            side (str): The side from which the extra alien appears ('left' or 'right').
            screen_width (int): The width of the screen.
        """
        super().__init__()
        self.image = pygame.image.load('graphics\\extra.png').convert_alpha()
        
        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3
        
        self.rect = self.image.get_rect(topleft=(x, 80))

    def update(self):
        """
        Update the extra alien's position based on its speed.
        """
        self.rect.x += self.speed
