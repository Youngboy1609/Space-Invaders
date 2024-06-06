from laser import Laser
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed=8):
        """
        Initialize the player sprite.

        Args:
            pos (tuple): The starting position of the player.
            constraint (int): The maximum x-coordinate the player can move to.
            speed (int, optional): The speed at which the player moves. Default is 8.
        """
        super().__init__()
        self.image = pygame.image.load('graphics\\spaceship.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        
        self.lasers = pygame.sprite.Group()

        self.lasers_sound = pygame.mixer.Sound('audio\\laser.wav')
        self.lasers_sound.set_volume(0.5)
    
    def get_input(self):
        """
        Get player input for movement and shooting.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.lasers_sound.play()

    def recharge(self):
        """
        Handle the laser recharge cooldown.
        """
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):
        """
        Ensure the player stays within the screen bounds.
        """
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
    
    def shoot_laser(self):
        """
        Shoot a laser from the player's current position.
        """
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))

    def update(self):
        """
        Update the player state, handling input, movement constraints, laser recharge, and laser updates.
        """
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
