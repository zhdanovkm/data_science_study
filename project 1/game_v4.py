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
    maxlen = 100 # максимальное число
    minlen = 1 # минимальное число
    midlen = 0 # среднее число
    predict_number = 0
    
    while True:
        count+=1
        midlen = (maxlen+minlen)//2
        if number == midlen:
            predict_number=midlen
            break
        else:
            if number > midlen:
                minlen = midlen+1
            else:
                maxlen = midlen-1
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