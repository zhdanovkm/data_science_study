## Проект 1: Угадай число менее чем за 20 попыток

## Оглавление
[1. Описание проекта](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Описание-проекта)

[2. Какой кейс решаем](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Какой-кейс-решаем)

[3. Краткая информайия о данных](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Этапы-работы-над-проектом)

[5. Результат](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Результат)

[6. Выводы](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Выводы)

### Описание проекта
Угадать загаданное компьютером число менее чеем за 20 попыток.

:arrow_up: [к оглавлению](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Оглавление)

## Какой кейс решаем
Нужно написать программу, которая угадывает числа менее чем за 20 попыток

**Условия соревнования:**
- Компьютер загадывает число от 0 до 100, и нам его нужно "угадать". Под угадать, подразумевается "написать программу, которая угадвает число."
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам. При этом случайные числа подбираются из 5-ти интервалов по 20 значений.

**Метрика качества:**
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем:**
Учимся писать хороший код на Python

:arrow_up: [к оглавлению](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Оглавление)

## Краткая информация о данных
Случайные числа

:arrow_up: [к оглавлению](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Оглавление)

## Этапы работы над проектом
1. Создали функцию  random_predict для определения в каком отрезке по 20 значений из интервала от 0 до 100 находится загаданное число и далее генерируется случайное число в данном отрезке и фиксируется кол-во попыток по угадыванию загаданного числа.

2. Создали функцию score_game, которая генерирует список из 1000 случайных чисел, которые подаются на вход функции random_predict, после чего фиксируется среднее число попыток, за которое было отгадано число.

:arrow_up: [к оглавлению](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Оглавление)

## Результат
Программа отгадывает число в среднем за 19 раз.

:arrow_up: [к оглавлению](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Оглавление)

## Выводы
1. Научились пользоваться функцией random из библиотеки numpy

2. Вспомнили как использовать циклы и f-строки

:arrow_up: [к оглавлению](https://github.com/zhdanovkm/data_science_study/blob/main/project%201/README.MD#Оглавление)
