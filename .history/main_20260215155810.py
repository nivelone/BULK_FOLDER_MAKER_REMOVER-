# Function to make bulk directories and remove bulk directories

import os

#Make dir Bulk
def mk_dir_bulks(n,folder_name,path): 
    os.chdir(path) 
    for i in range(0,n):
        
        os.mkdir(f"{path}/{folder_name} { i+1}") 
    print("Folder created ! Successfully")  

#Remove dir Bulk
def remove_dir_bulks(folder_name,path):
    folderlist=os.listdir(path)
    for i in range(len(folderlist)):
        os.chdir(path) 
        os.rmdir(f"{folder_name} { i+1}")
    print("="*80)    
    print("All Folders Successfully Removed")
    print("="*80)
#####Calling the fucntions#####

print("="*80)
print(f"{"Welcome Bulk File Making and removing":<18}")
print("="*80)
print(f"{"1. Create bulk folders (specify the directory and number of directory to creat)":<18}")
print(f"{"2. Remove directory":<18}")
print(f"{"3.Quit":<18}")
user=int(input("Enter Your choice : "))
while user!=3:
    if user==1:
        n=int(input("Enter number of directory to be created :"))
        name=input("Enter the name of the directory :")
        path=input("Give the path where you want to create the directory :")
        mk_dir_bulks(n,name,path)
        user=int(input("Enter Your choice : "))
    elif user==2:
        name=input("Enter the name of the folder to be removed :")
        path=input("Give the path were the directory is located :")
        remove_dir_bulks(name,path)
        user=int(input("Enter Your choice : "))
    elif user==3:
        print("="*80)
        print("Thanks for using more update will come in future....")
        print("="*80)
        break
    else:
        print("="*80)
        print("Invalid Input! Please choose an option from the given options!.")
        print("="*80)

        

    

# mk_dir_bulks(100,"Practice day","e:/coding-projects/practise/os module introduction/data")

# remove_dir_bulks("Practice day","e:/coding-projects/practise/os module introduction/data")        
 