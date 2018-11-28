try:
    "animals".index("z")
# except:
#     print("Not Found")
except BaseException as e:
    print("Not Found. e={}".format(e))
