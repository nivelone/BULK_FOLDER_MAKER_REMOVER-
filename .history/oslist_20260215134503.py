import os

folders=os.listdir('data')
print(os.cwd)


for folder in folders:
    print(folder)
    print(os.listdir(f'data/{folder}'))