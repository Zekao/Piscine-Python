from ast import arg
from grapheme import length
import numpy as np
import matplotlib.pyplot as plt
import sys
import style
class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4, filepath=None, debug="0"):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        self.debug = debug


    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----

        X: has to be an numpy.ndarray, apython redoKmeans.py filepath="data.csv" ncentroid=3 max_iter=2 matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.

        -------
        Explains:
            -   First of all, we will pick a random value for each centroid
            -   After that, we will use our function predict until we've reached the number max_iter iterations
            -   
        """
        self.centroids = X[np.random.choice(X.shape[0], self.ncentroid, replace=False)]
        for _ in range(self.max_iter):
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

        ------
        Explains:
            -   np.linalg.norm will be useful to calculate distance between many points
                we will use it to get a tab with the distance between each point
            -   np.argmin will tell us the position of each lowest value, according to his position we will determine centroid
        """
        dist = np.linalg.norm(X[:, np.newaxis, :] - self.centroids[np.newaxis, :, :], axis=2)
        if int(self.debug) == 1:
            print(">" * 30 + " Dist Values " + "<" * 30)
            print(style.blue(dist))
            print(">" * 30 + " centroid " + "<" * 30)
            print(style.blue(np.argmin(dist, axis=1)))
        return np.argmin(dist, axis=1)
    
def main(**kwargs):
    
    try:
        kluster = KmeansClustering(**kwargs)
        data = np.genfromtxt(kwargs.get('filepath'), delimiter=",", skip_header=1)
    except Exception as e:
        print ('Usage: python Kmeans.py filepath=<filepath> ncentroid=<number> max_iter=<number>')
        print(style.red('>>> ' + str(e) + ' <<<'))
        return

    for _ in range(0, 20):
        print('>' * 30 + ' Test ' + str(_) + ' ' + '<' * 30)
        kluster.fit(data)
        labels = kluster.predict(data)
        for i in range(kluster.ncentroid):
            print("Cluster %d: %d points" % (i, np.sum(labels == i)))
            print ('-' * 69)
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.legend
    plt.show()

if __name__ == "__main__":
    args = {}
    for arg in sys.argv:
        if '=' in arg:
            k, v = arg.split('=')
            args[k] = v
            if v.isdigit():
                args[k] = int(v)
    main(**args)