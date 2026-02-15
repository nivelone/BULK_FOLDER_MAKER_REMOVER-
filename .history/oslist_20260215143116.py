import os



def remove_files():
    for i in range(4,100):
        path=f"e:/coding-projects/practise/os module introduction/data/Tutorial {i}"
        os.chdir("e:/coding-projects/practise/os module introduction/data")
        # print(os.getcwd())
        # # for i in range(2,100):    
        os.rmdir(path)
 
def mk_files(): 
    for i in range(0,100):
        os.chdir("e:/coding-projects/practise/os module introduction/data") 
        os.mkdir(f"e:/coding-projects/practise/os module introduction/data/Tutorial {i+1}") 


os.chdir("e:/coding-projects/practise/os module introduction/data") 
print(os.listdir('e:/coding-projects/practise/os module introduction/data').count())

 