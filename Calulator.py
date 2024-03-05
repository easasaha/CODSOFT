def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


print("Welcome to the Calculator App\n")
num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))


print("\n\t1. '+' Addition")
print("\t2. '-' Subtraction")
print("\t3. '*' Multiplication")
print("\t4. '/' Division") 
    
    
operator = input("\nPlease enter one of the above operator: ")
    
if operator == '+':
        print(f"The sum is {num1 + num2}")
        
elif operator == '-':
        print(f"The difference is {num1 - num2}")
        
elif operator == '*':
        print(f"The product is {num1 * num2}")
        
elif operator == '/':
        try:  # To handle division by zero error
            result = num1 / num2
            print(f"The quotient is {result}")
        except ZeroDivisionError:
            print("Error! Cannot divide by zero.")
    
    
else:
        print("Invalid operator!\n Please Enter a valid option.\n")
        
print("Thank You for using Calulator App!")