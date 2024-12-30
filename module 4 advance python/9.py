#  Write a Python program to copy the contents of a file to another file. 

def copy_file_contents(source_file_path, destination_file_path):
    
    try:
        with open(source_file_path, 'r') as source_file:
            content = source_file.read()  
        
        with open(destination_file_path, 'w') as destination_file:
            destination_file.write(content)  
        
        print(f"Contents of {source_file_path} have been copied to {destination_file_path}.")
    except FileNotFoundError:
        print(f"Error: The file {source_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


source_file_path = "source.txt" 
destination_file_path = "destination.txt"  
copy_file_contents(source_file_path, destination_file_path)
