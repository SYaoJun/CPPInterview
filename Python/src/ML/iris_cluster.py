from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    pca = PCA(n_components=2)
    reduced_X = pca.fit_transform(X)
    plt.scatter(reduced_X[:, :1], reduced_X[:, 1:2])
    plt.show()
