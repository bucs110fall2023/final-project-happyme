import pygame 
from src.View import View
from src.Model import Player, Timer, FishTank, Button, InfoBox

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600, 300, 200, .25) #movable character
        self.timer = Timer()
        self.gameStarted = False
        self.gameComplete = False
        self.tanks_viewed= []
        self.tankCounter = 6
        
        #sprite group of fishtanks
        self.fishTanks = pygame.sprite.Group()
       
        self.fishTank1 = FishTank(0, 0, 1)
        self.fishTank2 = FishTank(400, 0, 1)  
        self.fishTank3 = FishTank(800, 0, 1)   
        self.fishTank4 = FishTank(0, 600, 1)  
        self.fishTank5 = FishTank(400, 600, 1)  
        self.fishTank6 = FishTank(800, 600, 1)    
        self.fishTanks.add(self.fishTank1, self.fishTank2, self.fishTank3, self.fishTank4, self.fishTank5, self.fishTank6)
        
        #startbutton for menu screen
        self.startButton = Button(400, 350, 100, 300, "START", "cornflowerblue", 100) 
    
        self.t1Info = InfoBox( "Guppy", "-tropical fish", "-popular freshwater species", "-name comes from Robert John Lechmere Guppy", "assets/guppy.jpg")
        
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
                        #for i in  pygame.sprite.spritecollide(self.player, self.fishTanks, True):
                        if pygame.sprite.collide_rect(self.player, self.fishTank1):
                            self.view.drawPopupScreen(self.t1Info.points, self.t1Info.image, self.t1Info.name, self.t1Info.fact1, self.t1Info.fact2, self.t1Info.fact3)
                            
                        #for tank in self.tanks_viewed:
                            #self.tankCounter -= 1
                            #if self.tankCounter == 0:
                                #print ("You have completed the game!")
                    
        pygame.quit()    
        
