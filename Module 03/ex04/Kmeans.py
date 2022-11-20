from math import sqrt
import sys
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.cluster import KMeans
import matplotlib.colors as mcolors

class CsvReader():
    def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
        try:
            self.file_obj = open(filename, "r")
            self.sep = sep
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
            self.header = header

        except FileNotFoundError as inst:
            print(inst)
            sys.exit()

    def __enter__(self):
        recordsCount = len(str(self.file_obj.readline()).split(self.sep))
        for line in self.file_obj.readlines():
            splitedLine = str(line[:-1]).split(self.sep)
            if (any(not el for el in splitedLine)):
                return None
            if (recordsCount != len(splitedLine)):
                return None
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        result = []
        self.file_obj.seek(0)
        for idx, line in enumerate(self.file_obj.readlines()):
            if (self.skip_bottom <= idx >= self.skip_top and line[:-1]):
                result.append(str(line[:-1]).split(self.sep))
        return result

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if (self.header is None):
            return None
        else:
            self.file_obj.seek(0)
            return str(self.file_obj.readline()[:-1]).split(self.sep)


def drawKmeans(header, globalIdx, kmean, globalVar):
    clusters = kmean[0]
    centroids = kmean[1]
    var = kmean[2]

    def draw3d():
        plt.figure()
        axes = plt.axes(projection='3d')
        axes.set_xlabel(header[0])
        axes.set_ylabel(header[1])
        axes.set_zlabel(header[2])
        color = ["red", "blue", "green", "magenta"]
        for idx, point in enumerate(centroids):
            plt.plot(point[0], point[1], point[2], marker=("o"), color=color[idx], label="Cluster  #{}, mean distance of {:.2f}".format(idx, var[idx]))
        for idxC, cluster in enumerate(clusters):
            for point in cluster:
                plt.plot(point[1], point[2], point[3], marker=("."), color=color[idxC])
        plt.title(" #{} / global mean :{:.5f}".format(globalIdx, globalVar))
        axes.legend()

    def draw2d(header, wich):
        plt.figure()
        axes = plt.axes()
        axes.set_xlabel(header[wich[0]])
        axes.set_ylabel(header[wich[1]])
        color = ["red", "blue", "green", "magenta"]
        for idx, point in enumerate(centroids):
            plt.plot(point[wich[0]], point[wich[1]], marker=("x"), color=color[idx], label="Cluster  #{}, mean distance of {:.2f}".format(idx, var[idx]))
        for idxC, cluster in enumerate(clusters):
            for point in cluster:
                plt.plot(point[1:][wich[0]], point[1:][wich[1]], marker=("."), color=color[idxC])
        plt.title(" #{} / variance of means :{:.5f}".format(globalIdx, globalVar))
        axes.legend()
    if (not isinstance(kmean, list)):
        print("kmean need to be list")
        return
    draw3d()
    for idx, _ in enumerate(header):
        draw2d(header, [idx, (idx + 1) % len(header)])
    plt.show()


def drawK(title, header, X, fit):
    def draw3d():
        plt.figure()
        axes = plt.axes(projection='3d')
        axes.set_xlabel(header[0])
        axes.set_ylabel(header[1])
        axes.set_zlabel(header[2])
        color = mcolors.TABLEAU_COLORS
        for point, clr in zip(X, fit):
            plt.plot(point[0], point[1], point[2], marker=("."), color=list(color.values())[clr])
        plt.title(title)

    def draw2d(header, wich):
        plt.figure()
        axes = plt.axes()
        axes.set_xlabel(header[wich[0]])
        axes.set_ylabel(header[wich[1]])
        color = mcolors.TABLEAU_COLORS
        for point, clr in zip(X, fit):
            plt.plot(point[wich[0]], point[wich[1]], marker=("."), color=list(color.values())[clr])
        plt.title(title)
    draw3d()
    for idx, _ in enumerate(header):
        draw2d(header, [idx, (idx + 1) % len(header)])


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    # calculate distance between two points, multidimensional
    # Return none if pointA or B is not a list
    def distCalc(self, pointA, pointB):
        if (not (isinstance(pointA, np.ndarray) or isinstance(pointB, np.ndarray))):
            raise TypeError("invalid type inside for point calculation.")
        return sqrt(sum((pointA - pointB)**2))

    # Kmeans algorithm
    # https://neptune.ai/blog/k-means-clustering
    # update self.centroids with ncentroid-th points
    def kmeans(self, X):
        tracks = []  # keep tracks of calculated clusters [clusters, centroids, variance]
        # stop when max_iter is reach
        for _ in tqdm(range(self.max_iter)):
            self.centroids = np.array([X[i] for i in np.random.choice(X.shape[0], self.ncentroid, replace=False)])  # init random value for centroids
            it = 0  # keep track of iteration
            # while convergence of centroids is not found
            while True:
                clusters = [[] for _ in range(ncentroid)]  # init cluster array of ncentroid array
                # iterate on point inside 'X' array
                for point in X:
                    dist = np.array([self.distCalc(point, centroid) for centroid in self.centroids])  # array containing the distance between 'point' and ncentroid's point
                    minIdx = dist.tolist().index(np.amin(dist))  # find the shorter distance
                    clusters[minIdx].append(np.array(point))  # add the point to the corresponding cluster
                newCentroids = np.array([[np.array(cluster)[:, (pos)].mean() for pos in range(len(cluster[0]))] for cluster in clusters])  # get the mean point for each cluster
                comparison = newCentroids == np.array(self.centroids)  # is last centroids array equal to actual centroids array?
                # True case
                if (not comparison.all()):
                    self.centroids = newCentroids  # change centroids value to new mean
                    it += 1  # count iteration
                else:
                    # calculate the mean of distance for each cluster (ncentroid)
                    newVar = [np.sum(np.array([self.distCalc(point, centroid) for point in cluster])) for cluster, centroid in zip(clusters, self.centroids)]
                    tracks.append([clusters, self.centroids, newVar])  # keep tracks of the clustering
                    break  # centroids doesn't change, clustering ended
        result = [0, 0, np.Inf]  # [iteration idx, track, mean of mean of the distance of each cluster]
        # iterate through tracks to find the most relevant clustering
        for idx, track in enumerate(tracks):
            # save the track with the lowest mean
            if (result[2] > np.sum(track[2])):
                result = [idx, track, np.sum(track[2])]
        self.centroids = result[1][1]

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
        self.kmeans(X)

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
        result = []
        for point in X:
            dist = np.array([self.distCalc(point, centroid) for centroid in self.centroids])  # array containing the distance between 'point' and ncentroid's point
            minIdx = dist.tolist().index(np.amin(dist))  # find the shorter distance
            result.append(minIdx)
        return result

    def identify(self, X):
        """
        find matches between clusters and the citizens' homelands
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension 4 * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        print(f"The centroids are : \n{self.centroids}")

        tallest = max(i[0] for i in self.centroids)
        belt_colony = [i for i in self.centroids if i[0] == tallest]
        slender = min(i[1] for i in self.centroids if (i != belt_colony[0]).all())

        venus_colony = [i for i in self.centroids if i[1] == slender and all(i != belt_colony[0])]
        mars_and_earth_colony = [i for i in self.centroids if (all(i != belt_colony[0]) and all(i != venus_colony[0]))]
        size_mars = max(mars_and_earth_colony[0][0], mars_and_earth_colony[1][0])
        mars_colony = [i for i in self.centroids if i[0] == size_mars]
        earth_colony = [i for i in mars_and_earth_colony if all(i != mars_colony[0])]

        print(f"The belt_colony centroid coordinates are {*belt_colony[0],} because they are the tallest")
        print(f"The venus_colony centroid coordinates are {*venus_colony[0],} because they are the slenderest")
        print(f"The mars_colony centroid coordinates are {*mars_colony[0],} because they are taller than the earth colony")
        print(f"The earth_colony centroid coordinates are {*earth_colony[0],} because they are smaller than the mars colony")


if not (2 <= len(sys.argv) <= 4):
    print("Invalid number of argument !")
    print("ex: Kmeans.py [PATH TO CSV] [number of centroids] [max iteration]")
    sys.exit()
path = sys.argv[1].split('=')[1]
try:
    ncentroid = 5  # default value of ncentroid
    max_iter = 20  # default value of max_iter
    if (len(sys.argv) >= 3):
        ncentroid = int(sys.argv[2].split('=')[1])  # if ncentroid specified on param
        if (ncentroid >= 10):
            print("ncentroid too high, max is 9")
            sys.exit()
        if (len(sys.argv) >= 4):
            max_iter = int(sys.argv[3].split('=')[1])  # if max_iter specified on param
    with CsvReader(path) as f:
        array = np.asarray(f.getdata())[1:-1, (1, 2, 3)].astype(float)  # create numpy array skipping last line (empty)
        header = np.asarray(f.getdata()[0])[1:].astype(str)

        kmClust = KmeansClustering(max_iter, ncentroid)  # init Kmean clustering class
        kmClust.fit(array)  # find best clustering
        mine_pred = kmClust.predict(array)

        model = KMeans(n_clusters=ncentroid, random_state=0).fit(array)
        kmean_pred = model.predict(array)
        error_prct = np.mean(mine_pred==kmean_pred)
        drawK("mine", header, array, mine_pred,)
        drawK("kmean", header, array, kmean_pred)
        kmClust.identify(array)
        plt.show()
except ValueError as e:
    print("One of the options is not an int")
    sys.exit()
