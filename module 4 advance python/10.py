''' Write python program that user to enter only odd numbers, else will 
raise an exception.  '''

def get_odd_number():
   
    try:
       
        number = int(input("Please enter an odd number: "))
        
        
        if number % 2 == 0:
            raise ValueError("The number is not odd! Please enter an odd number.")
        
        print(f"Thank you! You entered the odd number: {number}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
        get_odd_number()  


get_odd_number()
