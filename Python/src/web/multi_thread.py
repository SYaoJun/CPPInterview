#子线程会等待所有的子线程结束后才结束
"""
参考博客https://blog.csdn.net/SYaoJun/article/details/103896590
"""
import threading
import time
def sing():
    for i in range(5):
        print("唱歌")
        time.sleep(0.5)
def dance():
    for i in range(5):
        print("跳舞")
        time.sleep(0.5)


if __name__ == '__main__':

    t1 = threading.Thread(target=sing)  # 注意函数名是没有小括号的
    t1.start()
    t2 = threading.Thread(target=dance)  # 注意函数名是没有小括号的
    t2.start()
    print("主线程结束了！")
