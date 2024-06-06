import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed=-8, screen_height=600):
        """
        Initialize a laser sprite.

        Args:
            pos (tuple): The starting position of the laser.
            speed (int, optional): The speed at which the laser moves. Default is -8.
            screen_height (int, optional): The height of the screen. Default is 600.
        """
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.height_y_constraint = screen_height
    
    def destroy(self):
        """
        Destroy the laser if it moves out of the screen bounds.
        """
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        """
        Update the laser's position and check if it should be destroyed.
        """
        self.rect.y += self.speed
        self.destroy()
