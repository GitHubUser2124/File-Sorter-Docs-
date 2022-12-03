import os
import shutil

source = "/Users/shaikbhai/Downloads"
destination = "/Users/shaikbhai/Documents"

list_of_files = os.listdir(source)
print(list_of_files)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    if ext in [".pdf", ".xlx", ".zip", ".pkg", ".cmd", ".dmg", ".json"]:
        originalPath = source+"/"+i
        folderPath = destination+"/"+"Docs"
        finalPath = destination+"/"+"Docs"+"/"+i

        

        if(os.path.exists(folderPath)):
            shutil.move(originalPath,finalPath)
            print("Moving...")
        else:
            # If the Docs folder does not exist then we first create it 
            os.makedirs(folderPath)
            shutil.move(originalPath,finalPath)
            print("A_F_Z_A_L Bot is moving the files...")