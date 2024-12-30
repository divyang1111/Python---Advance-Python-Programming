#  Write a python program to find the longest words.

def find_longest_words(file_path):
    
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()  
            max_length = max(len(word) for word in words)  
            longest_words = [word for word in words if len(word) == max_length] 
        return longest_words
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "example.txt"  
result = find_longest_words(file_path)

if isinstance(result, list):
    print("Longest word(s):")
    print(result)
else:
    print(result)  