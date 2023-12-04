import pygame

class View: 
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
    
    def drawMenuScreen (self, startButtonColor, points, message):    
        self.screen.fill("WHITE") 
        pygame.display.set_caption('acquarium start menu')
        self.screen.blit(message, (600, 350))
        pygame.draw.polygon(self.screen, startButtonColor, points)
        pygame.display.flip()
    
    def drawGameScreen(self, player):
        self.screen.fill("cornsilk3") 
        pygame.display.set_caption('aquarium game')
        pygame.draw.circle(self.screen, player.color, (player.x, player.y) , player.radius)
        pygame.display.flip()
    
    def drawTank(self, fishTankColor, points):
        self.screen.fill((255,255,255)) #White
        pygame.draw.polygon(self.screen, fishTankColor, points)
        
    
        
        
