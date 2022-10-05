import itertools

l = [(2, 5), (3, 2), (4, 3)]
result = itertools.starmap(pow, l)
print(list(result))


result_map = map(pow, l)
print(list(result_map))