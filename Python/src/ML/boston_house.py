import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    boston = datasets.load_boston()
    data_X = boston.data
    y = boston.target
    model = LinearRegression()
    model.fit(data_X, y)
    pred = model.predict(data_X[:2, :])
    actu = y[:2]
    print(pred)
    print(actu)
    plt.show()
