#tuple
a = 'harry',
b = ('harry',)
c=()
d = 'harry', 'ron' #packing
e = ('hermione') #string
f = ('harry', 'ron') #packing
g = ('hermione',)
print(g, id(g))
g = g+f
print(g, id(g))
print(g)
print(g+f)
print(f[1])
x, y = f #unpacking
print(y)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

