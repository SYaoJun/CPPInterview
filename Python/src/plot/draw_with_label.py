import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.plot([1, 3, 5, 7], [1, 9, 25, 49], 'r')
    # 有中文时需要加上fontproperties来确定显示的字体，此处是楷体和中文黑体及仿宋，fontsize来确定字体大小
    plt.title('format: function $y=x^2$', fontsize=20)
    plt.xlabel('x axis', fontsize=20)
    plt.ylabel('y axis', fontsize=20)
    plt.show()