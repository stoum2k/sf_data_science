"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно загадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    predict_number = np.random.randint(1, 101)  # предполагаемое число
    upper_limit = 101 # первоначальное значение верхнего предела поиска
    low_limit = 1 # первоначальное значение нижнего предела поиска
    
    while True:
        count += 1
        if predict_number < number: 
            low_limit = predict_number # сужение поиска снизу
            predict_number = np.random.randint(low_limit+1, upper_limit)
        elif predict_number > number:
            upper_limit = predict_number # сужение поиска сверху
            predict_number = np.random.randint(low_limit+1, upper_limit)
        if number == predict_number:
            break # выход из цикла если угадали  
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
