import itertools

A = "ABCDEFG"
a = "abcdef"

result = itertools.zip_longest(A, a, fillvalue=" ")
print(list(result))