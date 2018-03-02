import os

def rename_files():
    #(1) Get filenames from a directory/folder
    file_list = os.listdir(r"E:\Full Stack Web Developer Nanodegree\Lesson 3 - Use Functions\prank")
    saved_path = os.getcwd()        #We have to use it, since the `os.rename()` method renames files inside the current directory.
                                    #But, we want to change the names of files inside the `prank` directory.  
    os.chdir(r"E:\Full Stack Web Developer Nanodegree\Lesson 3 - Use Functions\prank")

    #(2) Rename all the files in the 'prank' directory
    for file_name in file_list:
        translation_table = str.maketrans("0123456789", "          ", "0123456789")     #Each of the numeric digit (as in first argument)
                                                                                        # would be replaced with a whitespace. 
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(translation_table) + "\n")
        os.rename(file_name, file_name.translate(translation_table))
    
    os.chdir(saved_path)            #Going back to the previously working directory.

rename_files()                      #Method is being called.