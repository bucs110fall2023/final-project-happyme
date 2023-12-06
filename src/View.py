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
        pygame.display.set_caption('aquarium start menu') 
        pygame.draw.polygon(self.screen, startButtonColor, startBpoints) #draw start button
        self.screen.blit(startBmessage, (self.width / 3, self.height/2)) #display name of start button
        self.screen.blit(self.gameTitle, (self.width / 90, self.height/10)) #draw title
        pygame.display.flip()
    
    def drawGameScreen(self, playerImage, playerPos, spriteGroup ):
       
       self.screen.fill("seashell1") 
       pygame.display.set_caption('aquarium game')
       spriteGroup.draw(self.screen) #draw fish tanks
       self.screen.blit(playerImage , playerPos) #draw player
       pygame.display.flip()
       
    def drawPopupScreen(self,startBpoints, image, name, fact1, fact2, fact3 ):
        pygame.draw.polygon(self.screen, "cornflowerblue", startBpoints) #draw rectangle
        self.screen.blit(image, (250, 300))#draw image
        self.screen.blit(name, (250, 220))#draw name of exhibit
        self.screen.blit(fact1, (400, 300))#draw fact1
        self.screen.blit(fact2, (400, 400))#draw fact2
        self.screen.blit(fact3, (400, 500))#draw fact3
        pygame.display.flip()
        