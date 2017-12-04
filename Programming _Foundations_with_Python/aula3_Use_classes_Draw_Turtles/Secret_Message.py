import os

files_address = r"C:\Users\rcoelho\Downloads\prank\prank"

def rename_files():
    # 1 Get file names from folder
    file_list =  os.listdir(files_address)
    print(file_list)

    saved_path = os.getcwd() # In the end go back to saved_path
    print("Current directory " + saved_path)
    os.chdir(files_address)

    # 2 For each file - Rename (strip numbers)
    table = str.maketrans(dict.fromkeys('0123456789'))
    for file_name in file_list:
        #https://stackoverflow.com/questions/41708770/translate-function-in-python-3
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(table))
        os.rename(file_name, file_name.translate(table))

    os.chdir(saved_path) # Go back to the source path

rename_files()

