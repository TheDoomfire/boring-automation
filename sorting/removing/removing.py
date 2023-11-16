import os

def remove_empty_folders(full_file_path):
    #os.rmdir(full_file_path)
    print("Running empty folders")
    #print(full_file_path)
    #print(os.listdir(full_file_path))
    for item in os.listdir(full_file_path):
        #print(item)
        the_path = full_file_path + "\\" + item
        #print(os.path.isdir(the_path))
        if os.path.isdir(the_path):
            #print(the_path)
            #print(os.path.isdir(the_path))
            if not os.listdir(the_path): # IF folder is EMPTY!
                #print(os.path.join(full_file_path, item))
                os.removedirs(os.path.join(full_file_path, item))