# 正月点灯笼的视频
# 装饰器中含有返回值, 装饰器需要传参
import time


def display_time(func):
    def inner(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print("Total time: {:.4}".format(end - start))
        return res
    return inner  # 注意这里没有括号


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


@display_time
def count_prime_nums(maxmum):
    count = 0
    for i in range(2, maxmum):
        if is_prime(i):
            count += 1
    return count


if __name__ == '__main__':
    count = count_prime_nums(50000)
    print(count)
