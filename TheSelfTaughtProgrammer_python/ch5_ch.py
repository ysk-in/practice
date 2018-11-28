# 1
m_list = ["m1", "m2"]
print(m_list)
m_list.append("musician3")
print(m_list)

# 2
p1 = (10.0, 20.0)
p2 = (111.1, 222.2)
p_list = [p1, p2]
print(p_list)

# 3
dict = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
}
print(dict)

# 4
key = input("input the key: ")
if key in dict:
    print(dict[key])
else:
    print("key=" + str(key) + " not in dict.")

# 5
m_dict = {}
for m in m_list:
    if m == "m1":
        m_dict[m] = "m1_m"
    else:
        m_dict[m] = str(m) + "_Music"
print(m_dict)

# 6
s_val = set()
s_val.add("s1")
s_val.add("s2")
print(s_val)
s_val = set(m_list)
s_val.add("m1")
s_val.add("m1")
print(s_val)
print("difference(m1) = " + str(s_val.difference(["m1"])))
