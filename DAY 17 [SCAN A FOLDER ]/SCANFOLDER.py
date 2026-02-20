import os
folder_name = input("write the folder name location ")
if os.path.isdir(folder_name):
    print("yes it found")
    for items in os.listdir(folder_name):
        print(items)   
        if not os.listdir(items):
            confirmation = input("type DELETE:")
            if confirmation =="DELETE":
                os.rmdir(items)
            else:continue      
else:
    print("folder not found")    

  