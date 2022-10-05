import itertools

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = itertools.tee(l, 3)
print(list(results[0]))