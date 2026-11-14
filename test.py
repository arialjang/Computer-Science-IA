import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

# 1. Create the main surface with per-pixel alpha support
cover = pygame.Surface((600, 400), pygame.SRCALPHA)
cover.fill((20, 20, 40, 100))  # Semi-transparent dark blue

# 2. Create a mask surface for the hole
hole_radius = 80
hole_mask = pygame.Surface((hole_radius * 2, hole_radius * 2), pygame.SRCALPHA)
# Draw a white circle with full alpha (255) to subtract all alpha from the cover
pygame.draw.circle(hole_mask, (0, 0, 0, 255), (hole_radius, hole_radius), hole_radius)

# 3. Cut the hole out of the cover surface
cover.blit(hole_mask, (300 - hole_radius, 200 - hole_radius), special_flags=pygame.BLEND_RGBA_SUB)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a bright background to verify the hole is transparent
    screen.fill((255, 200, 50))

    # Blit the surface with the hole on top
    screen.blit(cover, (0, 0))
    pygame.display.flip()

pygame.quit()
