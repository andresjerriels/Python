def add(num1, num2):
    """Return num1 plus num2"""
    return num1 + num2


def sub(num1, num2):
    """Return num1 minus num2"""
    return num1 - num2


def mul(num1, num2):
    """Return num1 times num2"""
    return num1 * num2


def div(num1, num2):
    """Return num1 divided num2"""
    return num1 / num2


def main():
    print("Hello")
    while True:
        InvalidInput = False
        while not InvalidInput:
            try:
                Operation = int(input("What do you want to do? (1. Add, 2. Subtract, 3. Multiply, 4. Divide 5. Exit the program). Enter a number:"))
                if (Operation == 5):
                    print("Please wait...")
                    break
                num1 = int(input("What is number 1?"))
                num2 = int(input("what is number 2?"))
                InvalidInput = True
            except:
                print("Invalid input. Try again!")

        if(Operation == 1):
            print("Adding...")
            print(add(num1, num2))
        elif(Operation == 2):
            print("Subtracting...")
            print(sub(num1, num2))
        elif (Operation == 3):
            print("Multiplying...")
            print(mul(num1, num2))
        elif (Operation == 4):
            print("Dividing...")
            print(div(num1, num2))
        elif (Operation == 5):
            print("Exiting program... Thank you!")
            break
        else:
            print("ERROR. Try again!")


main()
