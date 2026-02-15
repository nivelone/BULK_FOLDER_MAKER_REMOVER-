import os 

# if(not os.path.exists("data")):
#     os.mkdir('data')

for i in range(0, 100):
    os.rename(f"data/Tutorial{i+1}",f"data/Tutorial {i+1}")


# mk_dir_bulks(50,"Aman","e:/coding-projects/practise/os module introduction/data")
