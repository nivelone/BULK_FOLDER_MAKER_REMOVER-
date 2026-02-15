import os


path=f"e:/coding-projects/practise/os module introduction/data"

def remove_files(path):
    folderlist=os.listdir(path)
    while len(folderlist)!=0:
        os.chdir(path)
        # print(os.getcwd())
        # # for i in range(2,100):    
        os.rmdir(path)
    print("All files successfully deleted !")   
    
 
def mk_dir_bulks(n,folder_name): 
    for i in range(0,n):
        os.chdir("e:/coding-projects/practise/os module introduction/data") 
        os.mkdir(f"e:/coding-projects/practise/os module introduction/data/{folder_name} {i+1}") 


os.chdir("e:/coding-projects/practise/os module introduction/data") 
folderlist=os.listdir('e:/coding-projects/practise/os module introduction/data')


# print(len(folderlist))
if len(folderlist)==0:
    print("The dir is empty !")



 