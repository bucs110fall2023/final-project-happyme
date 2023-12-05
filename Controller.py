import pygame 
from View import View
from Model import Player, Timer, FishTank, Button

class Controller:        
    def __init__(self):
        self.view = View()
        self.player = Player(600,350, 300, .25) #movable character
        self.timer = Timer()
        self.gameStarted = False
        self.gameComplete = False
        
        #sprite group of fishtanks
        self.fishTanks = pygame.sprite.Group()
        number_of_fishTanks = 6
        interval = 400
        xpos = 50
        for i in range(number_of_fishTanks):
            while xpos <= 850:
                new_fishTank = FishTank(xpos, 0, (.25))
                self.fishTanks.add(new_fishTank)
                xpos += interval
            else: 
                xpos = 50
                new_fishTank = FishTank(xpos, 600, (.25))
                self.fishTanks.add(new_fishTank)
                
        # self.fishTank1 = FishTank( 50, 0, 300, 100)
        # self.fishTank2 = FishTank( 450, 0, 300, 100)
        # self.fishTank3 = FishTank( 850, 0, 300, 100)
        # self.fishTank4 = FishTank( 50, 600, 300, 100)
        # self.fishTank5 = FishTank( 450, 600, 300, 100)
        # self.fishTank6 = FishTank( 850, 600, 300, 100)
        
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
                        self.view.drawGameScreen(self.player.getImg(), self.player.getRect(),self.fishTanks  )
                        
                        # col =  self.sprite.collide_rect(self.player, self.fishTank1)
                        # if col:
                        #     self.view.drawPopUp(col)
                        #     print("do something when they collide")
                        #if player collides with a tank, display specific pop up window about fish
                        #if self.fishTank1.checkForCollision(self.player.x, self.player.y):
                        #    self.view.drawPopUp()
                        #if self.fishTank2.checkForCollision(self.player.x, self.player.y):
                         #   self.view.drawPopUp()
                        #if self.fishTank3.checkForCollision(self.player.x, self.player.y):
                        #    self.view.drawPopUp()
                        #if self.fishTank4.checkForCollision(self.player.x, self.player.y):
                        #    self.view.drawPopUp()
                        #if self.fishTank5.checkForCollision(self.player.x, self.player.y):
                        #    self.view.drawPopUp()
                        #if self.fishTank6.checkForCollision(self.player.x, self.player.y):
                         #   self.view.drawPopUp()
                            
        pygame.quit()    
        
        

    