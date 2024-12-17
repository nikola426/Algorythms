"""
Жадный алгоритм решения задачи с коробками. Суть в том, что у нас есть несколько коробок, которые надо расположить друг
на друге так, чтобы каждая коробка в столбике могла выдержать вес коробок сверху. Складывать все коробки в один столбик
необязательно. Алгоритм намеренно реализован без помощи рекурсии и сортировки.
"""

from loguru import logger

from random import randint

# Класс "Коробка"
class Box:
    def __init__(self, box_num, weight, max_weight):
        # Номер коробки
        self.box_num = box_num

        # Вес коробки
        self.weight = weight

        # Максимальный вес, который коробка может выдержать
        self.max_weight = max_weight

    def __str__(self):
        return f'Коробка №{self.box_num}: вес: {self.weight}; прочность: {self.max_weight}'

# Функция генерации списка объектов "Коробка" со случайными весом и прочностью (от 1 до 100)
def boxes_init(cnt):
    return [Box(i + 1, randint(1, 100), randint(1, 100)) for i in range(cnt)]

# Функция поиска в столбике коробки с максимальным весом. Возвращает её вес и индекс в столбе.
def max_weight(box_list):
    max_box_weight = 0

    for i in range(len(box_list)):
        if box_list[i].weight > max_box_weight:
            max_box_weight = box_list[i].weight
            index = i

    return max_box_weight, index

# Функция поиска минимальной суммы веса и прочности коробок в списке доступных коробок. Не учитывает нули.
# В случае отсутствия доступных коробок возвращает False.
def minimum(num_list):
    min = 201

    for num in num_list:
        if (num != 0) and (num < min):
            min = num

    if min == 201:
        return False

    return min

# Функция вывода на экран списка коробок
def print_list(lst):
    box_str = ''

    for box in lst:
        if box != 0:
            box_str += f'{box}\n'

    print(box_str)

# Функция перебора и установки коробок друг на друга в столбик. На вход получает неотсортированный список коробок
# (входной). Возвращает специально отсортированный список (столб) из коробок
@logger.catch
def boxes_install(boxes_list):

    # Вычисляем суммы весов и прочности для каждой коробки во входном списке и заносим их в отдельный список. Если
    # коробка отсутствует, то записываем 0.
    sums_list = [box.weight + box.max_weight if box != 0 else 0 for box in boxes_list]

    # Инициализируем итоговый столбец
    box_tower = []

    # Инициализируем вес столбца
    sum_weights = 0

    # Запускаем цикл по списку сумм, в котором будем сверять и переставлять коробки
    for _ in sums_list:

        # Находим минимальную сумму в списке с помощью специальной функции поиска
        min_sum = minimum(sums_list)

        # Если в списке остались одни нули, то цикл завершается
        if not min_sum:
            break

        # Находим индекс минимальной суммы в списке сумм
        min_sum_index = sums_list.index(min_sum)

        # Если максимальная прочность коробки, обладающей это минимальной суммой, больше, чем вес столбца, то:
        if boxes_list[min_sum_index].max_weight >= sum_weights:

            # Добавляем коробку в низ столбца
            box_tower.append(boxes_list[min_sum_index])

            # Прибавляем вес коробки к весу столбца
            sum_weights += boxes_list[min_sum_index].weight

            # Удаляем коробку из входного списка
            boxes_list[min_sum_index] = 0
        else:

            # Находим коробку с максимальным весом и её индексом в столбце
            max_box_weight, max_weight_i = max_weight(box_tower)

            # Если вес коробки, обладающей минимальной суммой, меньше, чем вес самой тяжёлой коробки в столбце, то:
            if boxes_list[min_sum_index].weight < max_box_weight:

                # Возвращаем самую тяжёлую в столбце коробку обратно во входной список
                boxes_list[box_tower[max_weight_i].box_num - 1] = box_tower[max_weight_i]

                # Возвращаем сумму её веса и прочности в список сумм
                sums_list[box_tower[max_weight_i].box_num - 1] = (
                        box_tower[max_weight_i].weight + box_tower[max_weight_i].max_weight)

                # Вставляем новую коробку с минимальной суммой на место старой
                box_tower[max_weight_i] = boxes_list[min_sum_index]

                # Удаляем новую коробку из входного списка
                boxes_list[min_sum_index] = 0

        # Удаляем сумму прочности и веса рассмотренной коробки из списка сумм, даже если она не подошла ни под одно из
        # условий. Тем самым в дальнейшем она рассматриваться не будет.
        sums_list[min_sum_index] = 0

    # Возвращаем итоговый столбец (список)
    return box_tower

# Основная функция запуска программы
def main():

    # Инициализируем список коробок
    boxes_list = boxes_init(30)

    # Выводим его на экран с помощью специальной функции
    print('Коробки в наличии:')
    print_list(boxes_list)

    # Инициализируем номер итогового столбца (списка) коробок
    col = 0

    # Цикл запуска программы. Будет продолжаться до того, пока все коробки не будут расставлены, то есть пока в
    # boxes_list не останутся одни нули.
    while True:
        col += 1

        # Запускаем функцию перебора и установки коробок друг на друга
        box_tower = boxes_install(boxes_list)

        # Выводим результат
        print(f'Столб №{col}')
        print_list(box_tower)

        # Проверяем boxes_list на заполненность нулями. Если все элементы - нули, то цикл завершается
        for box in boxes_list:
            if box != 0:
                break
        else:
            break

main()