import pygame, os, random, math
from os import listdir
from os.path import isfile, join

height = 720
width = 1280
BG = pygame.image.load("Python Stuff/Games/Spider Game/assets/main_bg.jpg")
fps = 60

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Spider game")
window = pygame.display.set_mode((width, height))

def main(window):
    
    
    def spider():
        player_vel = 5
        
   
    
    def map(window, BG):
        window.blit(BG, (0, 0))
        pygame.display.update()
            
            
    
    def others():
        pass
    
    run = True
    while run:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        map(window, BG)
        
    pygame.quit()
    quit()
    
    
if __name__ == "__main__":
    main(window)        
        