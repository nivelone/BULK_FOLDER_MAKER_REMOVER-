# Function to make bulk directories and remove bulk directories

import os

#Make dir Bulk
def mk_dir_bulks(n,folder_name,path): 
    for i in range(0,n):
        os.chdir(path) 
        os.mkdir(f"{path}/{folder_name} { i+1}") 
    print("Folder created ! Successfully")  

#Remove dir Bulk
def remove_dir_bulks(folder_name,path):
    folderlist=os.listdir(path)
    for i in range(len(folderlist)):
        os.chdir(path) 
        os.rmdir(f"{folder_name} { i+1}")
    return "All Folders Successfully Removed"

#####Calling the fucntions#####

# mk_dir_bulks(100,"Practice day","e:/coding-projects/practise/os module introduction/data")

remove_dir_bulks("Practice day","e:/coding-projects/practise/os module introduction/data")        
 