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


# mk_dir_bulks(50,"Aman","e:/coding-projects/practise/os module introduction/data")

 