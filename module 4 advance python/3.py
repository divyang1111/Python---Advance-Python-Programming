#  Write a Python program to read first n lines of a file. 

def read_first_n_lines(file_path, n):
   
    try:
        with open(file_path, 'r') as file:
            lines = [file.readline().strip() for _ in range(n)]
        return '\n'.join(lines)
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "example.txt"  
n = 3  
output = read_first_n_lines(file_path, n)
print(f"The first {n} lines of the file:")
print(output)
