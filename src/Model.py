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

class FishTank(pygame.sprite.Sprite): 
    def __init__(self, x, y, scale):
        super().__init__()
        self.x = x
        self.y = y

        self.scale = scale
        self.image = pygame.image.load("assets/fishtank.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x , self.y]
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 2 *self.scale), int(self.rect.height * self.scale)))
        
    # def checkForCollision(self, playerx, playery):
    #     tankCollide = False
    #     if self.x1 <= playerx <= self.x1 + self.length and self.y1 <= playery <= self.y1 + self.width:
    #         tankCollide = True
    #     return tankCollide
    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, scale):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.scale = scale
        self.image = pygame.image.load("assets/character.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x , self.y]
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.scale), int(self.rect.height * self.scale)))
        
        
    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect.topleft
    
    def updatePos(self, type, dt):
        adjust = self.speed * dt
        #LEFT
        if type == 1:
            if (self.x - adjust) > 50:
                self.x -= adjust
        #RIGHT
        if type == 2:
            if (self.x + adjust) < 1050:
                self.x += adjust
        #UP
        if type == 3:
            if (self.y - adjust) > 0:
                self.y -= self.speed * dt
        
        #DOWN  
        if type == 4:
            if (self.y + adjust) < 500:
                self.y += self.speed * dt
        
        self.rect.topleft = [self.x , self.y]
            
class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
    def get_dt(self):
        self.dt = (self.clock.tick(60) / 1000)
        return self.dt