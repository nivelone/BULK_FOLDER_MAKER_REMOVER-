# Function to make bulk directories and remove bulk directories

import os

#Make dir Bulk
def mk_dir_bulks(n,folder_name,path): 
    for i in range(0,n):
        
        os.mkdir(f"{path}{folder_name} { i+1}") 
    print("="*80)
    print("Folder created ! Successfully")  
    print("="*80)

#Remove dir Bulk
def remove_dir_bulks(folder_name,path):
    os.chdir(path)
    folderlist=os.listdir(path)
    for i in range(len(folderlist)):
         
        os.rmdir(f"{folder_name} { i+1}")
    print("="*80)    
    print("All Folders Successfully Removed")
    print("="*80)



#####Calling the fucntions#####
def display_cli():
    print("="*80)
    print("Welcome Bulk File Making and Removing".center(80))
    print("="*80)
    print("1. Create bulk folders (specify directory and number)".center(80))
    print("2. Remove directory".center(80))
    print("3. Quit".center(80))
user=int(input("Enter Your choice : "))
display_cli()
while True:
    if user==1:
        n=int(input("Enter number of directory to be created :"))
        name=input("Enter the name of the directory :")
        path=input("Give the path where you want to create the directory :")
        mk_dir_bulks(n,name,path)
        display_cli()
        user=int(input("Enter Your choice : "))
    elif user==2:
        name=input("Enter the name of the folder to be removed :")
        path=input("Give the path were the directory is located :")
        remove_dir_bulks(name,path)
        display_cli()
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
        display_cli()

        

       
 