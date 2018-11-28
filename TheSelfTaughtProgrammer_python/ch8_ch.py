import random
import statistics
import cubed

num_list = list()
for i in range(10):
    num_list.append(random.randint(1, 100))
num_list.sort()
print(num_list)

# 1
print("#1 statistics.median_high(num_list)={}, statistics.median_low(num_list)={}".format(
    str(statistics.median_high(num_list)), str(statistics.median_low(num_list))))

# 2
print("#2 cubed.pow3(3)={}".format(cubed.pow3(3)))
