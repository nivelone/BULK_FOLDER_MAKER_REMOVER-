import os

path="e:/coding-projects/practise/os module introduction/data"
# print(os.getcwd())
os.remove("e:/coding-projects/practise/os module introduction/data/Tutorial")

for folder in path:
    os.rmdir("e:/coding-projects/practise/os module introduction/data/Tutorial {i}")