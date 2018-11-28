i = 0

# 1
print("#1 カミュを1文字ずつ改行して出力できたらOK")
for i in "カミュ":
    print(i)

# 2
print("#2 input文字が正しく埋め文字になってればOK")
print("私は昨日 [{}] を書いて， [{}] に送った！".format(
    input("input 書いたもの: "), input("input 送り先: ")))

# 3
print("#3 文頭が大文字になってたからOK")
print("aldous Huxley was born in 1894.".capitalize())

# 4
val = "どこで？ 誰が？ いつ？"
print("#4 文字列({})を\" \"で区切ったリストが出力されたらOK".format(val))
print(val.split(" "))

# 5
val = ("The", "fox", "jumped", "a...z", ".")
print("#5 リスト({})が連結されて文字列になってればOK".format(val))
print(" ".join(val).replace(" .", "."))

# 6
val = "A screaming comes across the sky."
print("#6 文字列({})中の\"s\"が\"$\"に変わってればOK".format(val))
print(val.replace("s", "$"))

# 7
val = "Hemingway"
print("#7 文字列({})中の\"m\"のindexが出力されたらOK".format(val))
print(val.index("m"))

# 8
val = "好きな\"文章"
print("#8 文字列({}) \"ダブルクォート\"が出力されてたらOK".format(val))

# 9
val = "three"
print("#9 文字列({})が three three three と出力されてたらOK".format(val + " " + val + " " + val))
print("#9 文字列({})が three three three と出力されてたらOK".format(("three " * 3).strip()))

# 10
val = "ああああああああああ，いいいいいいい，ううううう，ええええ，お。"
print("#10 文字列({})中の先頭\",\"の手前までが出力されたらOK".format(val))
print(val[:val.index("，")])
