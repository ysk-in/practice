test_list = ["aaa", "bbb"]
print("module1 name={}".format(__name__))

if __name__ == "__main__":
    print("Hello")

    print(test_list)
    test_list.append("ccc")

