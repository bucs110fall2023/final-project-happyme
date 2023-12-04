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
    
   
        
