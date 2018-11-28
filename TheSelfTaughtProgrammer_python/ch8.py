import math
import random
import statistics
import keyword

print(math.pow(2, 3))

nums = [33, 33]
for i in range(10):
    nums.append(random.randint(1, 100))
print("リスト({}) の 平均={}, 中央値={}, 最頻値={}".
      format(nums, statistics.mean(nums), statistics.median(nums), statistics.mode(nums)))

for i, keyword in enumerate(keyword.kwlist):
    print("i={}, keyword={}".format(i, keyword))
