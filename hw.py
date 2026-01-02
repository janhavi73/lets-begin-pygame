import pygame
pygame.init()
WINDOW_SIZE = (500, 500)
CAPTION = "My first game screen"
BACKGROUND_COLOR = (58, 58, 58)
IMAGE_SIZE = (300, 300)
IMAGE_PATH = 'photo.png' 
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(CAPTION)
image = pygame.image.load(IMAGE_PATH)
image = pygame.transform.scale(image, IMAGE_SIZE)

