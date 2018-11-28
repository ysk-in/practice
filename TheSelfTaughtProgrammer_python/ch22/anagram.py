def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    print("sorted(w1)={}, sorted(w2)={}".format(sorted(w1), sorted(w2)))
    return sorted(w1) == sorted(w2)


print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))
print(anagram("アナグラムにしたい文字列を入力してください。漢字等が混ざっても良いですが、半角英数字や記号には対応していません。",
              "ざ等記応列てくさいせ字はい角を。まい力ナ号て混で字ラグにしい。文ム、し英も対数だアんやてが字しが入半良たっにす漢"))
