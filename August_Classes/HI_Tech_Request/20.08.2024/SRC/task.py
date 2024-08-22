import os
import shutil


path = r"E:\MY_DATA\newdata.txt"
backup_dir = r"E:\My_Backup_Files"

if os.path.exists(path):
    choice = input(f"Would you like to delete {path}? (Y/N): ")
    if choice.lower() == "y":
        response = input("Would you like to create a backup before deletion? (Y/N): ")
        
        if response.lower() == "y":
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            backup_path = os.path.join(backup_dir, os.path.basename(path))
            
            shutil.copy(path, backup_path)
            print("File backed up successfully.")
            
            os.remove(path)
            print("File has been deleted successfully.")
        
        elif response.lower() == "n":
            os.remove(path)
            print("File has been deleted successfully.")
        
        else:
            print("Please enter 'Y' or 'N'.")
    
    elif choice.lower() == "n":
        print("File has not been deleted.")
    
    else:
        print("Please enter 'Y' or 'N'.")
else:
    print("File not found.")
