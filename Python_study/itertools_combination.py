import itertools

l = [1, 2, 3]
result = itertools.combinations_with_replacement(l, 2)
print(list(result))