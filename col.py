def myzip(it1, it2):
    """zip function for 2 collections."""
    # Determine the minimum length of the input iterables
    min_length = min(len(it1), len(it2))
    
    # Create tuples by pairing elements based on their positions
    zipped = [(it1[i], it2[i]) for i in range(min_length)]
    
    return zipped

def main():
    while True:
        print("Enter two lists to zip:")
        
        # Get input from the user
        list1 = input("Enter elements for the first list (comma-separated): ").split(',')
        list2 = input("Enter elements for the second list (comma-separated): ").split(',')

        # Using the custom myzip function
        result = myzip(list1, list2)
        print("Result of myzip function:")
        print(result)

        # Ask if the user wants to zip more lists
        choice = input("Do you want to zip more lists? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
