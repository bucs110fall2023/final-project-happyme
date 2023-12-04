import pygame 
from View import View
from Model import Player, Timer, fishTank, button

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600,350, 30, 300)
        self.timer = Timer()
        self.fishTank1 = fishTank("cadetblue1", 0, 0, 100)
        self.startButton = button(400, 350, 150, 300, "START", "paleturquoise3") #create button
        
    def mainloop(self):
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False   
                elif event.type == pygame.KEYDOWN:
                    dt = self.timer.get_dt()
                    if event.key == pygame.K_LEFT:
                        self.player.updatePos(1, dt)  
                    elif event.key == pygame.K_RIGHT:
                        self.player.updatePos(2, dt)
                         
                    elif event.key == pygame.K_UP:
                        self.player.updatePos( 3, dt)  
                        self.view.drawGameScreen(self.player) 
                    elif event.key == pygame.K_DOWN:
                        self.player.updatePos( 4, dt)    
                        self.view.drawGameScreen(self.player) 
                self.view.drawGameScreen(self.player)      

        pygame.quit()    

                        
                