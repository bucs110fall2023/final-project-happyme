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
        self.tanks_viewed = []
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

        #popup box initialization
        self.t1Info = InfoBox( "Guppy", "-A tropical fish native to South America", "-Omnivores", "-Named after Robert John Lechmere Guppy", "assets/guppy.jpg")
        self.t2Info = InfoBox( "Red Snapper", "-May grow up to 40 inches long", "-Prey to large marine mammals" , "-Can be fished at the Gulf of Mexico", "assets/redsnapper.jpg")
        self.t3Info = InfoBox( "Largemouth Bass", "-Top Predators in Aquatic Ecosystem", "-Native to the Mississippi River.", "-Can grow up to 16 inches in 3 years",  "assets/bass.jpg")
        self.t4Info = InfoBox( "Tuna", "-Very fast swimmers", "Travel in groups called 'schools'", "-Prey on crustaceans and squid", "assets/tuna.jpg")
        self.t5Info = InfoBox( "Blobfish", "-They have no bones or teeth", "-Native to New Zealand and Australia", "-Can grow up to 12 inches long" ,  "assets/blobfish.jpg")
        self.t6Info = InfoBox( "Pufferfish", "One of the most poisonous fish species", "-Can make nest patterns in the sand", "-Dolphins often play catch with this species", "assets/pufferfish.jpg")
        
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
                        
                        #if player collides with tank
                        #tank 1, top left
                        if pygame.sprite.collide_rect(self.player, self.fishTank1):
                            self.view.drawPopupScreen(self.t1Info.points, self.t1Info.image, self.t1Info.name, self.t1Info.fact1, self.t1Info.fact2, self.t1Info.fact3)
                            
                        #tank 2, top middle
                        if pygame.sprite.collide_rect(self.player, self.fishTank2):
                            self.view.drawPopupScreen(self.t2Info.points, self.t2Info.image, self.t2Info.name, self.t2Info.fact1, self.t2Info.fact2, self.t2Info.fact3)
                            
                        #tank 3, top right
                        if pygame.sprite.collide_rect(self.player, self.fishTank3):
                            self.view.drawPopupScreen(self.t3Info.points, self.t3Info.image, self.t3Info.name, self.t3Info.fact1, self.t3Info.fact2, self.t3Info.fact3)
                            
                        #tank 4, bottom left
                        if pygame.sprite.collide_rect(self.player, self.fishTank4):
                            self.view.drawPopupScreen(self.t4Info.points, self.t4Info.image, self.t4Info.name, self.t4Info.fact1, self.t4Info.fact2, self.t4Info.fact3)
                            
                        #tank 5, bottom middle
                        if pygame.sprite.collide_rect(self.player, self.fishTank5):
                            self.view.drawPopupScreen(self.t5Info.points, self.t5Info.image, self.t5Info.name, self.t5Info.fact1, self.t5Info.fact2, self.t5Info.fact3)
                           
                        #tank 6, bottom right
                        if pygame.sprite.collide_rect(self.player, self.fishTank6):
                            self.view.drawPopupScreen(self.t6Info.points, self.t6Info.image, self.t6Info.name, self.t6Info.fact1, self.t6Info.fact2, self.t6Info.fact3)
                                             
        
                    
        pygame.quit()    
        
