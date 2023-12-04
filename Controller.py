import pygame 
from View import View
from Model import Player, Timer, fishTank, button

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600,350, 30, 300)
        self.timer = Timer()
        self.fishTank1 = fishTank("cadetblue1", 0, 0, 100)
        self.startButton = button(400, 350, 100, 300, "START", "cornflowerblue", 100) 
    
        
    def mainloop(self):
        running = True
        gameStart = False
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False   
                if gameStart != True:
                    self.view.drawMenuScreen (self.startButton.color, self.startButton.getPoints(), self.startButton.message)
                #Detect mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    #mouse is clicking on start button
                    if self.startButton.checkForInput(mousePos):
                        gameStart = True
                        if event.type == pygame.KEYDOWN:
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

                        
                