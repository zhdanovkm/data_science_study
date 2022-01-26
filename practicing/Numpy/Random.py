import numpy as np
from scipy import rand

random = np.random.rand() #случайное число от 0 до 1
print(random)

random = int(round(np.random.rand()*100,0)) #случайное число от 0 до 100
print("\n", random)

random = np.random.rand(5)
print("\n", random)

random = np.random.rand(2,4)
print("\n", random)

random = np.random.rand(2, 3, 4, 10, 12, 23)
print("\n", random)
