

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

## Ressources 
# https://www.lovelyanalytics.com/2016/09/06/k-means-comment-ca-marche/ 
# https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
# https://stackoverflow.com/questions/39390418/python-how-can-i-enable-use-of-kwargs-when-calling-from-command-line-perhaps

class KmeansClustering:
	def __init__(self, max_iter=30, ncentroid=4):
		self.ncentroid = ncentroid 
		self.max_iter = max_iter 
		self.centroids = [] 
	
	def fit(self, X):
		"""
		Run the k-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
			None.
		Raises:
			This function should not raise any Exception.
		"""
		mean = np.mean(X, axis = 0)
		std = np.std(X, axis = 0)
		n = X.shape[0]
		c = X.shape[1]
		self.centroids = np.random.randn(self.ncentroid, c)*std + mean
		dotcolor = 10*["r", "g", "c", "b", "k"]
		graph=plt.figure()
		draw=Axes3D(graph)

		for el in range(X.shape[0]) :
			dot = dotcolor[4] 
			draw.scatter(X[el][0], X[el][1], X[el][2], color = dot)
		for i, el in enumerate(self.centroids) :
			dot = dotcolor[i] 
			draw.scatter(el[0], el[1], el[2], s=130, color = dot, marker= "x")

		plt.show()


		dist = np.zeros((n, self.ncentroid))
		self.clusters = np.zeros(X.shape[0])

		# Getting the mean 
		for i in range(self.max_iter) :
			for i in range(self.ncentroid) :
				dist[:,i] = np.linalg.norm(X - self.centroids[i], axis=1)
		self.clusters = np.argmin(dist, axis = 1) 


		for i in range(self.ncentroid):
			self.centroids[i] = np.mean(X[self.clusters == i], axis=0)

		self.table = np.zeros((X.shape[0], X.shape[1] + 1))
		self.table[:,:-1] = X
		self.table[:,3] = self.clusters
	
	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
			the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
			This function should not raise any Exception.
		"""

		y = [self.table[self.table[:,3]==kluster] for kluster in np.unique(self.table[:,3])]
		moy = np.zeros((self.ncentroid, X.shape[1] + 1))
		i = 0

		for i, el in enumerate(y) :
			moy[i] = el.mean(axis=0) 
		moy = moy[moy[:, 0].argsort()]
		
		ret = np.chararray(shape=(X.shape[0], 1), itemsize=26)
		for i in range(X.shape[0]):
			if (self.table[i][3] == moy[0][3]):
				ret[i] = "The flying cities of Venus"
			elif (self.table[i][3] == moy[1][3]):
				ret[i] = "United Nations of Earth"
			elif (self.table[i][3] == moy[2][3]):
				ret[i] = "Mars Republic"
			elif (self.table[i][3] == moy[3][3]):
				ret[i] = "Asteroids Belt colonies"
		return ret


def main(**kwargs):
	
		
	kluster = KmeansClustering(max_iter=100)
	for k, v in kwargs.items():
		setattr(kluster, k, v)
	kluster.ncentroid = int(kluster.ncentroid)
	kluster.max_iter = int(kluster.max_iter)
	f = open(kluster.filepath)
	lines = f.readlines()
	data = []
	for i in range(len(lines)):
		data.append(lines[i].split(','))
	dataset = np.delete(np.array(data[1:], dtype='float'), 0, 1)
	dataset = dataset / np.linalg.norm(dataset, axis = 0)

	kluster.fit(dataset)
	print(kluster.predict(dataset))

	colors = 10*["r", "g", "c", "b", "k"]
	fig=plt.figure()
	ax=Axes3D(fig)
	for i in range(kluster.table.shape[0]):
		color = colors[int(kluster.table[i][3])]
		ax.scatter(kluster.table[i][0],kluster.table[i][1],kluster.table[i][2], color = color)
	i = 0
	for centroid in kluster.centroids:
		color = colors[i]
		ax.scatter(centroid[0], centroid[1], centroid[2], s = 130 , color = color, marker = "x")
		i += 1
	plt.show()

if __name__ == "__main__":
    main(
         **dict(arg.split('=') for arg in sys.argv[1:])) # kwargs