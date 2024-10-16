from Planet import planet
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 60

masses = []
centralMass = planet(100000, 400, 400, 0, 0, 30, 'yellow')
body1 = planet(2, 400, 150, 20, 0, 15, 'red')
body2 = planet(3, 200, 300, 0, 20, 20, 'blue')

masses.append(centralMass)
masses.append(body1)
masses.append(body2)

def draw_object(object):
    pygame.draw.circle(screen, object.color, (object.pos.x, object.pos.y), object.radius)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    ##
    for b in masses:
        b.gravity(masses)
    for b in masses:
        b.update(FPS)
        draw_object(b)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

