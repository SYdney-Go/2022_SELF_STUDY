import itertools

a = [i for i in range(100)]
slice_result = itertools.islice(a, 10, 30)
print(list(slice_result))