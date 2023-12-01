import pygame
#import your controller

def main():
    pygame.init()
screen = pygame.display.set_mode((1000,700))
screen_size = pygame.display.get_window_size()
width, height = screen_size[0], screen_size[1]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/

if __name__ == '__main__':
    main()