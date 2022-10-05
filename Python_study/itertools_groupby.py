import itertools
import operator
import pprint

data = [
    {"name":"Lee", "score":"A"},
    {"name":"Ju", "score":"A"},
    {"name":"Han", "score":"B"},
    {"name":"Kim", "score":"C"},
    {"name":"Kang", "score":"B"},
    {"name":"Go", "score":"A"},
    {"name":"Yun", "score":"D"},
    {"name":"Im", "score":"F"},
    {"name":"Sin", "score":"D"},
]

data = sorted(data, key=operator.itemgetter("score"))

grouped_data = itertools.groupby(data, key=operator.itemgetter("score"))

result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)

pprint.pprint(result)