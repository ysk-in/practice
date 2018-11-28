import os
import csv

enc_utf8 = "utf-8"
line_sep = "\n"
base_dir = os.path.join("dir1", "dir1_1")
# 1
no1_rel_path = os.path.join(base_dir, "ch9_ch_#1.txt")
with open(no1_rel_path, "w", encoding=enc_utf8) as fobj:
    fobj.write("aaa\nbbb\nccc")
print("#1 ファイル({})の中身が出力されたらOK".format(no1_rel_path))
with open(no1_rel_path, "r", encoding=enc_utf8) as fobj:
    print(fobj.read())

# 2
no2_rel_path = os.path.join(base_dir, "ch9_ch_#2.txt")
with open(no2_rel_path, "a", encoding=enc_utf8) as fobj:
    new_line = input("入力された文字列をファイル({})に追記します: ".format(
        os.getcwd() + os.path.sep + no2_rel_path))
    try:
        fobj.write(new_line)
    except BaseException as e:
        print("write failed. e=" + str(e))

# 3
data_to_write = [
    ["Top Gun", "Risky Business", "...1"],
    ["Titanic", "The Revenant", "...2"],
    ["Training Day", "Man on Fire", "...3"]
]
no3_rel_path = os.path.join(base_dir, "ch9_ch_#3.txt")
with open(no3_rel_path, "w", encoding=enc_utf8, newline=line_sep) as f:
    w = csv.writer(f, delimiter=",")
    for d in data_to_write:
        w.writerow(d)

# 4
data_to_write = [
    ["とっぷがん", "りすきーびじねす", "...1"],
    ["ＴＩＴＡＮＩＣ", "㋹㋹辨と", "...2"],
    ["Training Day", "Man on Fire", "...3"]
]
no4_rel_path = os.path.join(base_dir, "ch9_ch_#4.txt")
with open(no4_rel_path, "w", encoding=enc_utf8, newline=line_sep) as f:
    w = csv.writer(f, delimiter=",")
    for d in data_to_write:
        w.writerow(d)
