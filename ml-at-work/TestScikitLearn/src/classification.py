from math import sqrt

from sklearn import datasets, svm
from sklearn.metrics import confusion_matrix, mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

if __name__ == "__main__":
    digits = datasets.load_digits()
    data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target)
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(data_train, label_train)
    label_predict = clf.predict(data_test)
    print("label_test:\n{}\n"
          "label_predict\n{}\n".format(label_test, label_predict))


def print_confusion_matrix():
    n = np.where(label_predict != label_test)
    print("np_where={}\nlabel_test={}\nlabel_predict={}.".format(n[0], label_test[n[0]], label_predict[n[0]]))
    cm = confusion_matrix(label_test, label_predict)
    print(cm)


def main():
    print_confusion_matrix()


if __name__ == "__main__":
    main()
