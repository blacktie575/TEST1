# tools/test.py
from enum import Enum
from number.simp import add_numbers, subtract_numbers
from number.comp import sum_of_digits, is_palindrome
from col import myzip

class MenuOption(Enum):
    ADD_NUMBERS = 1
    SUBTRACT_NUMBERS = 2
    SUM_OF_DIGITS = 3
    IS_PALINDROME = 4
    MYZIP = 5
    EXIT = 6

# Flag to check if a function from simp.py was called
simp_function_called = False

def get_user_numbers():
    """Get user input for numbers."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def test_add_numbers():
    global simp_function_called
    num1, num2 = get_user_numbers()
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
    simp_function_called = True

def test_subtract_numbers():
    global simp_function_called
    # Check if a function from simp.py was called before allowing this function
    if not simp_function_called:
        print("Error: Function from simp.py must be called before test_subtract_numbers.")
        return

    num1, num2 = get_user_numbers()
    result = subtract_numbers(num1, num2)
    print(f"The difference of {num1} and {num2} is: {result}")

def test_sum_of_digits():
    global simp_function_called
    # Check if a function from simp.py was called before allowing this function
    if not simp_function_called:
        print("Error: Function from simp.py must be called before test_sum_of_digits.")
        return

    number = int(input("Enter a number: "))
    result = sum_of_digits(number)
    print(f"The sum of digits in {number} is: {result}")

def test_is_palindrome():
    global simp_function_called
    # Check if a function from simp.py was called before allowing this function
    if not simp_function_called:
        print("Error: Function from simp.py must be called before test_is_palindrome.")
        return

    number = int(input("Enter a number: "))
    result = is_palindrome(number)
    print(f"{number} is a palindrome: {result}")

def test_myzip():
    global simp_function_called
    # Check if a function from simp.py was called before allowing this function
    if not simp_function_called:
        print("Error: Function from simp.py must be called before test_myzip.")
        return

    print("Enter two lists to zip:")
    list1 = input("Enter elements for the first list (comma-separated): ").split(',')
    list2 = input("Enter elements for the second list (comma-separated): ").split(',')
    
    try:
        result = myzip(list(map(float, list1)), list(map(str, list2)))
        print("Result of myzip function:")
        print(result)
    except ValueError:
        print("Error: Please enter valid numeric values for the first list.")

if __name__ == "__main__":
    while True:
        # Display menu
        print("\nChoose an option to Test -WARNING --Make sure you use function from 'simp' BEFORE using function From 'comp':")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Calculate the sum of digits")
        print("4. Check if a number is a palindrome")
        print("5. Use myzip function")
        print("6. Exit")

        # Get user choice
        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Perform the chosen operation
        if choice == MenuOption.ADD_NUMBERS.value:
            test_add_numbers()
        elif choice == MenuOption.SUBTRACT_NUMBERS.value:
            test_subtract_numbers()
        elif choice == MenuOption.SUM_OF_DIGITS.value:
            test_sum_of_digits()
        elif choice == MenuOption.IS_PALINDROME.value:
            test_is_palindrome()
        elif choice == MenuOption.MYZIP.value:
            test_myzip()
        elif choice == MenuOption.EXIT.value:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid menu option.")
