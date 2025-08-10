import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cow Jump Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
PINK = (255, 182, 193)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Cow properties
cow_x = 100
cow_y = HEIGHT - 80
cow_width = 50
cow_height = 40
cow_vel_y = 0
gravity = 0.8
is_jumping = False

# Obstacles
obstacles = []
obstacle_speed = 5

score = 0

def draw_cow(x, y):
    """Draw a simple cartoon cow."""
    # Body
    pygame.draw.rect(screen, WHITE, (x, y, cow_width, cow_height))
    # Head
    pygame.draw.rect(screen, WHITE, (x + cow_width, y + 5, 20, 20))
    # Legs
    pygame.draw.rect(screen, BROWN, (x + 5, y + cow_height, 10, 15))
    pygame.draw.rect(screen, BROWN, (x + cow_width - 15, y + cow_height, 10, 15))
    # Nose
    pygame.draw.rect(screen, PINK, (x + cow_width + 15, y + 10, 10, 10))
    # Eye
    pygame.draw.circle(screen, BLACK, (x + cow_width + 10, y + 10), 3)

def draw_obstacles(obs_list):
    for obs in obs_list:
        pygame.draw.rect(screen, BROWN, obs)

def show_score(scr):
    text = font.render(f"Score: {scr}", True, BLACK)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    clock.tick(30)
    screen.fill((135, 206, 250))  # Sky blue background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                cow_vel_y = -12
                is_jumping = True

    # Gravity
    cow_y += cow_vel_y
    cow_vel_y += gravity
    if cow_y >= HEIGHT - 80:
        cow_y = HEIGHT - 80
        is_jumping = False

    # Spawn obstacles
    if random.randint(1, 40) == 1:
        obstacles.append(pygame.Rect(WIDTH, HEIGHT - 50, 30, 50))

    # Move obstacles
    for obs in obstacles:
        obs.x -= obstacle_speed

    # Remove off-screen obstacles
    obstacles = [obs for obs in obstacles if obs.x > -30]

    # Collision detection
    cow_rect = pygame.Rect(cow_x, cow_y, cow_width + 20, cow_height)
    for obs in obstacles:
        if cow_rect.colliderect(obs):
            print(f"💀 Game Over! Final Score: {score}")
            pygame.quit()
            sys.exit()

    # Score
    score += 1

    # Draw everything
    draw_cow(cow_x, cow_y)
    draw_obstacles(obstacles)
    show_score(score)

    pygame.display.flip()
