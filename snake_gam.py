import pygame
import random
import math
import sys

# ---------------- SETUP ----------------
pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nokia Snake")

clock = pygame.time.Clock()

# Nokia-style colors
BG = (155, 170, 80)
DARK = (30, 40, 20)

font = pygame.font.SysFont("Courier", 24, bold=True)
big_font = pygame.font.SysFont("Courier", 48, bold=True)

# ---------------- FUNCTIONS ----------------
def new_game():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (BLOCK, 0)
    fruit = (
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    )
    return snake, direction, fruit, 0, False

def draw_snake(snake, direction, mouth_open):
    for i, (x, y) in enumerate(snake):
        if i == 0:
            # Head
            pygame.draw.rect(screen, DARK, (x, y, BLOCK, BLOCK), 3)

            if mouth_open:
                dx, dy = direction
                mx = x + BLOCK//2 + dx//2
                my = y + BLOCK//2 + dy//2
                pygame.draw.line(
                    screen, DARK,
                    (x + BLOCK//2, y + BLOCK//2),
                    (mx, my),
                    3
                )
        else:
            # Body dots
            pygame.draw.rect(screen, DARK, (x+6, y+6, 8, 8))

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def game_over_screen(score):
    text = big_font.render("GAME OVER", True, DARK)
    restart = font.render("R = Restart   Q = Quit", True, DARK)
    score_text = font.render(f"Score: {score}", True, DARK)

    screen.blit(text, (WIDTH//2 - 140, HEIGHT//2 - 60))
    screen.blit(score_text, (WIDTH//2 - 70, HEIGHT//2))
    screen.blit(restart, (WIDTH//2 - 150, HEIGHT//2 + 40))
    pygame.display.update()

# ---------------- GAME INIT ----------------
snake, direction, fruit, score, grow = new_game()
game_over = False

# ---------------- GAME LOOP ----------------
running = True
while running:
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and direction != (0, BLOCK):
                    direction = (0, -BLOCK)
                if event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                    direction = (0, BLOCK)
                if event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                    direction = (-BLOCK, 0)
                if event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                    direction = (BLOCK, 0)
            else:
                if event.key == pygame.K_r:
                    snake, direction, fruit, score, grow = new_game()
                    game_over = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    if not game_over:
        # Move snake (wrap walls)
        hx = (snake[0][0] + direction[0]) % WIDTH
        hy = (snake[0][1] + direction[1]) % HEIGHT
        new_head = (hx, hy)

        # Self collision
        if new_head in snake:
            game_over = True

        snake.insert(0, new_head)
        if not grow:
            snake.pop()
        grow = False

        # Eat fruit
        if new_head == fruit:
            score += 1
            grow = True
            fruit = (
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            )

        # Mouth opens when close
        mouth_open = distance(new_head, fruit) < 40

        # Draw fruit (pixel style)
        pygame.draw.rect(screen, DARK, (fruit[0]+5, fruit[1]+5, 10, 10))

        # Draw snake
        draw_snake(snake, direction, mouth_open)

        # Draw score (top-left)
        score_text = font.render(f"Score:{score}", True, DARK)
        screen.blit(score_text, (10, 10))

    else:
        game_over_screen(score)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
