import sys
from pathlib import Path
from colorama import init, Fore, Style

def list_of_folder(path):
        for el in path.iterdir():
            if el.is_dir():
                list_of_folder(el)
                print(el.name)
            else:
                print(el.name)

def main():
    if len(sys.argv) >= 1:
        path_to_directory = Path(sys.argv[1])
        if path_to_directory.exists() and path_to_directory.is_dir():
            directory = Path(path_to_directory)
            list_of_folder(directory)
            print(f"Name of the directory: {path_to_directory.name}")
            print(f"Name: {directory}")
        else:
            print(f"Invalid directory path: {directory}")

        # print(f"Name of the directory: {directory.name}")
        # print(f"Path to the folder: {sys.argv[1]}")
    else:
         print(f"Arguments are not provided")

if __name__ == "__main__":
    main()




