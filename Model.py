import pygame 

class Player:
    def __init__(self, x, y, radius, speed):
        self.color = "BLUE" #Blue 
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.radius = radius
        self.speed = speed
        
    def updatePos(self, type, dt):
        if type == 1:
            self.x -= self.speed * dt
        if type == 2:
            self.x += self.speed * dt
        if type == 3:
            self.y += self.speed * dt
        if type == 4:
            self.y -= self.speed * dt
            
class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
    #def updateDT(self):
        #self.dt = (self.clock.tick(60) / 1000)
        
    def get_dt(self):
        self.dt = (self.clock.tick(60))
        return self.dt