import math
try:
    print("Choose an option:")
    print("1. sin")
    print("2. cos")
    print("3. tan")
    choice = int(input("Enter choice: "))
    num = int(input("Enter number: "))
    result = 0
    if choice == 1:
        result = math.tan(num)
        print(f"sin of {num} is: {result}")
    elif choice == 2:
        result = math.cos(num)
        print(f"cos of {num} is: {result}")
    elif choice == 3:
        result = math.cos(num)
        print(f"tan of {num} is: {result}")
except:
    print("Error")