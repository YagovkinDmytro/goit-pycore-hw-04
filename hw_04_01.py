from pathlib import Path

path_to_employees_file = Path("employees.txt")

def total_salary(path):
        with open(path, "r", encoding="utf-8") as employees_file:
            employees_info = [el.strip().split(",") for el in employees_file.readlines()]   

        total = 0
        for employee in employees_info:
            try:
                total += int(employee[1])
            except (ValueError, IndexError):
                raise ValueError(f"Error in data: {employee}")
        
        if len(employees_info) == 0:
            raise ValueError("File is empty or contains invalid data")
        
        average = int(total / len(employees_info))
        salary_info = (total, average)
        print(type(salary_info))
        return salary_info
        
    

if path_to_employees_file.exists():
    try:
        total, average = total_salary(path_to_employees_file)
        print(f"Total salary: {total}, average salary: {average}")
    except ValueError as e:
        print(f"Data processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
else:
    print("File not found")