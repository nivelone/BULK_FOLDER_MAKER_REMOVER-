import os


address=f"e:/coding-projects/practise/os module introduction/data"

def remove_files(path):
    folderlist=os.listdir(path)
    while len(folderlist)!=0:
        os.chdir(path)  
        os.rmdir(path)
    print("All files successfully deleted !")   
    
 
def mk_dir_bulks(n,folder_name,path): 
    for i in range(0,n):
        os.chdir(path) 
        os.mkdir(f"{path}/{folder_name} {i+1}") 

print(os.getcwd())

remove_files(address)

 