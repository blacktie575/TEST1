from enum import Enum

class MenuOption(Enum):
    SUM_OF_DIGITS = 1
    IS_PALINDROME = 2
    EXIT = 3

def sum_of_digits(number):
    """Calculate the sum of digits in a given number."""
    num_str = str(number)
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum

def is_palindrome(number):
    """Check if a given number is a palindrome."""
    num_str = str(number)
    return num_str == num_str[::-1]

def main():
    while True:
        # Display menu
        print("\nChoose an option:")
        print("1. Calculate the sum of digits")
        print("2. Check if a number is a palindrome")
        print("3. Exit")

        # Get user choice
        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Perform the chosen operation
        if choice == MenuOption.SUM_OF_DIGITS.value:
            number = int(input("Enter a number: "))
            result = sum_of_digits(number)
            print(f"The sum of digits in {number} is: {result}")
        elif choice == MenuOption.IS_PALINDROME.value:
            number = int(input("Enter a number: "))
            result = is_palindrome(number)
            print(f"{number} is a palindrome: {result}")
        elif choice == MenuOption.EXIT.value:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid menu option.")

if __name__ == "__main__":
    main()
