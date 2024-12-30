# Write a Python program to append text to a file and display the text.

def append_and_display(file_path, text_to_append):
   
    try:
       
        with open(file_path, 'a') as file:
            file.write(text_to_append + '\n')
        
       
        with open(file_path, 'r') as file:
            content = file.read()
        print("Updated file content:")
        print(content)
    
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = "example.txt" 
text_to_append = "This is the new line to append."
append_and_display(file_path, text_to_append)
 