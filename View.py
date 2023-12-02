import pygame

class View: 
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        pygame.display.set_caption('museum')
    
    def drawScreen(self, player):
        self.screen.fill((255,255,255)) #White
        pygame.draw.circle(self.screen, player.color, player.pos, player.radius)
        pygame.display.flip()
               
        
        