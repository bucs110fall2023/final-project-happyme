class Player:
    def __init__(self, x, y, radius):
        self.color = "BLUE" #Blue 
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.radius = radius
        
    def updatePos(self, type):
        if type == 1:
            self.x -= 10
        if type == 2:
            self.x += 10
        if type == 3:
            self.y -= 10
        if type == 4:
            self.y -= 10