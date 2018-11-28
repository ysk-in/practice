for num in range(1, 101):
    r3 = num % 3
    r5 = num % 5
    if not r3 and not r5:
        print("FizzBuzz")
    elif not r3:
        print("Fizz")
    elif not r5:
        print("Buzz")
    else:
        print(num)
