import pygame 
from View import View
from Model import Player, Timer

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600,350, 30, 300)
        self.timer = Timer()
        
    def mainloop(self):
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False   
                elif event.type == pygame.KEYDOWN:
                    #self.timer.updateDT()
                    dt = self.timer.get_dt()
                    if event.key == pygame.K_LEFT:
                        self.player.updatePos( 1, dt)  
                        self.view.drawScreen(self.player) 
                        print("Left key pressed")  
                        print(self.player.x) 
                        print(self.player.y)
                    elif event.key == pygame.K_RIGHT:
                        self.player.updatePos( 2, dt)  
                        self.view.drawScreen(self.player) 
                        print("Right key pressed")   
                        print(self.player.x) 
                        print(self.player.y)
                    elif event.key == pygame.K_UP:
                        self.player.updatePos( 3, dt)  
                        self.view.drawScreen(self.player)
                        print(self.player.x) 
                        print(self.player.y)
                        print("Up key pressed")  
                    elif event.key == pygame.K_DOWN:
                        self.player.updatePos( 4, dt)  
                        self.view.drawScreen(self.player)  
                        print("Down key pressed")
                        print(self.player.x) 
                        print(self.player.y)
          
                self.view.drawScreen(self.player)      
            
        pygame.quit()    
