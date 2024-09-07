import random
import string

def generate_password(length):
    # Define character sets for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user to specify the length of the password
        length = int(input("Enter the desired length for the password: "))

        # Validate the length
        if length < 1:
            print("Password length must be at least 1.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Error: Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()
