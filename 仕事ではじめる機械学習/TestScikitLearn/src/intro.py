from sklearn import datasets, svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


def test_confusion_matrix():
    digits = datasets.load_digits()

    data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target)

    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(data_train, label_train)
    label_predict = clf.predict(data_test)

    cm = confusion_matrix(label_test, label_predict)
    print(cm)


def main():
    test_confusion_matrix()


if __name__ == "__main__":
    main()
