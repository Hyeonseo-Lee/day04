#list comprehension

odd_lists = [i for i in range(1,11) if i % 2 ==1]
print(odd_lists, type(odd_lists))
odd_tuples = (i for i in range(1,11) if i % 2 ==1)
print(odd_tuples, type(odd_tuples))

print(type(range(1,101)))

# odd_lists = []
# for i in range(1,11):
#     if i % 2 == 1:
#         odd_lists.append(i)
# print(odd_lists)