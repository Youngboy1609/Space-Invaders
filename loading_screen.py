from main import *
import pygame
import threading
import sys

class Button:
    """
    Class to create and manage button objects in the game.

    Attributes:
        rect (pygame.Rect): The rectangle representing the button's position and size.
        image (pygame.Surface): The scaled image of the button.
    """
    def __init__(self, x, y, image, scale):
        """
        Initializes a Button object with position, image, and scale.

        Args:
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            image (pygame.Surface): The image to be used for the button.
            scale (float): The scaling factor for the button's image.
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        """
        Draws the button on the screen.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def clicked(self, pos):
        """
        Checks if the button was clicked based on the mouse position.

        Args:
            pos (tuple): The (x, y) coordinates of the mouse click.

        Returns:
            bool: True if the button was clicked, False otherwise.
        """
        return self.rect.collidepoint(pos)

class Background:
    """
    Class to manage the background loading process and display in the game.

    Attributes:
        loading_finished (bool): Flag indicating if loading is finished.
        loading_progress (int): Counter for loading progress.
        WORK (int): Total amount of work to simulate loading.
    """
    def __init__(self):
        """
        Initializes the Background object.
        """
        self.loading_finished = False
        self.loading_progress = 0
        self.WORK = 30000000

    def doWork(self):
        """
        Simulates a long computational task to update loading progress.
        """
        for i in range(self.WORK):
            math_equation = 523687 / 789456 * 89456
            self.loading_progress = i
        self.loading_finished = True
    
    def play_background(self):
        """
        Handles the background loading screen and plays background music.
        """
        FONT = pygame.font.SysFont("Roboto", 100)
        CLOCK = pygame.time.Clock()
        
        # Loading BG
        LOADING_BG = pygame.image.load("graphics/Loading Bar Background.png")
        LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))
    
        # Loading Bar and variables
        loading_bar = pygame.image.load("graphics/Loading Bar.png")
        loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
        loading_bar_width = 8
        
        # Finished text
        finished_image = pygame.image.load("graphics/Playing Bar.png").convert_alpha()
        finished_rect = Button(390, 240, finished_image, 0.6666)
    
        # Thread
        threading.Thread(target=self.doWork).start()
    
        running = True

        # Music
        pygame.mixer.music.load('audio\\cyberpunk.mp3')
        pygame.mixer.music.play(-1)
        
        # Game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.loading_finished and finished_rect.clicked(event.pos):
                        pygame.mixer.music.load('audio\\nolimits.mp3')
                        pygame.mixer.music.play(-1)
                        running = False  # Stop the loading screen loop
                        
    
            screen.fill("#0d0e2e")
        
            if not self.loading_finished:
                loading_bar_width = self.loading_progress / self.WORK * 720
                loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
                loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
                screen.blit(LOADING_BG, LOADING_BG_RECT)
                screen.blit(loading_bar, loading_bar_rect)
            else:
                finished_rect.draw()
            
            pygame.display.update()
            CLOCK.tick(60)
