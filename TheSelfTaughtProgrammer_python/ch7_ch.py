# 1
show_list = ("ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ")
print("#1 リストの要素が表示できればOK。リスト={}".format(show_list))

# 2
print("#2 25から50の数値が出力されたらOK。")
for num in range(25, 51):
    print(num)

# 3
print("#3 #1のリストをインデックス値と一緒に出力できたらOK。")
for i, show in enumerate(show_list):
    print("index={}, show={}".format(i, show))

# 4
num_list = (1, 99)
print("#4 数値入力を求め，入力値が({})に含まれたら\"正解\"，含まれなけば\"不正解\"と表示する。".format(num_list))
while True:
    try:
        input_val = input("数字を入力するか，qで終了します: ")
        if input_val == "q":
            break
        input_num = int(input_val)
    except BaseException as e:
        print("入力値が不正です。エラー情報={}".format(str(e)))
        continue
    if input_num in num_list:
        print("正解")
    else:
        print("不正解")

# 5
list1 = (8, 19, 148, 4)
list2 = (9, 1, 33, 83)
print("#5 2つのリスト(リスト1={}, リスト2={})のそれぞれの要素をかけた値が出力されたらOK".format(list1, list2))
new_list = list()
for list1_val in list1:
    for list2_val in list2:
        new_list.append(list1_val * list2_val)
print(new_list)
