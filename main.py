import pygame
from src.Controller import Controller

def main():
    pygame.init()
    screen = Controller()#Create an instance on your controller object
    screen.mainloop() #Call your mainloop
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
     
#https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main() 