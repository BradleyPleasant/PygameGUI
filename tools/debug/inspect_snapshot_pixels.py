import os
os.environ['SDL_VIDEODRIVER']='dummy'
import pygame
pygame.init()
img = pygame.image.load('ui_snapshot.png')
for p in [(20,39),(20,55),(15,15),(10,10)]:
    try:
        print(p, img.get_at(p))
    except Exception as e:
        print('err', p, e)

