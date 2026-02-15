import os


address=f"e:/coding-projects/practise/os module introduction/data"
print(os.getcwd())

os.chdir(address)
print(os.getcwd())




def mk_dir_bulks(n,folder_name,path): 
    for i in range(0,n):
        os.chdir(path) 
        os.mkdir(f"{path}/{folder_name} {i+1}") 
    print("Folder created ! Successfully")  


folderlist=os.listdir("e:/coding-projects/practise/os module introduction/data")
for i in range(len(folderlist)):
    os.rmdir("Aman 1")
        
 