def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y
def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("enter thr operator (+,-,*,/)")
        if operation == "+":
            result = add(num1,num2)
        elif operation == "-":
            result = subtract(num1,num2)
        elif operation == "*":
            result = multiply(num1,num2)
        elif operation == "/":
            result = divide(num1,num2)
        else:
            raise ValueError(f"Invalid operation {operation}")
        print(f"Result : {result}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()







        
