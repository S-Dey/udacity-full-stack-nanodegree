import os

def rename_files():
    #(1) Get filenames from a directory/folder
    file_list = os.listdir(r"E:\Full Stack Web Developer Nanodegree\Lesson 3 - Use Functions\prank")
    saved_path = os.getcwd()        #We have to use it since the `os.rename()` method renames files in the current directory only.
                                    #But, we want to change the names of files in the `prank` directory.  
    os.chdir(r"E:\Full Stack Web Developer Nanodegree\Lesson 3 - Use Functions\prank")

    #(2) Rename all the files in the 'prank' directory
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
    os.chdir(saved_path)            #Going back to the previously working directory.

rename_files()                      #Method is being called.