# zenzone_pygame.py
import pygame, sys
pygame.init()
W,H = 800,480
TILE=32
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
# simple level as list of strings
LEVEL = [
"                                ",
"                                ",
"      S          ===           G",
"    ____                   __  ",
"               ^   ^   ^       ",
"  ____  _____   _____  _____  ",
"###############################",
]
def draw():
    screen.fill((6,18,31))
    # draw tiles...
while True:
    dt = clock.tick(60)/1000
    for e in pygame.event.get():
        if e.type==pygame.QUIT: sys.exit()
    # handle input, physics, draw...
    pygame.display.flip()
