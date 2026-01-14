import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my first game screen")
bg_color = (58, 58, 58)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(bg_color)
    
    
    
    pygame.display.flip()

pygame.quit()
