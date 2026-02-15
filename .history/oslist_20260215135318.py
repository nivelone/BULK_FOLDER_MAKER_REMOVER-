import os

folders=os.listdir('data')
print(os.getcwd())
os.chdir("/data/Tutorial 10")

# for folder in folders:
#     print(folder)
#     print(os.listdir(f'data/{folder}'))