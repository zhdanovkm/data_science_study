from array import array
import numpy as np

a = np.array([[1,2,3],[1,2,3]])
print(a)
print(type(a))
print(a.dtype)

b = np.array([[4,5,6],[4,5,6]], dtype=np.int8)
print(b, '\n', b.dtype)

b[1,2]=2000
print(b)

b = np.float16(b)
print(b.dtype)

print(b.ndim) #Узнать размерность массива
print(b.size) #Узнать общее число элементов в массиве
print(b.shape) #Форма или структура массива
print(b.itemsize) #сколько «весит» каждый элемент массива в байтах

c = np.zeros(4) #Можно заранее подготовить массив заданной размерности, заполненный нулями, а потом загружать в него реальные данные по мере необходимости
print(c)

c = np.zeros((4,3,2), dtype=np.int8)
print(c)

d = np.arange(3) #для создания одномерных массивов arange([start,] stop, [step,], dtype=None).
print(d)

d = np.arange(2, 9, 0.4, dtype=np.float16)
print(d, type(d))

arr = np.linspace(1, 2, 10) #Она тоже возвращает одномерный массив из чисел, расположенных на равном удалении друг от друга между началом и концом диапазона
#np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#num — параметр, задающий число элементов, которое должно оказаться в массиве (по умолчанию 50);
#endpoint — включён или исключён конец диапазона (по умолчанию включён);
#retstep (по умолчанию False) позволяет указать, возвращать ли использованный шаг между значениями, помимо самого массива;
print(arr)

arr = np.linspace(1, 2, 10, endpoint=False)
print(arr)

arr, step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
print(step)

arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
print(round(step,2))