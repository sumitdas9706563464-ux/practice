import random
import string
import re

def get_user_choice():
    print("Welcome to Password Generator")
    length = int(input("Enter password length: "))
    use_upper = input("Include upper case letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lower case letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
    return length, use_upper, use_lower, use_digits, use_symbols

def generate_password(length, upper, lower, digit, symbol):
    characters = ""
    password = []

    if upper:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if lower:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if digit:
        characters += string.digits
        password.append(random.choice(string.digits))
    if symbol:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        return "Error: no character types selected!"

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

def check_strength(password):
    strength = 0
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[@#$%^&*(),.?":{}<>|]', password):
        strength += 1

    if len(password) < 6:
        return "Very Weak"
    elif strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    else:
        return "Very Strong"

# Run the program
length, upper, lower, digits, symbols = get_user_choice()
generated = generate_password(length, upper, lower, digits, symbols)

print(f"\nYour generated password is: {generated}")
print(f"Password strength: {check_strength(generated)}")
