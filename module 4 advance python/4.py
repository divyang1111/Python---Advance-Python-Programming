#   Write a Python program to read a file line by line and store it into a list 

def read_file_to_list(file_path):
   
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
            lines = [line.strip() for line in lines]  # Remove leading/trailing whitespace
        return lines
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "example.txt"  
lines_list = read_file_to_list(file_path)

if isinstance(lines_list, list):
    print("Lines stored in the list:")
    print(lines_list)
else:
    print(lines_list)  
