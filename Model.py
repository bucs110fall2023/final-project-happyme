import pygame 
class button: 
    def __init__(self, x , y , width, length, message, color):
        self.x1 = x
        self.y1 = y
        self.cord1 = ((self.x1, self.y1))
        self.cord2 = ((self.x1 + length, self.y1))
        self.cord3 = ((self.x1 + length, self.y1 + width))
        self.cord4 = ((self.x1 , self.y1 + width))
        self.font = pygame.font.Font(None, 48)
        self.message = self.font.render(message, True, "WHITE")
        self.color = color
        self.buttonMessage = self.font.render(self.message, True, self.color)
    
    def checkForInput (self, position):
        buttonPress = False
        if position[0] in range(self.buttonMessage.left, self.buttonMessage.right)and position[1] in range(self.buttonMessage.top, self.buttonMessage.bottom):
            buttonPress = True
        return buttonPress    
    
    def getPoints (self):
        points = [ self.cord1,  self.cord2,  self.cord3,  self.cord4]
        return points
        
        
class fishTank: 
    def __init__(self, color, startx, starty, length):
        self.color = color
        self.points = [(startx, starty), (startx + length, starty), (startx + length, starty - length), (startx, starty - length)]
        #points does not work 
    def getTankPoints(self):
        pointsCopy = self.points.copy()
        return pointsCopy
    
class Player:
    def __init__(self, x, y, radius, speed):
        self.color = "cornflowerblue" #Blue 
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        
    def updatePos(self, type, dt):
        adjust = self.speed * dt
        #LEFT
        if type == 1:
            if (self.x - adjust) > 100:
                self.x -= adjust
        #RIGHT
        if type == 2:
            if (self.x + adjust) < 1100:
                self.x += adjust
        #UP
        if type == 3:
            if (self.y - adjust) > 100:
                self.y -= adjust
        #DOWN
        if type == 4:
            if (self.y + adjust) < 600:
                self.y += adjust
            
            
class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
    def get_dt(self):
        self.dt = (self.clock.tick(60) / 1000)
        return self.dt