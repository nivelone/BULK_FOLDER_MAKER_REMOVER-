import os

path="e:/coding-projects/practise/os module introduction/data"

os.chdir("e:/coding-projects/practise/os module introduction/data")
print(os.listdir(path))
print(os.getcwd())
os.rmdir(path)
 