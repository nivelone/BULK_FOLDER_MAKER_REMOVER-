import os


address=f"e:/coding-projects/practise/os module introduction/data"
print(os.getcwd())

os.chdir(address)

def remove_files(path):
      
    folderlist=os.listdir(path)
    print(f"dir changed ")

    
    # while len(folderlist)!=0:
       
    #     os.rmdir(path)
    # print("All files successfully deleted !")   
    
remove_files(address)

def mk_dir_bulks(n,folder_name,path): 
    for i in range(0,n):
        os.chdir(path) 
        os.mkdir(f"{path}/{folder_name} {i+1}") 





 