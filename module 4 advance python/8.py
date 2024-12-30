#  Write a Python program to write a list to a file. 

def write_list_to_file(file_path, data_list):
    
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")  
        print(f"Data has been written to {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = "example.txt"  
data_list = ['apple', 'banana', 'cherry', 'date']
write_list_to_file(file_path, data_list)
