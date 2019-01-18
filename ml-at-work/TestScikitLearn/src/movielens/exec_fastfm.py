from sklearn.feature_extraction import DictVectorizer


def test_fastfm():
    train = [
        {"user": "1", "item": "5", "age": 19},
        {"user": "2", "item": "43", "age": 33},
        {"user": "3", "item": "20", "age": 55},
        {"user": "4", "item": "10", "age": 20},
    ]

    v = DictVectorizer()
    x = v.fit_transform(train)
    print(x.toarray())
