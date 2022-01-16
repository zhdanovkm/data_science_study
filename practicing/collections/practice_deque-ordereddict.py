a = [['Milk', 'Bread'], ['Meat']]
b = ['Milk', 'Bread', 'Meat']
print(len(a))
print(len(b))

from collections import deque

new = deque()

for i in a:
    for j in i:
        new.append(j)

print(new)
print(len(new))
