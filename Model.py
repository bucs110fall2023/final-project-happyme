import pygame 
class Button: 
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

class FishTank: 
    def __init__(self, x, y, length, width):
        self.x1 = x
        self.y1 = y
        self.length = length
        self.width = width
        xcoords = [self.x1, self.x1 + length, self.x1 + length, self.x1]
        ycoords = [self.y1, self.y1, self.y1 + width, self.y1 + width]
        self.points = list(zip(xcoords, ycoords))
        
    def getPoints(self):
        return self.points
    
    def checkForCollision(self, playerx, playery):
        tankCollide = False
        if self.x1 <= playerx <= self.x1 + self.length and self.y1 <= playery <= self.y1 + self.width:
            tankCollide = True
        return tankCollide
    
class Player:
    def __init__(self, x, y, radius, speed):
        self.color = "slateblue4" #Purple 
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
            if (self.y - adjust) > 50:
                self.y -= adjust
        #DOWN
        if type == 4:
            if (self.y + adjust) < 650:
                self.y += adjust
            
            
class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
    def get_dt(self):
        self.dt = (self.clock.tick(60) / 1000)
        return self.dt