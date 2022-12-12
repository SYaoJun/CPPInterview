from collections import Counter

colors = ['red', 'red', 'blue', 'blue', 'green', 'yellow']
result = Counter(colors)
print(dict(result))  # 统计词频
print(result.most_common(2))  # 频次最高的两个对象
