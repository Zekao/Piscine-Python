from ast import arg
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.centroids = X[np.random.choice(X.shape[0], self.ncentroid, replace=False)]
        for i in range(self.max_iter):
            labels = self.predict(X)
            self.centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.ncentroid)])
        print(labels)
        return 

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        dist = np.linalg.norm(X[:, np.newaxis, :] - self.centroids[np.newaxis, :, :], axis=2)
        return np.argmin(dist, axis=1)
    
def main(**kwargs):
    
    kluster = KmeansClustering(**kwargs)
    data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
    kluster.fit(data)
    labels = kluster.predict(data)
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.legend(loc="upper left") 

    plt.show()
    
    




    # plt.scatter(X[:, 0], X[:, 1], c=kluster.predict(X))
    
    # plt.show()



if __name__ == '__main__':
    main()