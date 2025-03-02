import os
directory_path=input("enter the  number")
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    content=os.listdir(directory_path)
    print(f"contents of directory'{directory_path}:")
    for items in content:
        print(items)
    else:
        print(f"the directory'{directory_path}'does not exist or is not valid directory ")
