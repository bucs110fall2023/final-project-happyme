import pygame
#import your controller

#variables
player_velocity = 10
player_width = 40
player_height = 60

def check_input (key):
    if key == pygame.K_LEFT:
        player_x -= player_velocity
    elif key == pygame.K_RIGHT:
        player_x += player_velocity
    elif key == pygame.K_DOWN:
        player_y += player_velocity
    elif key == pygame.K_UP:
        player_y -= player_velocity
                    
def mainloop(pygame):
    player_x = 30 
    player_y = -30 
    run = True
    screen = pygame.display.set_mode((1200, 720)) 
    pygame.display.set_caption("Museum")
        
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYDOWN: 
            check_input((event.key))
                        
        screen.fill("WHITE")
        pygame.draw.rect(screen, ("PURPLE"), (player_x, player_y, player_width, player_height ))
        pygame.display.update()
    
       

def main():
    pygame.init()
    
    #Create an instance on your controller object
    mainloop (pygame) #Call your mainloop
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
#if __name__ == '__main__':
    #main()

main()

 