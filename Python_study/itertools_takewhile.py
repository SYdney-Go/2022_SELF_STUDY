import itertools

l = [1, 2, 3, 4, 5, 6, 7, 8]
result = itertools.takewhile(lambda x : x < 5, l)
print(list(result))

# 결과 : [1, 2, 3, 4]