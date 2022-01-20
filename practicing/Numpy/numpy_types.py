import numpy as np

a = np.int16(10)
print(a)
print(type(a))
print(np.iinfo(a))

print(np.iinfo(np.uint64))

c = a + 20

print(c, type(c))

d = np.int8(520)

print(d)

e = np.uint8(200)
f = np.uint8(60)

print(e, f)
print(e+f)

print(np.finfo(np.float128))

#print(np.sctypeDict)
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

print(np.uint8(-456))
