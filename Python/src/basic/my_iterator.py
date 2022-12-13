class Mylist(object):
    def __init__(self):
        self.items = []

    def __iter__(self):
        iter = MylistIterator(self.items)
        return iter

    def addItem(self, item):
        self.items.append(item)


class MylistIterator(object):
    '''自定义迭代器类'''

    def __init__(self, items):
        self.items = items
        self.currentIndex = 0

    def __iter__(self, mylist):
        pass

    def __next__(self):
        '''判断当前下标是否越界 '''
        if self.currentIndex < len(self.items):
            data = self.items[self.currentIndex]  # 根据下标获取下标对应的元素值
            self.currentIndex += 1  # 下标位置加1
            return data  # 返回下标对应的数据
        else:
            raise StopIteration  # 主动抛出异常 停止迭代


if __name__ == "__main__":
    mylist = Mylist()
    mylist.addItem("zhangsan")
    mylist.addItem("lisi")
    mylist.addItem("wanger")
    for value in mylist:
        print(value)
