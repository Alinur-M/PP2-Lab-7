import pygame

pygame.init()


WIDTH, HEIGHT = 700, 700
WHITE = (255,255,255)
RED = (255,0,0)


radius = 25 


step = 20


x = WIDTH // 2
y = HEIGHT // 2


screen = pygame.display.set_mode((WIDTH, HEIGHT))
 

clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    keys = pygame.key.get_pressed()
    

    sdvig_po_OX = x + (keys[pygame.K_d] - keys[pygame.K_a]) * step
    sdvig_po_OY = y + (keys[pygame.K_s] - keys[pygame.K_w]) * step


    if WIDTH - radius > sdvig_po_OX:
        x = max(radius, sdvig_po_OX)
    else:
        x = max(radius, WIDTH - radius)

    if HEIGHT - radius > sdvig_po_OY:
        y = max(radius, sdvig_po_OY)
    else:
        y = max(radius, HEIGHT - radius)

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    pygame.display.flip()
  
    clock.tick(60)


pygame.quit()