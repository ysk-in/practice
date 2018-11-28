import os
import locale
import csv

enc_utf8 = "utf-8"

# readテスト
base_dir = os.path.join("dir1", "dir1_1")
file1_rel_path = os.path.join(base_dir, "file1")
file1_obj = open(file1_rel_path, "r")
for line in file1_obj.readlines():
    print(line)
print("read end")
file1_obj.close()

# writeテスト
file2_rel_path = os.path.join(base_dir, "file2")
file2_obj = open(file2_rel_path, "w", encoding=enc_utf8)
file2_obj.write("こんにちは Python から！\n2行目\r\n3行目\r4行目")
file2_obj.close()

# with openをreadテスト
with open(file2_rel_path, "r", encoding=enc_utf8) as fobj:
    print(fobj.read())

print("locale.getpreferredencoding()=" + locale.getpreferredencoding())

csv_rel_path = os.path.join(base_dir, "self_taught.csv")
with open(csv_rel_path, "w", encoding=enc_utf8, newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])
input("write終了")

with open(csv_rel_path, "r", encoding=enc_utf8) as f:
    print(f.read())
