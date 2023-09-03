import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    # Define character sets for password generation
    upper_chars = string.ascii_uppercase if use_upper else ''
    lower_chars = string.ascii_lowercase if use_lower else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special else ''

    # Combine selected character sets
    all_chars = upper_chars + lower_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        return "Please select at least one character set."

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(f"Generated Password: {generated_password}")