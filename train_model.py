from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def find_optimal_clusters(X):

    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(
            n_clusters=i,
            init='k-means++',
            random_state=42
        )

        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1,11), wcss)
    plt.title("Elbow Method")
    plt.xlabel("Clusters")
    plt.ylabel("WCSS")
    plt.savefig("outputs/elbow_method.png")
    plt.show()

def train_model(X):

    kmeans = KMeans(
        n_clusters=5,
        init='k-means++',
        random_state=42
    )

    y_kmeans = kmeans.fit_predict(X)

    return kmeans, y_kmeans