import numpy as np

random = np.random.rand() #случайное число от 0 до 1
print(random)

random = int(round(np.random.rand()*100,0)) #случайное число от 0 до 100
print("\n", random)

random = np.random.rand(5)
print("\n", random)

random = np.random.rand(2,4)
print("\n", random)

#random = np.random.rand(2, 3, 4, 10, 12, 23) - 6и мерный массив, много места
#print("\n", random)

shape = (2,3)
random = np.random.rand(*shape) #кортеж обрабатывается только в распакованном виде *
print("\n", random)

random = np.random.sample(shape) #для этой функции не нужна распаковка кортежа
print("\n", random)

random = np.random.uniform()
print("\n", random)
random = np.random.uniform(-5, 10)
print("\n", random)
random = np.random.uniform(-5, 10, size=3) #верхняя, нижняя граница + размер
print("\n", random)
random = np.random.uniform(-5, 10, size=(3,2)) 
print("\n", random)

random = np.random.randint(4, size=(2,3)) #randint(low, high=None, size=None, dtype=int)
print("\n", random)

random = np.random.randint(6, 12, size=(3,3))
print("\n", random)

arr = np.arange(6)
print(arr)
print(np.random.shuffle(arr)) #Просто перемешать все числа в массиве 
print(arr) 

playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
shuffled = np.random.permutation(playlist) #Чтобы получить новый перемешанный массив, а исходный оставить без изменений
print(shuffled)
print(playlist)

print(np.random.permutation(10)) #Перемешать набор чисел от 0 до n-1 без использования функции arrange

#выбрать 2х случайных людей из списка без повторений:
workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
choice = np.random.choice(workers, size=2, replace=False)
print(choice)

#для воспроизводимого кода необходимо использовать seed:
np.random.seed(23)
print(np.random.randint(10, size=(3,4))) 

np.random.seed(100)
print(np.random.randint(10, size=3))
print(np.random.randint(10, size=3))
print(np.random.randint(10, size=3))

ar=np.arange(2,17,2)
print(ar)