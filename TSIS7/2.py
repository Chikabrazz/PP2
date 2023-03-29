import pygame
import os

# Инициализация pygame
pygame.init()

# Создание окна для вывода информации о плеере
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Chikabrazz Music Player')

# Получение списка файлов в папке с музыкой
# music_folder = "D:\chikabrazz\MuzLo\VK Coffee"
music_folder = "music"
music_files = os.listdir(music_folder)

# Инициализация звукового потока
pygame.mixer.init()

# Загрузка музыкальных файлов в плеер
for file in music_files:
    pygame.mixer.music.queue(os.path.join(music_folder, file))


# Функция для воспроизведения музыки
def play_music():
    pygame.mixer.music.play()
    pygame.display.set_caption(music_files[0])


# Функция для остановки воспроизведения музыки
def stop_music():
    pygame.mixer.music.stop()


# Функция для перехода к следующей песне
def next_song():
    pygame.mixer.music.load(os.path.join(music_folder, music_files[1]))
    pygame.mixer.music.play()


# Функция для перехода к предыдущей песне
def prev_song():
    pygame.mixer.music.load(os.path.join(music_folder, music_files[-1]))
    pygame.mixer.music.play()

running = True
# Создание шрифта
font = pygame.font.Font(None, 30)

# Начальное значение текущего трека
current_track = music_files[0]

# Основной цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_song()
                current_track = music_files[(music_files.index(current_track) + 1) % len(music_files)]
            elif event.key == pygame.K_LEFT:
                prev_song()
                current_track = music_files[(music_files.index(current_track) - 1) % len(music_files)]

    # Отрисовка текущего трека
    screen.fill((34, 25, 26))
    text = font.render(current_track, True, (0, 0, 0))
    screen.blit(text, (10, 10))
    img = pygame.image.load('interface.png')
    img = pygame.transform.scale(img, (380,175))
    screen.blit(img, (10, 50))
    pygame.display.update()

# Освобождение занятых ресурсов
pygame.quit()




