import time


def timer(func):
    """Декоратор для замера времени выполнения функции."""

    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало замера времени
        result = func(*args, **kwargs)  # Вызов декорируемой функции
        end_time = time.time()  # Конец замера времени
        execution_time = end_time - start_time  # Вычисление времени выполнения
        print(f"Время выполнения функции '{func.__name__}': {execution_time:.6f} секунд.")
        return result  # Возврат результата выполнения функции

    return wrapper