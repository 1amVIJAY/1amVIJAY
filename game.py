import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NFT Cow Runner")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

# Load cow image (replace with your NFT cow PNG)
cow_img = pygame.image.load("cow.png")
cow_img = pygame.transform.scale(cow_img, (80, 80))
cow_rect = cow_img.get_rect(midbottom=(100, HEIGHT - 30))

# Obstacle
obstacle_img = pygame.Surface((50, 50))
obstacle_img.fill((200, 0, 0))
obstacles = []

# Physics
gravity = 0
jump_force = -15

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and cow_rect.bottom >= HEIGHT - 30:
                gravity = jump_force

    # Cow movement
    gravity += 1
    cow_rect.y += gravity
    if cow_rect.bottom >= HEIGHT - 30:
        cow_rect.bottom = HEIGHT - 30

    # Spawn obstacles
    if random.randint(1, 50) == 1:
        obstacle_rect = obstacle_img.get_rect(midbottom=(WIDTH, HEIGHT - 30))
        obstacles.append(obstacle_rect)

    # Move obstacles
    for obstacle in obstacles:
        obstacle.x -= 5
        screen.blit(obstacle_img, obstacle)
    obstacles = [o for o in obstacles if o.x > -50]

    # Draw cow
    screen.blit(cow_img, cow_rect)

    # Collision check
    for obstacle in obstacles:
        if cow_rect.colliderect(obstacle):
            print("Game Over")
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

