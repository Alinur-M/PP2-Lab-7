import pygame # импортируем библиотеку pygame
import datetime # для работы с датой и временем

pygame.init() # инициализируем pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 1080 # задаем размеры экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # создаем окно с заданными размерами
pygame.display.set_caption("Clock") # задаем заголовок окна
clock = pygame.time.Clock() # создаем объект Clock для управления частотой кадров

bg = pygame.image.load("./clock/mickey.jpeg") # загружаем изображение фона
second_hand = pygame.image.load("./clock/sec.png") # загружаем изображение секундной стрелки
minute_hand = pygame.image.load("./clock/min.png") # загружаем изображение минутной стрелки

def blit_rotate(image, pos, angle): # функция для рисования повернутого изображения
    rotated_image = pygame.transform.rotate(image, angle) # поворачиваем изображение на заданный угол
    new_rect = rotated_image.get_rect(center=pos) # получаем новый прямоугольник с центром в заданной позиции
    screen.blit(rotated_image, new_rect.topleft) # рисуем повернутое изображение на экране

running = True # отвечает за условия работы цикла
while running: # главный цикл программы
    clock.tick(60) # устанавливаем частоту кадров до 60 FPS
   
    spisok = pygame.event.get() # получаем список всех событий

    for event in spisok: # списка событий
        if event.type == pygame.QUIT or \
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # проверяем тип события
            running = False # завершаем цикл и выходим из программы

    now = datetime.datetime.now() # получаем текущее время

    second_angle = -now.second / 60 * 360 + 145 # для получения угла поворота секундной стрелки, с помощью математической формулы 
    minute_angle = -now.minute / 60 * 360 - 45  # для получения угла поворота  минутной стрелки, с помощью математической формулы

    print(now, ' ', now.second)
    print(now, ' ', now.minute)

    center_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # определяем центр экрана, цельным числом 

    screen.blit(bg, (0, 0)) # рисуем фон на экран
    blit_rotate(second_hand, center_pos, second_angle) # рисуем секундную стрелку с поворотом
    blit_rotate(minute_hand, center_pos, minute_angle) # рисуем минутную стрелку с поворотом    
    pygame.draw.circle(screen, (232, 34, 51), center_pos, 20)   # рисуем центр часов

    pygame.display.flip()   # обновляем экран

pygame.quit() # завершаем работу pygame


















    

    pygame.display.flip()


pygame.quit()
