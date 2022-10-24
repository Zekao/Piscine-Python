from ast import arg
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        print('ncentroid: ', ncentroid)
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
        if (isinstance(X, np.ndarray) and len(X.shape) == 2):
            self.centroids = X[np.random.choice(X.shape[0], self.ncentroid, replace=False)]
            for i in range(self.max_iter):
                labels = self.predict(X)
                self.centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.ncentroid)])
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

        if (isinstance(X, np.ndarray) and len(X.shape) == 2):
            dist = np.linalg.norm(X[:, np.newaxis, :] - self.centroids[np.newaxis, :, :], axis=2)
            return np.argmin(dist, axis=1)

        return None
    
def main(**kwargs):
    
    kluster = KmeansClustering(20, 5)
    kluster.predict([1, 6, 7, 81, 5, 7, 9])
    print(kluster)
    plt.show()


if __name__ == '__main__':
    main()