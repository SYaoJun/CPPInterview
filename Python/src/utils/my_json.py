import json
# 定义一个字典
data = {
    "name": "yaojun",
    "age": 100,
    "price": 11.20
}
json_str = json.dumps(data)  # 将字典data序列化为json对象
print(json_str)  # 序列化的json对象本质是字符串

data1 = json.loads(json_str)
print(data1)
# 如果我们要处理的是文件而不是字符串，则可以使用json.dump()和json.load()来编码和解码
