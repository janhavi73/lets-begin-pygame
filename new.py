import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my first game screen")
bg_color = (58, 58, 58)
img = pygame.Surface((300, 300))
img.fill((255, 0, 0)) 
img_rect = img.get_rect(center=(250, 250)) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(bg_color)
    
    screen.blit(img, img_rect)
    
    pygame.display.flip()

pygame.quit()
