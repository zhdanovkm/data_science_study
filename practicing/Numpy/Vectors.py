import numpy as np

vec1 = np.array([1,2,3,4])
vec2 = np.array([5,6,7,8])
print(vec1+vec2) #сложение векторов происходит поэлементно

list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1+list2) #сложение списков происходит добавлением

print([x + y for x,y in zip(list1, list2)]) #формула для сложения элементов списка

print('\n', vec1**2)
print('\n', vec1<vec2)
print('\n', vec1<3)

length1 = np.sqrt(np.sum(vec1**2)) #сложная формула для определения длины вектора
print('\n', length1)

length1 = np.linalg.norm(vec1) #встроенная функция нахождения длины вектора в библиотеки numpy, модуль linalg
print('\n', length1)

distance = np.sqrt(np.sum((vec1-vec2)**2))
print('\n', distance) #расстояние между векторами

distance = np.linalg.norm(vec1-vec2)
print('\n', distance) #расстояние между векторами, встроенная функция

vec1 = np.arange(1, 6)
vec2 = np.linspace(10, 20, 5)
scalar_product = np.sum(vec1 * vec2) #скалярное произведение векторов
print('\n', scalar_product)

scalar_product = np.dot(vec1, vec2) #скалярное произведение векторов, встроенная функция
print('\n', scalar_product)

print('\n', vec1.min())
print('\n', np.max(vec1))
print('\n', np.mean(vec1))