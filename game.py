import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cow Adventure 🐄")

# Clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
COW_COLOR = (255, 255, 200)  # light cream

# Cow position
cow_x = 50
cow_y = HEIGHT - 120
cow_y_velocity = 0
gravity = 1
jump_strength = -15
is_jumping = False
cow_size = 60

# Ground
ground_height = HEIGHT - 40

# Obstacles
obstacle_width = 40
obstacle_height = 60
obstacle_x = WIDTH
obstacle_speed = 6

score = 0
font = pygame.font.SysFont(None, 40)

# Main game loop
running = True
while running:
    clock.tick(60)
    screen.fill(SKY_BLUE)

    # Draw ground
    pygame.draw.rect(screen, GREEN, (0, ground_height, WIDTH, 40))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                cow_y_velocity = jump_strength
                is_jumping = True

    # Update cow position
    cow_y_velocity += gravity
    cow_y += cow_y_velocity
    if cow_y >= HEIGHT - 120:
        cow_y = HEIGHT - 120
        cow_y_velocity = 0
        is_jumping = False

    # Move obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        score += 1

    # Draw obstacle
    pygame.draw.rect(screen, BROWN, (obstacle_x, ground_height - obstacle_height, obstacle_width, obstacle_height))

    # Draw cow (circle shape)
    pygame.draw.circle(screen, COW_COLOR, (cow_x + cow_size // 2, cow_y + cow_size // 2), cow_size // 2)

    # Collision detection
    cow_rect = pygame.Rect(cow_x, cow_y, cow_size, cow_size)
    obstacle_rect = pygame.Rect(obstacle_x, ground_height - obstacle_height, obstacle_width, obstacle_height)
    if cow_rect.colliderect(obstacle_rect):
        print(f"💀 Game Over! Final Score: {score}")
        running = False

    # Score display
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
