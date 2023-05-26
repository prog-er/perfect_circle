import pygame
import math

import time
# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH = 800
HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Установка размеров окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рисование круга")

# Переменные для отслеживания рисования
drawing = False
start_point = None
end_point = None

# Переменные для отслеживания ошибок
too_close_error = False
too_slow_error = False

center = (WIDTH / 2, HEIGHT / 2)

pygame.draw.ellipse(window, WHITE, (*center, 20, 20))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                start_point = event.pos
                window.fill(BLACK)

                start_time = time.time()

                radius = math.dist(start_point, center)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                if drawing:
                    end_point = event.pos
                    drawing = False
                    # Вычисление радиуса и центра круга

                    # Проверка на ошибки


        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                end_point = event.pos

                if time.time() - start_time > 5:
                    too_slow_error = True
                elif math.dist(center, end_point) < 100:
                    too_close_error = True
                elif radius < 50:
                    too_close_error = True
                else:
                    too_close_error = False
                    too_slow_error = False
                    pygame.draw.rect(window, BLACK, (10, 10, 200, 30))

    # Очистка экрана
    # window.fill(BLACK)

    # Рисование круга
    if start_point and end_point:

        # Вычисление погрешности круга в процентах
        perfect_circle_error = math.fabs(1 - (math.dist(end_point, center) / radius)) * 100

        pygame.draw.rect(window, RED, (300, 15, 200, 40))
        font = pygame.font.Font(None, 56)
        text = font.render(f"{round(100 - perfect_circle_error, 2)}%", True, GREEN)
        window.blit(text, (315, 15))

        # Изменение цвета в зависимости от погрешности
        color = (255, int(255 * (1 - perfect_circle_error / 100)), int(255 * (1 - perfect_circle_error / 100)))

        # Отрисовка круга
        try:
            pygame.draw.ellipse(window, color, (end_point[0] - 5, end_point[1] - 5, 10, 10))

        except:
            pygame.draw.rect(window, RED, (10, 10, 200, 30))
            font = pygame.font.Font(None, 25)
            text = font.render("Слишком далеко", True, BLACK)
            window.blit(text, (15, 15))

    # Отображение ошибок
    if too_close_error:
        pygame.draw.rect(window, RED, (10, 10, 200, 30))
        font = pygame.font.Font(None, 25)
        text = font.render("Слишком близко к центру!", True, BLACK)
        window.blit(text, (15, 15))

    if too_slow_error:
        pygame.draw.rect(window, RED, (10, 50, 200, 30))
        font = pygame.font.Font(None, 25)
        text = font.render("Слишком медленное рисование!", True, BLACK)
        window.blit(text, (15, 55))

    pygame.draw.ellipse(window, WHITE, (*center, 20, 20))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()

