import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def list_of_folder(path, indent="  "):
        for el in path.iterdir():
            if el.is_dir():
                print(f"{indent}{Fore.BLUE}📁 {el.name}")
                list_of_folder(el, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}📄 {el.name}")
                
def main():
    if len(sys.argv) > 1:
        path_to_directory = Path(sys.argv[1])
        if path_to_directory.exists() and path_to_directory.is_dir():
            directory = Path(path_to_directory)
            print(f"{Fore.YELLOW}📁 {path_to_directory.name}")
            list_of_folder(directory)
        else:
            print(f"{Fore.RED}The directory path is invalid or does not exist: {path_to_directory}")
    else:
         print(f"{Fore.YELLOW}Arguments are not provided")

if __name__ == "__main__":
    main()




