import pygame 
class button: 
    def __init__(self, x, y, width, length, message, color, messageSize):
        self.x1 = x
        self.y1 = y
        self.width = width
        self.length = length
        self.font = pygame.font.SysFont("cambria", messageSize)
        xcoords = [self.x1, self.x1 + length, self.x1 + length, self.x1]
        ycoords = [self.y1, self.y1, self.y1 + width, self.y1 + width]
        self.points = list(zip(xcoords, ycoords))
        self.message = self.font.render(message, True, "WHITE")
        self.color = pygame.Color(color)

    def getPoints(self):
        return self.points
    
    def checkForInput(self, mousePos):
        buttonClicked = False
        if self.x1 <= mousePos[0] <= self.x1 + self.length and self.y1 <= mousePos[1] <= self.y1 + self.width:
            buttonClicked = True
        return buttonClicked

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