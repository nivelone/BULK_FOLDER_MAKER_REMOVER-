import os



def remove_files():
    for i in range(4,100):
        path=f"e:/coding-projects/practise/os module introduction/data/Tutorial {i}"
        os.chdir("e:/coding-projects/practise/os module introduction/data")
        # print(os.getcwd())
        # # for i in range(2,100):    
        os.rmdir(path)
 

 