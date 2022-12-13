import matplotlib.pyplot as plt

if __name__ == '__main__':
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    plt.pie(sizes, labels=labels, autopct='%.2f%%')
    plt.show()