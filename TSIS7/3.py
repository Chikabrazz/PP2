import pygame

# инициализация Pygame
pygame.init()

# установка размеров экрана
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# установка цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# создание поверхности для рисования
ball_surface = pygame.Surface((50, 50))
ball_surface.set_colorkey(WHITE)
pygame.draw.circle(ball_surface, RED, (25, 25), 25)

# начальные координаты шарика
ball_x, ball_y = 295, 215

# главный цикл игры
running = True
while running:

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обработка пользовательского ввода
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x > 20:
        ball_x -= 20
    elif keys[pygame.K_RIGHT] and ball_x < screen_width - 70:
        ball_x += 20
    elif keys[pygame.K_UP] and ball_y > 20:
        ball_y -= 20
    elif keys[pygame.K_DOWN] and ball_y < screen_height - 70:
        ball_y += 20

    # рисование на экране
    screen.fill(WHITE)
    screen.blit(ball_surface, (ball_x, ball_y))
    pygame.display.flip()

pygame.quit()