import numpy as np
from sympy import Order

arr = np.arange(8)
print(arr)

arr.shape = (2,4) #меняем форму массива
print(arr)

arr_new = arr.reshape((1,8)) #принимает в качестве аргумента кортеж из чисел для формы, но возвращает новый массив, а не изменяет исходный

print("\n", arr_new)
print("\n", arr)

arr_new2 = arr_new.reshape((2,4), order='F') #order='C' (по умолчанию), массив заполняется по строкам. Если order='F', массив заполняется числами по столбцам

print("\n", arr_new2)

arr_trans = arr.transpose()
print("\n", arr_trans)

arr_lin = np.linspace(1,2,6) #ниже работа со срезами
print("\n", arr_lin)
print("\n", arr_lin[1])
print("\n", arr_lin[2:5])
print("\n", arr_lin[::-1])

nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4) #создание двумерного массива
print("\n", nd_array)
print("\n", nd_array[2][3])
print("\n", nd_array[2, 3])
print("\n", nd_array[:2, 3])
print("\n", nd_array[:2, 1:3])
print("\n", nd_array[::-1,-1:])

arr = np.array([23,12,45,12,23,4,15,3])
arr_new = np.sort(arr)
print("\n", arr)
print("\n", arr_new)

data = np.array([4, 9, -4, 3])
roots = np.sqrt(data)
print("\n", data)
print("\n", roots)

print(type(None))
print(type(np.nan))

print(None == None)
# True
print(np.nan == np.nan)
# False

print(None is None)
# True
print(np.nan is np.nan)
# True
print(np.nan is None)
# False

roots[np.isnan(roots)] = 0 #замена нан на 0
print("\n", sum(roots))
