import itertools

l1 = "123"
l2 = "ABC"
result = itertools.product(l1, l2)
print(list(result))