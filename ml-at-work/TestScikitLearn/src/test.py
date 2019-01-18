def train_test_split(*arrays, **options):
    print("type of arrays = {}".format(type(arrays)))
    print("type of options = {}".format(type(options)))
    for a in arrays:
        print(a)
    for key, val in enumerate(options):
        print("key={}, val={}, options[val]={}".format(key, val, options[val]))


def call_train_test_split():
    X_dev = [1, 2, 3]
    y_dev = [11, 22, 33]
    train_test_split(X_dev, y_dev, test_size=0.1, random_state=42)


def main():
    call_train_test_split()


if __name__ == "__main__":
    main()
