import glob
import os

for file_name in glob.glob(r"C:\git\study\ml-at-work\TestScikitLearn\src\kickstarter\result\*"):
    os.rename(file_name, file_name + ".json")
