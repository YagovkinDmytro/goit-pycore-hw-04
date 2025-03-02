from pathlib import Path

path_to_cats_file = Path("cats.txt")

def get_cats_info(path):
    cats_list = []
    with open(path, "r", encoding="utf-8") as cats_file:    
        for line in cats_file.readlines():
            try:
                id, name, age = line.strip().split(",")
                cats_list.append({"id": id, "name": name, "age": age})
            except (ValueError, IndexError):
                raise ValueError(f"Error in data: {line}") 
    return cats_list

if path_to_cats_file.exists():
    try:
        cats_info = get_cats_info(path_to_cats_file)
        print(cats_info)
    except ValueError as e:
        print(f"Data processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
else:
    print("File not found")