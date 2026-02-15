import os

folders=os.listdir('data')
print(os.getcwd())
os.chdir("/coding-projects")
print(os.getcwd())
print(os.listdir("coding-projects")) 
# for folder in folders:
#     print(folder)
#     print(os.listdir(f'data/{folder}'))