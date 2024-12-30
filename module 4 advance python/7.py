#  Write a Python program to count the frequency of words in a file.

from collections import Counter
import re

def count_word_frequency(file_path):
   
    try:
        with open(file_path, 'r') as file:
            
            text = file.read()
            
            words = re.findall(r'\b\w+\b', text.lower())  
            
            word_count = Counter(words)
        return word_count
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "example.txt"  
word_frequency = count_word_frequency(file_path)

if isinstance(word_frequency, dict):
    print("Word frequency count:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")
else:
    print(word_frequency)  
