import pygame 
from View import View
from Model import Player, Timer, FishTank, Button

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600,350, 30, 300)
        self.timer = Timer()
        
        self.fishTank1 = FishTank( 50, 0, 300, 100)
        self.fishTank2 = FishTank( 450, 0, 300, 100)
        self.fishTank3 = FishTank( 850, 0, 300, 100)
        self.fishTank4 = FishTank( 50, 600, 300, 100)
        self.fishTank5 = FishTank( 450, 600, 300, 100)
        self.fishTank6 = FishTank( 850, 600, 300, 100)
        
        self.startButton = Button(400, 350, 100, 300, "START", "cornflowerblue", 100) 
    
        
    def mainloop(self):
        running = True
        gameStart = False
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False   
                elif event.type == pygame.KEYDOWN:
                    #self.timer.updateDT()
                    dt = self.timer.get_dt()
                    if event.key == pygame.K_LEFT:
                        self.player.updatePos(1, dt)  
                        self.view.drawScreen(self.player) 
                        print("Left key pressed")  
                        print (dt)
                    elif event.key == pygame.K_RIGHT:
                        self.player.updatePos( 2, dt)   
                        print("Right key pressed")   
                    elif event.key == pygame.K_UP:
                        self.player.updatePos( 3, dt)  
                        print("Up key pressed")  
                    elif event.key == pygame.K_DOWN:
                        self.player.updatePos( 4, dt)    
                        print("Down key pressed")
          
                self.view.drawScreen(self.player)     
                pygame.display.flip() 
            
        pygame.quit()    