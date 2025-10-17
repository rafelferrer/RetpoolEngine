import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pygame
import random

# Constantes
WIDTH, HEIGHT = 400, 600
GRAVITY = 500
JUMP = -200
GAP = 150
PIPE_WIDTH = 80
PIPE_SPEED = 200

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Retpool Engine")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Bird
bird_rect = pygame.Rect(100, HEIGHT//2, 34, 24)
bird_vel = 0

# Pipes
pipes = []
spawn_timer = 0
score = 0
passed_pipes = []

game_over = False

running = True
while running:
    dt = clock.tick(60) / 1000  # delta time en segundos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_over:
                bird_vel = JUMP
            else:
                # Reiniciar juego
                bird_rect.y = HEIGHT//2
                bird_vel = 0
                pipes.clear()
                spawn_timer = 0
                score = 0
                passed_pipes.clear()
                game_over = False

    if not game_over:
        # Física del pájaro
        bird_vel += GRAVITY * dt
        bird_rect.y += bird_vel * dt

        # Generar pipes
        spawn_timer += dt
        if spawn_timer > 1.5:
            spawn_timer = 0
            h = random.randint(100, HEIGHT-100-GAP)
            top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, h)
            bottom_pipe = pygame.Rect(WIDTH, h+GAP, PIPE_WIDTH, HEIGHT-h-GAP)
            pipes.extend([top_pipe, bottom_pipe])

        # Mover pipes
        for pipe in pipes:
            pipe.x -= PIPE_SPEED * dt

        # Colisiones
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                game_over = True
        if bird_rect.y > HEIGHT or bird_rect.y < 0:
            game_over = True

        # Contar score
        for pipe in pipes:
            if pipe.y == 0 and pipe.x + PIPE_WIDTH < bird_rect.x and pipe not in passed_pipes:
                score += 1
                passed_pipes.append(pipe)

    # Dibujar
    screen.fill((135, 206, 250))  # cielo azul

    # Pipes verdes
    for pipe in pipes:
        pygame.draw.rect(screen, (0, 200, 0), pipe)

    # Bird amarillo
    pygame.draw.rect(screen, (255, 255, 0), bird_rect)

    # Score
    score_surf = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_surf, (10,10))

    if game_over:
        go_surf = font.render("GAME OVER", True, (255,0,0))
        screen.blit(go_surf, (WIDTH//2-80, HEIGHT//2-20))

    pygame.display.flip()
