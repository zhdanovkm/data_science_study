from collections import OrderedDict

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
client_ages = dict(data)

ordered_client = OrderedDict(data)

print(client_ages)
print(ordered_client)

sort_ordered_client = OrderedDict(sorted(data, key=lambda x: x[1]))

print(sort_ordered_client)

sort_ordered_client2 = OrderedDict(sorted(data, key=lambda x: x[0]))

print(sort_ordered_client2)

sort_ordered_client['Sonya']=16

print(sort_ordered_client)

import sys
print(sys.version)