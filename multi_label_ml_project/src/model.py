from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(X_train, y_train):

    base_model = LogisticRegression(max_iter=1000)
    model = OneVsRestClassifier(base_model)

    model.fit(X_train, y_train)
    return model


def save_model(model, path):
    joblib.dump(model, path)