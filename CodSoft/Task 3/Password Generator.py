import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special):
    #define the character sets to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    special = string.punctuation if include_special else ''

    #combine all characters
    all_characters = lower + upper + digits + special

    if not all_characters:
        print("No characeters types selected. Cannot generate a password.")
        return None
    
    #Generate the password
    password = ''.join(random.choice(all_characters)for _ in range(length))
    return password

def main():
    print("Strong Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of password: "))
            if length <= 0 :
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

            include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
            include_special = input("Include special characters? (yes/no):").lower() == 'yes'

            password  = generate_password(length, include_uppercase, include_numbers, include_special)

            if password:
                print(f"Generated password: {password}")

                another = input("Generate another password? (yes/no): ").lower()
                if another != 'yes':
                    break

            if __name__ == "__main__":
                 main()