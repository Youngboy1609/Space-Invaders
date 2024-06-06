import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        """
        Initialize a block sprite.

        Args:
            size (int): The size of the block (both width and height).
            color (tuple): The color of the block in RGB format.
            x (int): The x-coordinate of the block's position.
            y (int): The y-coordinate of the block's position.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

shape = [
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',   
'xxxxxxxxxxx',   
'xxx     xxx',
'xx       xx']
