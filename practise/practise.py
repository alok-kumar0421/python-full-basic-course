import pygame
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Follow Snake")

clock = pygame.time.Clock()

segments = 25
distance = 15

snake = [(width/2, height/2)] * segments

def follow(target, current, dist):
    tx, ty = target
    cx, cy = current

    dx = tx - cx
    dy = ty - cy

    angle = math.atan2(dy, dx)

    cx = tx - math.cos(angle) * dist
    cy = ty - math.sin(angle) * dist

    return (cx, cy)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    mouse = pygame.mouse.get_pos()
    snake[0] = mouse

    for i in range(1, segments):
        snake[i] = follow(snake[i-1], snake[i], distance)

    for i in range(segments-1):
        pygame.draw.line(screen, (0,255,0), snake[i], snake[i+1], 4)

    pygame.display.update()
    clock.tick(60)

pygame.quit()