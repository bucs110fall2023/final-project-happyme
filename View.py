import pygame

class View: 
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.font = pygame.font.SysFont("cambria", 200)
        self.gameTitle = self.font.render("AQUARIUM", True, "WHITE")
    
    def drawMenuScreen (self, startButtonColor, startBpoints, startBmessage):    
        self.screen.fill("cadetblue3") 
        pygame.display.set_caption('acquarium start menu') 
        pygame.draw.polygon(self.screen, startButtonColor, startBpoints) #draw start button
        self.screen.blit(startBmessage, (self.width / 3, self.height/2)) #display name of start button
        self.screen.blit(self.gameTitle, (self.width / 90, self.height/10)) #draw title
        pygame.display.flip()
    
    def drawGameScreen(self, player):
       self.screen.fill("cornsilk3") 
       pygame.display.set_caption('aquarium game')
       pygame.draw.circle(self.screen, player.color, (player.x, player.y) , player.radius)
       pygame.display.flip()
    
    def drawTank(self, fishTankColor, points):
        self.screen.fill((255,255,255)) #White
        pygame.draw.polygon(self.screen, fishTankColor, points)
        
    
        
        
