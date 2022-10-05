import itertools

a = ["ABCDE", "abcde"]
result = itertools.pairwise(a)
print(list(result))