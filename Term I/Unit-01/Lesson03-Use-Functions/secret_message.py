import os


def rename_files():
    # (1) Get filenames from the directory called "prank/"
    file_list = os.listdir(r"E:\udacity-full-stack-nanodegree\Term I\Unit-01\Lesson03-Use-Functions\prank")

    # We are using it since the `os.rename()` method renames files inside the current directory.
    # But, we want to change the names of files inside the `prank` directory.
    saved_path = os.getcwd()
    os.chdir(r"E:\udacity-full-stack-nanodegree\Term I\Unit-01\Lesson03-Use-Functions\prank")

    # (2) Rename all the files in the directory "prank/"
    for file_name in file_list:
        # Each of the numeric digit (as in first argument) would be replaced with a whitespace.
        translation_table = str.maketrans("", "", "0123456789")
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(translation_table) + "\n")
        os.rename(file_name, file_name.translate(translation_table))

    # Going back to the previously working directory.
    os.chdir(saved_path)


rename_files()
