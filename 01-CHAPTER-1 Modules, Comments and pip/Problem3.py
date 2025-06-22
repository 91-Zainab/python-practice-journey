#Write a python program to print the contents of a directory using the os module. search online for the function which does that.

import os

# Specify the directory path; use os.getcwd() for current directory
directory_path = os.getcwd()

try:

    entries = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
