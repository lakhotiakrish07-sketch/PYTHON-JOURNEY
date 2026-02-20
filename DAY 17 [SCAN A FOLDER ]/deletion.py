import os
folder_location=input("type folder location:")
if os.path.isdir(folder_location):
    print("folder found")
    for items in os.listdir(folder_location):
        print(items)
        item_path = os.path.join(folder_location,items)
        if os.path.isdir(item_path) and not os.listdir(item_path):
            print("it is a empty folder")
            confirm = input("if you want to delete type |yes|").lower()
            if confirm=="yes":
                try:
                    os.rmdir(item_path)
                except:
                    print("premisson declined")    
            else:
                continue
else:
    print("folder not found")                


                