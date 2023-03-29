try:
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
        pygame.mixer.music.load(os.path.join(music_folder, file))


    # Функция для воспроизведения музыки
    def play_music():
        pygame.mixer.music.play()


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

except Exception as e:
    print("Ошибка: ", e)