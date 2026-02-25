import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Square properties
rect = pygame.Rect(350, 250, 100, 100)
color = (255, 0, 0)
dragging = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                if rect.collidepoint(event.pos):
                    dragging = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                rect.center = event.pos # Move square center to mouse

    # Drawing
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()