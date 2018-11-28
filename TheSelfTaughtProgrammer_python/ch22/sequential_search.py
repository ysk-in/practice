def ss(nums, num):
    return num in nums


if __name__ == "__main__":
    numbers = range(0, 100)
    print(ss(numbers, 2))
    print(ss(numbers, 200))
