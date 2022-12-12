def list_test():
    print("hello world!")
    my_list = list()
    my_list.append('hello')
    my_list.append(45)
    my_list.append(4.5)
    for item in my_list:
        print(item)


def dict_test():
    my_dict = dict()
    my_dict[1] = 'hello'
    my_dict[2] = 'world'
    print(my_dict[1])


if __name__ == "__main__":
    dict_test()
