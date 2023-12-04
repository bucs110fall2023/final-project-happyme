import pygame

class View: 
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        #self.popUp = pygame.display.set_mode((500,500))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.font = pygame.font.SysFont("cambria", 200)
        self.gameTitle = self.font.render("AQUARIUM", True, "WHITE")
        
    def drawPopUp(self):
        self.screen.fill("cornsilk1") 
        pygame.display.flip()
    
    def drawMenuScreen (self, startButtonColor, startBpoints, startBmessage):    
        self.screen.fill("cadetblue3") 
        pygame.display.set_caption('acquarium start menu') 
        pygame.draw.polygon(self.screen, startButtonColor, startBpoints) #draw start button
        self.screen.blit(startBmessage, (self.width / 3, self.height/2)) #display name of start button
        self.screen.blit(self.gameTitle, (self.width / 90, self.height/10)) #draw title
        pygame.display.flip()
    
    def drawGameScreen(self, player, fishtankColor, tank1P, tank2P, tank3P, tank4P, tank5P, tank6P):
       self.screen.fill("seashell1") 
       pygame.display.set_caption('aquarium game')
       pygame.draw.polygon(self.screen, fishtankColor, tank1P) 
       pygame.draw.polygon(self.screen, fishtankColor, tank2P)
       pygame.draw.polygon(self.screen, fishtankColor, tank3P)
       pygame.draw.polygon(self.screen, fishtankColor, tank4P)
       pygame.draw.polygon(self.screen, fishtankColor, tank5P)
       pygame.draw.polygon(self.screen, fishtankColor, tank6P)
       pygame.draw.circle(self.screen, player.color, (player.x, player.y) , player.radius)
       pygame.display.flip()
    

        
        
    
        
        
