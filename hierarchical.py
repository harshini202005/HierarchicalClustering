

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import os

def generate_cluster_plots(clusters, output_dir='static'):
    
    X, _ = make_blobs(n_samples=100, centers=5, cluster_std=1.0, random_state=42)
    X = StandardScaler().fit_transform(X)


    Z = linkage(X, method='ward')

  
    plt.figure(figsize=(10, 6))
    dendrogram(Z)
    plt.axhline(y=6, color='r', linestyle='--')
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    dendrogram_path = os.path.join(output_dir, 'dendrogram.png')
    plt.savefig(dendrogram_path)
    plt.close()

    labels = fcluster(Z, clusters, criterion='maxclust')
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
    plt.title('Clustered Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    cluster_path = os.path.join(output_dir, 'clusters.png')
    plt.savefig(cluster_path)
    plt.close()

    return dendrogram_path, cluster_path
