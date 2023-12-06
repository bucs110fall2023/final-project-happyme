import pygame

class View: 
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
       
    def drawMenuScreen (self, startButtonColor, startBpoints, startBmessage, text):    
        self.screen.fill("cadetblue3") 
        pygame.display.set_caption('aquarium start menu') 
        pygame.draw.polygon(self.screen, startButtonColor, startBpoints) #draw start button
        self.screen.blit(startBmessage, (self.width / 3, self.height/2)) #display name of start button
        self.screen.blit(text, (self.width / 90, self.height/10)) #draw title
        pygame.display.flip()
    
    def drawGameScreen(self, playerImage, playerPos, spriteImage, tank1Rect, tank2Rect, tank3Rect , tank4Rect, tank5Rect, tank6Rect):
       
       self.screen.fill("seashell1") 
       pygame.display.set_caption('aquarium game')
       
       self.screen.blit(spriteImage, tank1Rect)
       #pygame.draw.rect(self.screen, "RED",tank1Rect, 1 )
       self.screen.blit(spriteImage, tank2Rect)
       #pygame.draw.rect(self.screen, "ORANGE",tank2Rect, 1 )
       self.screen.blit(spriteImage, tank3Rect)
       #pygame.draw.rect(self.screen, "YELLOW",tank3Rect, 1 )
       self.screen.blit(spriteImage, tank4Rect)
       #pygame.draw.rect(self.screen, "GREEN",tank4Rect, 1 )
       self.screen.blit(spriteImage, tank5Rect)
       #pygame.draw.rect(self.screen, "BLUE",tank5Rect, 1 )
       self.screen.blit(spriteImage, tank6Rect)
       #pygame.draw.rect(self.screen, "PURPLE",tank6Rect, 1 )

       self.screen.blit(playerImage , playerPos) #draw player
       #pygame.draw.rect(self.screen, "BLACK",playerPos, 1 )
       pygame.display.flip()
       
    def drawPopupScreen(self,startBpoints, image, name, fact1, fact2, fact3 ):
        pygame.draw.polygon(self.screen, "cornflowerblue", startBpoints) #draw rectangle
        self.screen.blit(image, (250, 300))#draw image
        self.screen.blit(name, (250, 220))#draw name of exhibit
        self.screen.blit(fact1, (400, 300))#draw fact1
        self.screen.blit(fact2, (400, 400))#draw fact2
        self.screen.blit(fact3, (400, 500))#draw fact3
        pygame.display.flip()
        
    def drawEndMessage(self, text):
        self.screen.fill("cadetblue3")
        pygame.display.set_caption('end screen') 
        self.screen.blit(text, (self.width / 90, self.height/10)) #draw title
        pygame.display.flip()
        