def test(x):
    x += 1
    yield x


if __name__ == '__main__':
    value = test(1)
    print(next(value))
