import pygame 
from src.View import View
from src.Model import Player, Timer, FishTank, Button

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(100, 150, 200, .25) #movable character
        self.timer = Timer()
        self.gameStarted = False
        self.gameComplete = False
        self.tanks_viewed= []
        self.tankCounter = 6
        
        #sprite group of fishtanks
        self.fishTanks = pygame.sprite.Group()
        number_of_fishTanks = 3
        interval = 400
        topRowNotFill = True
        xpos = 0
        #top row of fishtanks
        for i in range(0, number_of_fishTanks):
            new_fishTank = FishTank(xpos, 0, 1)
            xpos += interval    
            self.fishTanks.add(new_fishTank)
        
        x2pos = 0
        #bottom row of fishtanks
        for i in range(0, number_of_fishTanks):
            new_fishTank = FishTank(x2pos, 500, 1)
            x2pos += interval    
            self.fishTanks.add(new_fishTank)
        
        #startbutton for menu screen
        self.startButton = Button(400, 350, 100, 300, "START", "cornflowerblue", 100) 
    
        
    def mainloop(self):
        running = True
        gameStart = False
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False   
                #default display start menu 
                if gameStart != True:
                    self.view.drawMenuScreen (self.startButton.color, self.startButton.getPoints(), self.startButton.message)
                #Detect mouse click
                if event.type == pygame.MOUSEBUTTONDOWN or gameStart == True:
                    mousePos = pygame.mouse.get_pos()
                    
                    #mouse clicks or has clicked the start button
                    if self.startButton.checkForInput(mousePos):
                        gameStart = True
                        #detects keyboard input and moves character accordingly
                        if event.type == pygame.KEYDOWN:
                            dt = self.timer.get_dt()
                            if event.key == pygame.K_LEFT:
                                self.player.updatePos(1, dt)  
                            elif event.key == pygame.K_RIGHT:
                                self.player.updatePos(2, dt)
                            elif event.key == pygame.K_UP:
                                self.player.updatePos( 3, dt)  
                                
                            elif event.key == pygame.K_DOWN:
                                self.player.updatePos( 4, dt)     
                        #display game screen 
                        self.view.drawGameScreen(self.player.getImg(), self.player.getRect(), self.fishTanks )
                        
                        #if player collides with any tank
                        #self.tanks_viewed = pygame.sprite.spritecollide(self.player, self.fishTanks, True)
                        for i in  pygame.sprite.spritecollide(self.player, self.fishTanks, True):
                            self.tankCounter -= 1
                            print ("display exhibit") 
                            print (i)
                            if self.tankCounter == 0:
                                print ("You have completed the game!")
                        
                        #for tank in self.tanks_viewed:
                            #self.tankCounter -= 1
                            #if self.tankCounter == 0:
                                #print ("You have completed the game!")
                            
                            
                            
                        
                            
                        
                            
        pygame.quit()    
        
