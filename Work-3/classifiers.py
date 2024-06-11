from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train_svm(X_train, y_train):
    svm = SVC(kernel='linear')
    svm.fit(X_train, y_train)
    return svm


def train_rf(X_train, y_train):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    return rf
