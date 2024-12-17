def pack_boxes(weights, box_capacity):
    # Сортируем веса в порядке убывания
    weights.sort(reverse=True)

    boxes = []  # Список для хранения оставшегося места в каждой коробке

    for weight in weights:
        # Пытаемся найти подходящую коробку
        placed = False
        for i in range(len(boxes)):
            # Сверяем текущий вес коробки плюс вес рассматриваемого предмета с максимальным весом, который может
            # выдержать коробка
            if sum(boxes[i]) + weight <= box_capacity:
                boxes[i].append(weight)  # Помещаем предмет в коробку
                placed = True
                break

        # Если не нашли подходящую коробку, создаем новую
        if not placed:
            boxes.append([weight])

    return boxes  # Возвращаем список коробок вместе с содержимым


# Пример использования
weights = [4, 8, 1, 4, 2, 1]
box_capacity = 10
boxes = pack_boxes(weights, box_capacity)
result = ''

for i in range(len(boxes)):
    result += f'Коробка №{i + 1}: {boxes[i]}\n'

print(result)
