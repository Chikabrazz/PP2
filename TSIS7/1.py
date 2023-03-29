import pygame
import math
import time

pygame.init()

# установка размеров окна
window = pygame.display.set_mode((1400, 750))

# установка названия окна
pygame.display.set_caption("Mickey Mouse Clock")

# загрузка изображений рук Микки
minute_hand = pygame.image.load('mickey_minute_hand.png')
second_hand = pygame.image.load('mickey_second_hand.png')

minute_hand = pygame.transform.scale(minute_hand, (int(minute_hand.get_width() / 2), int(minute_hand.get_height() / 2)))
second_hand = pygame.transform.scale(second_hand, (int(second_hand.get_width() / 2), int(second_hand.get_height() / 2)))

# установка центра изображений в центр окна
minute_hand_rect = minute_hand.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
second_hand_rect = second_hand.get_rect(center=(window.get_width() // 2, window.get_height() // 2))

# функция для получения угла поворота руки
def get_angle(current_time, max_value):
    angle = (360 / max_value) * current_time
    return math.radians(angle - 90)

# главный цикл приложения
while True:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # получение текущего времени
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # получение углов поворота для рук Микки
    minute_hand_angle = get_angle(minute, 60)
    second_hand_angle = get_angle(second, 60)

    # поворот рук Микки
    minute_hand_rotated = pygame.transform.rotate(minute_hand, -math.degrees(minute_hand_angle))
    second_hand_rotated = pygame.transform.rotate(second_hand, -math.degrees(second_hand_angle))

    # установка точки центра вращения изображения
    minute_hand_rotated_rect = minute_hand_rotated.get_rect(center=minute_hand_rect.center)
    second_hand_rotated_rect = second_hand_rotated.get_rect(center=second_hand_rect.center)

    # отображение рук Микки на экране
    window.fill((255, 255, 255))
    window.blit(minute_hand_rotated, minute_hand_rotated_rect)
    window.blit(second_hand_rotated, second_hand_rotated_rect)
    pygame.display.update()