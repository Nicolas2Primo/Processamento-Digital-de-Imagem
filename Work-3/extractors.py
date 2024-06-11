from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import PCA
from skimage.feature import hog
import numpy as np

def extract_hog_features(X):
    hog_features = []
    for img in X:
        img = img.reshape((35, 35))
        features = hog(img, pixels_per_cell=(5, 5), cells_per_block=(2, 2), visualize=False)
        hog_features.append(features)
    return np.array(hog_features)


def extract_lda_features(X, y, n_components=9):
    lda = LDA(n_components=n_components)
    return lda.fit_transform(X, y)


def extract_pca_features(X, n_components=50):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(X)