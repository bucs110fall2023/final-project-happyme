import pygame

class View: 
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption('museum')
    
    def drawScreen(self, player):
        self.screen.fill((255,255,255)) #White
        pygame.draw.circle(self.screen, player.color, (player.x, player.y) , player.radius)
        pygame.display.flip()
    

        
