from collections import Counter

c = Counter()
c['red']=1
c['red']+=1
c['black']=2
print(c)

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']

cars_counter = Counter(cars)
print(sum(cars_counter.values()))

cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

print(counter_moscow, counter_spb)
counter_moscow.subtract(counter_spb)
print(*counter_moscow.elements())
print(list(counter_moscow))
print(dict(counter_moscow))
print(counter_moscow.most_common(1))