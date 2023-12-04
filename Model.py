import pygame 

class Player:
    def __init__(self, x, y, radius, speed):
        self.color = "BLUE" #Blue 
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
        
    #def updateDT(self):
        #self.dt = (self.clock.tick(60) / 1000)
        
    def get_dt(self):
        self.dt = (self.clock.tick(60) / 1000)
        return self.dt