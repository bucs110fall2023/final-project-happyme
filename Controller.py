import pygame 
from View import View
from Player import Player

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600,350, 50)
        
    def mainloop(self):
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False   
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.updatePos( 1)  
                        print("Left key pressed")  
                    elif event.key == pygame.K_RIGHT:
                        self.player.updatePos( 2)   
                        print("Right key pressed")   
                    elif event.key == pygame.K_UP:
                        self.player.updatePos( 3)  
                        print("Up key pressed")  
                    elif event.key == pygame.K_DOWN:
                        self.player.updatePos( 4)    
                        print("Down key pressed")
                        
            self.view.drawScreen(self.player)     
            
        pygame.quit()    
        
    def run_controller():
        controller = Controller()
        controller.mainloop()