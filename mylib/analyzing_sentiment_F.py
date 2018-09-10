import pickle
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score


def analyzing_sentiment(text):
    df = pd.read_csv('./data/refined_movie_review.csv')

    X_test = df.loc[15000:, 'review'].values
    y_test = df.loc[15000:, 'sentiment'].values

    curDir = os.getcwd()
    clf = pickle.load(open(os.path.join(curDir, 'data', 'pklObject', 'classifier.pkl'), 'rb'))

    y_pred = clf.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    label = {0: 'Negative', 1: 'Positive'}

    example = [text]
    predict = label[clf.predict(example)[0]]
    accuracy = np.max(clf.predict_proba(example)) * 100

    return test_accuracy, text, predict, accuracy
