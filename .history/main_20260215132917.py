import os 

if(os.path.exists()):
    os.mkdir('data')

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")