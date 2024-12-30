#  Write a Python program to count the number of lines in a text file.

def count_lines(file_path):
   
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  
            return len(lines)  
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "example.txt"  
line_count = count_lines(file_path)

if isinstance(line_count, int):
    print(f"The number of lines in the file is: {line_count}")
else:
    print(line_count)  
