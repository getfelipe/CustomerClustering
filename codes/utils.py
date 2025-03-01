import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib.colors import ListedColormap

# Plot cluster is a function to plot the cluster that KMeans classified, it takes the centers of each cluster and also all results classified.
def plot_clusters(df, cols, n_colors, centers, col_clusters):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    
    colors = plt.cm.tab10.colors[:n_colors]
    colors = ListedColormap(colors)
    
    for i, center in enumerate(centers):
        ax.scatter(*center, s=250, alpha=0.5)
        ax.text(*center, i, fontsize=12, horizontalalignment="center", verticalalignment="center")
        
        
    s = ax.scatter(df[cols[0]], df[cols[1]], df[cols[2]], c=df[col_clusters], cmap=colors)
    ax.legend(*s.legend_elements(), bbox_to_anchor=(1.4, 0.8))
    ax.set_xlabel("Age")
    ax.set_ylabel("Annual Income (k$)")
    ax.set_zlabel("Spending Score (1-100)")
    
    plt.show()
    
# Elbow has the aim to verify what is the elbow, taking in considerations a range between 2, 11, get the cost function inertia_, which is the distance between the points and centroids.
# Silhoute, on other hand, considers the quality of clusters, if the points is within its cluster compared to others.
def elbow(X, random_state=12, range_k=(2, 11)):
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 4), tight_layout=True)
    
    elbow = {}
    silhouette = []
    
    n_clusters = range(*range_k)
    RANDOM_STATE=14
    
    for n in n_clusters:
        kmeans = KMeans(n_clusters=n, random_state=random_state, n_init=10)
        kmeans.fit(X)
        elbow[n] = kmeans.inertia_
        labels = kmeans.labels_
        silhouette.append(silhouette_score(X, labels))
    
    sns.lineplot(x=list(elbow.keys()), y=list(elbow.values()), ax=axs[0])
    axs[0].set_xlabel("K")
    axs[0].set_ylabel("Inertia")
    axs[0].set_title("Elbow")
    
    sns.lineplot(x=n_clusters, y=silhouette, ax=axs[1])  # Fix n_clusters as a list
    axs[1].set_ylabel("Silhouette Score")
    axs[1].set_xlabel("K")
    axs[1].set_title("Silhouette")

    plt.show()