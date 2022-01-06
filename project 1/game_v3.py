"""Игра угадай число, где компьютор сам загадывает
и сам угадывает число. *меньше чем за 20 попыток
"""

import numpy as np
from numpy.core.fromnumeric import size

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # счетчик числа попыток
    
    while True:
        count+=1
        if number <= 20: # делим диапазон от 0 до 100 на отрезки по 20 значений, чтобы программа отгадывала число меньше чем за 20 попыток.
            predict_number = np.random.randint(1, 21) # предполагаемое число
            if number == predict_number:
                break # выход из цикла если угадали
        elif number > 20 and number <= 40:
            predict_number = np.random.randint(21, 41) # предполагаемое число
            if number == predict_number:
                break # выход из цикла если угадали
        elif number > 40 and number <= 60:
            predict_number = np.random.randint(41, 61) # предполагаемое число
            if number == predict_number:
                break # выход из цикла если угадали
        elif number > 60 and number <= 80:
            predict_number = np.random.randint(61, 81) # предполагаемое число
            if number == predict_number:
                break # выход из цикла если угадали
        else:
            predict_number = np.random.randint(81, 101) # предполагаемое число
            if number == predict_number:
                break # выход из цикла если угадали
        
    return(count)  

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # создаем список для записи значений попыток угадывания
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Ваш аргуммент угадывает число в среднем за: {score}')
    return(score)
    
if __name__ == '__main__':
    # Run
    score_game(random_predict)