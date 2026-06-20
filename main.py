from src.data_preprocessing import load_data
from src.train_model import find_optimal_clusters, train_model
from src.visualize import plot_clusters

def main():

    df, X = load_data()

    print(df.head())

    find_optimal_clusters(X)

    kmeans, y_kmeans = train_model(X)

    plot_clusters(X, y_kmeans, kmeans)

if __name__ == "__main__":
    main()