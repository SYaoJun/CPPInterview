from collections import deque

dq = deque(['a', 'b', 'c'])
dq.append(1)  # 右边加
dq.appendleft(2)  # 左边加
dq.insert(2, 'x')  # 下标为2的位置插入
dq.pop()  # 弹出右边
dq.popleft()  # 弹出左边
dq.remove('x')  # 删除指定元素
dq.reverse()  # 反转
print(dq)