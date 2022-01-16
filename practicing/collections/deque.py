from collections import deque

deq = deque()
deq.append('1')
deq.append('2')
deq.appendleft('3')

print(deq)
print(deq[0])

first_el = deq.popleft()

print(first_el)
print(deq)

last_el = deq.pop()

print(last_el)
print(deq)

deq.append('4')

print(deq)

del deq[0]

print(deq)

deq.extendleft([1, 2, 3])
deq.reverse()
deq.rotate(3)
deq.extend([5, 6, 7])

print(deq)
print(deq.index('4'))
print(deq.count(7))

lim_deq = deque([1, 2, 3], maxlen=5)

print(lim_deq)

lim_deq.extend([4, 5, 6 ,7])

print(lim_deq)

temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

days = deque(maxlen=7)
 
for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
    print("")