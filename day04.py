#list

a = [1,2,[5,9]]
b = a.copy()
c = list(a)
d = a[:]
a[1] = -77 #immutable
a[2][1] = 7 #mutable, b/c/d affects
print(a, b, c, d)


# import copy
# a = [1,2,[5,9]]
# b = copy.deepcopy(a)
# a[2][1] = 7 #mutable, deepcopy
# print(a, b)


# a = [1,2,[5,9]]
# b = a.copy()
# c = list(a)
# d = a[:]
# a[2][1] = 7 #mutable, b/c/d affects
# print(a, b, c, d)



# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# a[2] = 'sw' #immutalbe
# print(a, b, c, d)



primes = [2, 19, 3, 5, 7, 11]
primes_cp = primes
print(primes)
print(primes_cp)
primes[-1] = 'lunch time'
print(primes)
print(primes_cp)
primes_cp[0] = 'morning coffee'
print(primes)
print(primes_cp)

#TypeError: '<' not supported between instances of 'str' and 'int'
#mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무']
# mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']
# #mixed.sort()
# mixed.sort(reverse=True)
# print(mixed)


# primes = [2, 19, 3.0, 5, 7, 11]
# print(primes)
# primes.sort()
# print(primes)


# primes = [2, 19, 3.0, 5, 7, 11]
# primes_sorted = sorted(primes)
# print(primes)
# print((primes_sorted))
