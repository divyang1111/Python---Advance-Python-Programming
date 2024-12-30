#  Write a Python program to read an entire text file.  

def read_file(file_path):
   
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "example.txt"  
file_content = read_file(file_path)
print(file_content)
