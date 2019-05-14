from sklearn.cluster import KMeans

from utils import WIDERFaceDataset

dataset = WIDERFaceDataset()
k = 10
kmeans = KMeans(n_clusters=k)
