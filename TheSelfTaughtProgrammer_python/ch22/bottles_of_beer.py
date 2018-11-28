def bottles_of_beer(remain_beer_num):
    if remain_beer_num < 1:
        print("No more ...")
        return
    print("{} bottles ... Take one down, ... {} bottles ...".format(remain_beer_num, remain_beer_num - 1))
    remain_beer_num -= 1
    bottles_of_beer(remain_beer_num)


bottles_of_beer(100)
