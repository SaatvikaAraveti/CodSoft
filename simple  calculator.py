def add(m,n):
    return m+n
def subtract(m,n):
    return m-n
def multiply(m,n):
    return m*n
def divide(m,n):
    if n == 0:
        return "Cannot divide by zero."
    return m / n
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == '1':
        result = add(a,b)
    elif choice == '2':
        result = subtract(a,b)
    elif choice == '3':
        result = multiply(a,b)
    elif choice == '4':
        result = divide(a,b)
    else:
        result = "Invalid choice."
    print(f"Result: {result}")
calculator()